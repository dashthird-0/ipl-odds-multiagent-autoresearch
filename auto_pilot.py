#!/usr/bin/env python3
"""
Auto-Pilot — Fully autonomous match pipeline.

Discovers upcoming IPL matches from Polymarket, triggers the memo pipeline
at the right moment (post-toss, pre-first-ball), detects results from
market resolution, and auto-grades.

Runs every 5 minutes via cron. State machine per match:
  discovered → triggered → graded

Usage:
    python3 auto_pilot.py              # run once (check + act)
    python3 auto_pilot.py --dry-run    # show what would happen
    python3 auto_pilot.py --status     # show state
    python3 auto_pilot.py --install    # install local cron (every 5 min)
"""

import atexit
import json
import os
import signal
import subprocess
import sys
import tempfile
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError

PROJECT_ROOT = Path(__file__).parent
STATE_FILE = PROJECT_ROOT / "auto_pilot_state.json"
LOG_FILE = PROJECT_ROOT / "auto_pilot.log"
LOCK_FILE = PROJECT_ROOT / "auto_pilot.lock"
CASE_STUDIES_DIR = PROJECT_ROOT / "case_studies"

GAMMA_API = "https://gamma-api.polymarket.com/events"
IPL_TAG_ID = "101988"

# Timing constants (minutes)
# IPL protocol: toss at gameStartTime - 30, first ball at gameStartTime
# Trigger window: gameStartTime - 20 to gameStartTime - 10
#   = toss + 10 to toss + 20 (info has propagated, still 10+ min before first ball)
TRIGGER_WINDOW_OPEN = 20   # minutes before gameStartTime
TRIGGER_WINDOW_CLOSE = 10  # minutes before gameStartTime
RAIN_DELAY_TIMEOUT_HOURS = 3
RESULT_CHECK_AFTER_HOURS = 3
RESULT_DEADLINE_HOURS = 24

PROP_MARKET_KEYWORDS = [
    "Most Sixes", "Toss Match", "Top Batter", "Top Bowler",
    "Most Fours", "Man of the Match", "Total Runs", "Most Wickets",
    "Highest Opening", "First Wicket",
]

HOME_GROUNDS = {
    "Chennai Super Kings": "MA Chidambaram Stadium",
    "Mumbai Indians": "Wankhede Stadium",
    "Royal Challengers Bengaluru": "M Chinnaswamy Stadium",
    "Royal Challengers Bangalore": "M Chinnaswamy Stadium",
    "Kolkata Knight Riders": "Eden Gardens",
    "Delhi Capitals": "Arun Jaitley Stadium",
    "Rajasthan Royals": "Sawai Mansingh Stadium",
    "Sunrisers Hyderabad": "Rajiv Gandhi International Cricket Stadium",
    "Punjab Kings": "Maharaja Yadavindra Singh International Cricket Stadium",
    "Gujarat Titans": "Narendra Modi Stadium",
    "Lucknow Super Giants": "BRSABV Ekana Cricket Stadium",
}

TEAM_ABBREV = {
    "Chennai Super Kings": "csk",
    "Mumbai Indians": "mi",
    "Royal Challengers Bengaluru": "rcb",
    "Royal Challengers Bangalore": "rcb",
    "Kolkata Knight Riders": "kkr",
    "Delhi Capitals": "dc",
    "Rajasthan Royals": "rr",
    "Sunrisers Hyderabad": "srh",
    "Punjab Kings": "pbks",
    "Gujarat Titans": "gt",
    "Lucknow Super Giants": "lsg",
}


CANONICAL_TEAMS = {
    "Chennai Super Kings", "Mumbai Indians", "Royal Challengers Bengaluru",
    "Kolkata Knight Riders", "Delhi Capitals", "Rajasthan Royals",
    "Sunrisers Hyderabad", "Punjab Kings", "Gujarat Titans", "Lucknow Super Giants",
}


# ---------------------------------------------------------------------------
# PID lock (prevents cron overlap)
# ---------------------------------------------------------------------------

def acquire_lock() -> bool:
    try:
        fd = os.open(str(LOCK_FILE), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.write(fd, str(os.getpid()).encode())
        os.close(fd)
        return True
    except FileExistsError:
        try:
            old_pid = int(LOCK_FILE.read_text().strip())
            os.kill(old_pid, 0)
            return False  # process is still alive
        except (ValueError, ProcessLookupError, PermissionError):
            LOCK_FILE.unlink(missing_ok=True)
            return acquire_lock()


def release_lock():
    LOCK_FILE.unlink(missing_ok=True)


atexit.register(release_lock)
signal.signal(signal.SIGTERM, lambda *_: sys.exit(0))


# ---------------------------------------------------------------------------
# Telegram alerts
# ---------------------------------------------------------------------------

TELEGRAM_ENV = Path.home() / ".claude" / "channels" / "telegram" / ".env"
HEARTBEAT_INTERVAL_HOURS = 6


def _get_chat_id() -> str | None:
    cid = os.environ.get("TELEGRAM_CHAT_ID")
    if cid:
        return cid
    env_file = Path.home() / ".claude" / "channels" / "telegram" / ".env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            if line.startswith("TELEGRAM_CHAT_ID="):
                return line.split("=", 1)[1].strip()
    return None


def _get_bot_token() -> str | None:
    if not TELEGRAM_ENV.exists():
        return None
    for line in TELEGRAM_ENV.read_text().splitlines():
        if line.startswith("TELEGRAM_BOT_TOKEN="):
            return line.split("=", 1)[1].strip()
    return None


def send_telegram(text: str):
    token = _get_bot_token()
    chat_id = _get_chat_id()
    if not token or not chat_id:
        return
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = json.dumps({"chat_id": chat_id, "text": text}).encode()
    req = Request(url, data=payload, headers={"Content-Type": "application/json"})
    try:
        resp = urlopen(req, timeout=10)
        if resp.status != 200:
            log(f"  Telegram send failed: HTTP {resp.status}")
    except Exception as e:
        log(f"  Telegram send failed: {e}")


def maybe_send_heartbeat(state: dict):
    now = datetime.now(timezone.utc)
    last = state.get("last_heartbeat_at")
    if last:
        elapsed = (now - datetime.fromisoformat(last)).total_seconds() / 3600
        if elapsed < HEARTBEAT_INTERVAL_HOURS:
            return

    matches = state.get("matches", {})
    # Build upcoming match list
    upcoming_lines = []
    for ms in sorted(matches.values(), key=lambda m: m.get("game_start_time", "")):
        status = ms.get("status", "")
        t1 = ms.get("team1", "?")
        t2 = ms.get("team2", "?")
        gst_str = ms.get("game_start_time", "")
        if status == "discovered" and gst_str:
            gst = parse_game_time(gst_str)
            trigger_at = gst - timedelta(minutes=15)
            ist = trigger_at + timedelta(hours=5, minutes=30)
            upcoming_lines.append(f"  {t1} vs {t2} - {ist.strftime('%a %b %-d, %-I:%M %p')} IST")
        elif status == "triggered":
            upcoming_lines.append(f"  {t1} vs {t2} - forecast done, waiting for result")
        elif status == "graded":
            winner = ms.get("winner", "?")
            upcoming_lines.append(f"  {t1} vs {t2} - graded ({winner} won)")

    scorecard_path = PROJECT_ROOT / "scorecard.json"
    brier_line = ""
    if scorecard_path.exists():
        try:
            sc = json.loads(scorecard_path.read_text())
            b = sc.get("aggregates", {}).get("mean_brier")
            n = sc.get("aggregates", {}).get("n_matches", 0)
            if b is not None:
                brier_line = f"\nBrier: {b:.3f} across {n} match{'es' if n != 1 else ''} (0.25 = coin flip)"
        except (json.JSONDecodeError, KeyError):
            pass

    match_section = "\n".join(upcoming_lines) if upcoming_lines else "  No matches tracked"
    msg = f"IPL Auto-Pilot is running.\n\nMatches:\n{match_section}{brier_line}"
    send_telegram(msg)
    state["last_heartbeat_at"] = now.isoformat()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def log(msg: str):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"matches": {}}


def save_state(state: dict):
    tmp_fd, tmp_path = tempfile.mkstemp(dir=PROJECT_ROOT, suffix=".tmp")
    try:
        with os.fdopen(tmp_fd, "w") as f:
            json.dump(state, f, indent=2)
        os.replace(tmp_path, STATE_FILE)
    except Exception:
        os.unlink(tmp_path)
        raise


def parse_game_time(s: str) -> datetime:
    s = s.strip()
    # Normalize "+00" to "+00:00" so %z can parse it
    if s.endswith("+00"):
        s = s + ":00"
    elif s.endswith("-00"):
        s = s + ":00"
    for fmt in ["%Y-%m-%d %H:%M:%S%z", "%Y-%m-%dT%H:%M:%S%z",
                "%Y-%m-%dT%H:%M:%SZ"]:
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    try:
        dt = datetime.strptime(s[:19], "%Y-%m-%d %H:%M:%S")
        return dt.replace(tzinfo=timezone.utc)
    except ValueError:
        return datetime.now(timezone.utc) + timedelta(days=365)


TEAM_NORMALIZE = {
    "Royal Challengers Bangalore": "Royal Challengers Bengaluru",
    "Kings XI Punjab": "Punjab Kings",
    "Delhi Daredevils": "Delhi Capitals",
    "Rising Pune Supergiant": "Rising Pune Supergiants",
}


def extract_teams(title: str) -> tuple[str, str] | None:
    if " vs " not in title.lower():
        return None
    match_part = title.split(":", 1)[-1].strip() if ":" in title else title
    parts = [p.strip() for p in match_part.split(" vs ")]
    if len(parts) != 2:
        return None
    t1 = TEAM_NORMALIZE.get(parts[0], parts[0])
    t2 = TEAM_NORMALIZE.get(parts[1], parts[1])
    if t1 not in CANONICAL_TEAMS or t2 not in CANONICAL_TEAMS:
        return None
    return (t1, t2)


def get_venue(team1: str, team2: str) -> str:
    schedule_file = PROJECT_ROOT / "schedule.json"
    if schedule_file.exists():
        try:
            for m in json.loads(schedule_file.read_text()):
                teams = {m.get("team1", ""), m.get("team2", "")}
                if team1 in teams and team2 in teams and m.get("venue"):
                    return m["venue"]
        except (json.JSONDecodeError, KeyError):
            pass
    return HOME_GROUNDS.get(team1, HOME_GROUNDS.get(team2, "Unknown"))


def next_experiment_number() -> int:
    existing = []
    if CASE_STUDIES_DIR.exists():
        for d in CASE_STUDIES_DIR.iterdir():
            if d.is_dir() and d.name.startswith("exp_"):
                try:
                    existing.append(int(d.name.split("_")[1]))
                except (IndexError, ValueError):
                    pass
    return max(existing, default=0) + 1


def make_case_id(team1: str, team2: str, exp_num: int) -> str:
    a1 = TEAM_ABBREV.get(team1, team1[:3].lower())
    a2 = TEAM_ABBREV.get(team2, team2[:3].lower())
    return f"exp_{exp_num:03d}_{a1}_vs_{a2}"


# ---------------------------------------------------------------------------
# Polymarket API
# ---------------------------------------------------------------------------

def _gamma_fetch(params: str) -> list[dict]:
    url = f"{GAMMA_API}?tag_id={IPL_TAG_ID}&{params}&limit=50"
    req = Request(url, headers={"User-Agent": "CricketPricingRoom/1.0"})
    try:
        with urlopen(req, timeout=30) as resp:
            return json.loads(resp.read())
    except (URLError, TimeoutError) as e:
        log(f"API error: {e}")
        return []


def fetch_active_markets() -> list[dict]:
    events = _gamma_fetch("active=true&closed=false")
    markets = []
    for event in events:
        title = event.get("title", "")
        if any(kw in title for kw in PROP_MARKET_KEYWORDS):
            continue
        for mkt in event.get("markets", []):
            if not mkt.get("gameStartTime"):
                continue
            markets.append({
                "event_title": title,
                "market_id": mkt.get("id", ""),
                "condition_id": mkt.get("conditionId", ""),
                "game_start_time": mkt["gameStartTime"],
                "outcomes": mkt.get("outcomes", ""),
                "outcome_prices": mkt.get("outcomePrices", ""),
                "volume": float(mkt.get("volume", "0") or "0"),
                "accepting_orders": mkt.get("acceptingOrders", True),
            })
            break
    return markets


def fetch_resolved_markets() -> list[dict]:
    events = _gamma_fetch("closed=true&order=id&ascending=false")
    markets = []
    for event in events:
        title = event.get("title", "")
        if any(kw in title for kw in PROP_MARKET_KEYWORDS):
            continue
        for mkt in event.get("markets", []):
            markets.append({
                "event_title": title,
                "market_id": mkt.get("id", ""),
                "game_start_time": mkt.get("gameStartTime", ""),
                "outcomes": mkt.get("outcomes", ""),
                "outcome_prices": mkt.get("outcomePrices", ""),
            })
            break
    return markets


def detect_winner(market: dict) -> str | None:
    outcomes = market.get("outcomes", "[]")
    prices = market.get("outcome_prices", "[]")
    if isinstance(outcomes, str):
        outcomes = json.loads(outcomes)
    if isinstance(prices, str):
        prices = json.loads(prices)
    if len(outcomes) != 2 or len(prices) != 2:
        return None
    p0, p1 = float(prices[0]), float(prices[1])
    if p0 > 0.95:
        return outcomes[0]
    if p1 > 0.95:
        return outcomes[1]
    return None


# ---------------------------------------------------------------------------
# Pipeline actions
# ---------------------------------------------------------------------------

def sync_snapshots() -> bool:
    vps_host = os.environ.get("IPL_VPS_HOST")
    if not vps_host:
        log("IPL_VPS_HOST not set — skipping VPS sync")
        return False
    local_dir = PROJECT_ROOT / "market_snapshots"
    local_dir.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        ["rsync", "-avz", f"{vps_host}:/root/ipl_snapshots/data/", str(local_dir) + "/"],
        capture_output=True, text=True, timeout=60,
    )
    if result.returncode == 0:
        log("VPS snapshots synced")
        return True
    log(f"VPS sync failed: {result.stderr[:200]}")
    return False


def trigger_pipeline(team1: str, team2: str, venue: str, date: str,
                     case_id: str, dry_run: bool = False) -> bool:
    log(f"TRIGGER: {team1} vs {team2} at {venue} → {case_id}")
    if dry_run:
        log("  [DRY RUN] would build evidence + invoke agents")
        return True

    sync_snapshots()

    # Build evidence packet
    build_cmd = [
        sys.executable, str(PROJECT_ROOT / "run_pipeline.py"),
        team1, team2, venue, date, "--data-only", "--id", case_id,
    ]
    log(f"  building evidence...")
    r = subprocess.run(build_cmd, capture_output=True, text=True, timeout=300,
                       cwd=str(PROJECT_ROOT))
    if r.returncode != 0:
        log(f"  evidence build FAILED: {r.stderr[:400]}")
        return False
    log("  evidence packet ready")
    send_telegram(f"Pipeline triggered: {team1} vs {team2}. Agents running, expect ~30 min.")

    # Invoke Claude Code agents
    case_dir = CASE_STUDIES_DIR / case_id
    cutoff = datetime.now(timezone.utc).isoformat()
    prompt = (
        f"Run the memo pipeline on {case_dir}. "
        f"Match: {team1} vs {team2}, {date}. "
        f"Evidence cutoff: {cutoff}"
    )
    log("  invoking Claude Code agents...")
    r = subprocess.run(
        ["claude", "-p", prompt],
        capture_output=True, text=True, timeout=1800,
        cwd=str(PROJECT_ROOT),
    )
    if r.returncode != 0:
        log(f"  agent pipeline FAILED (evidence still intact): {r.stderr[:400]}")
        return False

    log("  memo pipeline complete")
    send_telegram(f"Forecast ready: {team1} vs {team2}.\nCheck case_studies/{case_id}/memo.md for the probability band.")
    return True


def grade_match(case_id: str, winner: str, dry_run: bool = False) -> bool:
    log(f"GRADE: {case_id} → winner: {winner}")
    if dry_run:
        log("  [DRY RUN] would score + grade")
        return True

    case_dir = CASE_STUDIES_DIR / case_id

    # Record result
    result_doc = (
        f"# Match Result\n\n"
        f"**Winner:** {winner}\n"
        f"**Recorded at:** {datetime.now(timezone.utc).isoformat()}\n"
        f"**Source:** Polymarket market resolution\n"
    )
    (case_dir / "result.md").write_text(result_doc)

    # Score
    score_cmd = [
        sys.executable, str(PROJECT_ROOT / "run_score.py"),
        str(case_dir), "--winner", winner,
    ]
    log("  scoring...")
    r = subprocess.run(score_cmd, capture_output=True, text=True, timeout=120,
                       cwd=str(PROJECT_ROOT))
    if r.returncode != 0:
        log(f"  scoring FAILED: {r.stderr[:400]}")
        return False

    # Grade via Claude Code
    prompt = (
        f"Grade {case_dir}. Read all files including the memo, result, stats, and market snapshot. "
        f"Write a thorough post-match grade to post_match_grade.md following the same format as "
        f"exp_001_rr_vs_gt/post_match_grade.md. "
        f"Then update reflection/learning_log.md with any new durable rules learned."
    )
    log("  invoking grader...")
    r = subprocess.run(
        ["claude", "-p", prompt],
        capture_output=True, text=True, timeout=1800,
        cwd=str(PROJECT_ROOT),
    )
    if r.returncode != 0:
        log(f"  grading FAILED: {r.stderr[:400]}")
        return False

    log("  grading complete")
    # Read Brier score from scorecard for this match
    brier_info = ""
    try:
        sc = json.loads((PROJECT_ROOT / "scorecard.json").read_text())
        for m in sc.get("matches", []):
            if m.get("case_id") == case_id:
                brier_info = f"\nBrier: {m['brier_score']:.3f} (0.25 = coin flip)"
                break
    except Exception:
        pass
    send_telegram(f"Match graded: {winner} won.\nSee case_studies/{case_id}/post_match_grade.md{brier_info}")
    return True


# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------

def run(dry_run: bool = False):
    now = datetime.now(timezone.utc)
    state = load_state()
    log(f"auto-pilot tick")

    # ── Phase 1: discover + trigger ──────────────────────────────────────
    active = fetch_active_markets()
    for mkt in active:
        teams = extract_teams(mkt["event_title"])
        if not teams:
            continue
        team1, team2 = teams
        gst = parse_game_time(mkt["game_start_time"])
        mins_to_start = (gst - now).total_seconds() / 60

        match_key = f"{mkt['game_start_time'][:10]}_{mkt['market_id']}"
        ms = state["matches"].get(match_key, {})

        if ms.get("status") in ("triggered", "graded", "missed", "trigger_failed"):
            continue

        # Inside trigger window (toss+10 to toss+20)
        if TRIGGER_WINDOW_CLOSE <= mins_to_start <= TRIGGER_WINDOW_OPEN:
            if not mkt["accepting_orders"]:
                log(f"  ABORT {team1} vs {team2}: market closed (match started early)")
                ms["status"] = "missed"
                ms["reason"] = "market closed before trigger window"
                send_telegram(f"MISSED: {team1} vs {team2}. Match started before trigger window fired.")
                state["matches"][match_key] = ms
                save_state(state)
                continue

            date = mkt["game_start_time"][:10]
            venue = get_venue(team1, team2)
            exp_num = ms.get("experiment_number") or next_experiment_number()
            case_id = make_case_id(team1, team2, exp_num)

            ok = trigger_pipeline(team1, team2, venue, date, case_id, dry_run)
            if not dry_run:
                ms.update({
                    "status": "triggered" if ok else "trigger_failed",
                    "team1": team1, "team2": team2,
                    "venue": venue, "date": date,
                    "case_id": case_id,
                    "experiment_number": exp_num,
                    "market_id": mkt["market_id"],
                    "game_start_time": mkt["game_start_time"],
                    "triggered_at": now.isoformat(),
                })
                state["matches"][match_key] = ms
                save_state(state)
                if not ok:
                    send_telegram(f"FAILED: {team1} vs {team2} trigger failed. Evidence may be built but agents didn't run. Check auto_pilot.log.")

        # Past trigger window but match not started yet (rain delay)
        elif mins_to_start < TRIGGER_WINDOW_CLOSE and mkt["accepting_orders"]:
            hours_past = -mins_to_start / 60
            if hours_past > RAIN_DELAY_TIMEOUT_HOURS:
                log(f"  TIMEOUT {team1} vs {team2}: rain delay > {RAIN_DELAY_TIMEOUT_HOURS}h")
                ms["status"] = "missed"
                ms["reason"] = "rain delay timeout"
                send_telegram(f"MISSED: {team1} vs {team2}. Rain delay exceeded {RAIN_DELAY_TIMEOUT_HOURS}h, gave up.")
                state["matches"][match_key] = ms
                save_state(state)
            elif ms.get("status") != "rain_delay":
                log(f"  RAIN DELAY {team1} vs {team2}: past scheduled start, market still open")
                current_prices = mkt.get("outcome_prices", "")
                if isinstance(current_prices, str):
                    try:
                        current_prices = json.loads(current_prices)
                    except json.JSONDecodeError:
                        current_prices = []
                baseline = [str(current_prices[0]), str(current_prices[1])] if len(current_prices) == 2 else []
                ms.update({
                    "status": "rain_delay",
                    "team1": team1, "team2": team2,
                    "game_start_time": mkt["game_start_time"],
                    "market_id": mkt["market_id"],
                    "rain_delay_detected_at": now.isoformat(),
                    "last_prices": baseline,
                })
                state["matches"][match_key] = ms
                save_state(state)
            else:
                # Already tracking rain delay — check for price movement (toss signal)
                stored_prices = ms.get("last_prices")
                current_prices = mkt.get("outcome_prices", "")
                if isinstance(current_prices, str):
                    try:
                        current_prices = json.loads(current_prices)
                    except json.JSONDecodeError:
                        current_prices = []

                if stored_prices and current_prices and len(current_prices) == 2:
                    price_move = abs(float(current_prices[0]) - float(stored_prices[0]))
                    if price_move > 0.04:
                        log(f"  TOSS DETECTED {team1} vs {team2}: price moved {price_move:.2f}")
                        date = mkt["game_start_time"][:10]
                        venue = get_venue(team1, team2)
                        exp_num = ms.get("experiment_number") or next_experiment_number()
                        case_id = make_case_id(team1, team2, exp_num)
                        ok = trigger_pipeline(team1, team2, venue, date, case_id, dry_run)
                        if not dry_run:
                            ms.update({
                                "status": "triggered" if ok else "trigger_failed",
                                "venue": venue, "date": date,
                                "case_id": case_id,
                                "experiment_number": exp_num,
                                "triggered_at": now.isoformat(),
                                "trigger_reason": "rain_delay_toss_detected",
                            })
                            state["matches"][match_key] = ms
                            save_state(state)
                        continue

                if current_prices and len(current_prices) == 2:
                    ms["last_prices"] = [str(current_prices[0]), str(current_prices[1])]
                    state["matches"][match_key] = ms
                    save_state(state)

        # Match started, we never triggered (missed entirely)
        elif mins_to_start < TRIGGER_WINDOW_CLOSE and not mkt["accepting_orders"]:
            if not ms.get("status"):
                log(f"  MISSED {team1} vs {team2}: match already underway")
                ms["status"] = "missed"
                ms["reason"] = "discovered after match start"
                send_telegram(f"MISSED: {team1} vs {team2}. Discovered after match already started.")
                state["matches"][match_key] = ms
                save_state(state)

        # Not yet in window
        else:
            if not ms.get("status"):
                log(f"  DISCOVERED {team1} vs {team2}: starts in {mins_to_start:.0f} min")
                ms.update({
                    "status": "discovered",
                    "team1": team1, "team2": team2,
                    "game_start_time": mkt["game_start_time"],
                    "market_id": mkt["market_id"],
                })
                state["matches"][match_key] = ms
                save_state(state)

    # ── Phase 2: detect results + grade ──────────────────────────────────
    triggered = {k: v for k, v in state["matches"].items()
                 if v.get("status") == "triggered"}

    if triggered:
        resolved = {m["market_id"]: m for m in fetch_resolved_markets()}
        for match_key, ms in triggered.items():
            gst = parse_game_time(ms["game_start_time"])
            hours_since = (now - gst).total_seconds() / 3600

            if hours_since < RESULT_CHECK_AFTER_HOURS:
                continue
            if hours_since > RESULT_DEADLINE_HOURS:
                log(f"  RESULT TIMEOUT: {ms['case_id']}")
                ms["status"] = "result_timeout"
                send_telegram(f"PROBLEM: {ms.get('team1','?')} vs {ms.get('team2','?')} - no result detected after 24h. Polymarket may not have resolved. Check manually.")
                state["matches"][match_key] = ms
                save_state(state)
                continue

            rmkt = resolved.get(ms["market_id"])
            if rmkt:
                winner = detect_winner(rmkt)
                if winner:
                    ok = grade_match(ms["case_id"], winner, dry_run)
                    if not dry_run:
                        ms.update({
                            "status": "graded" if ok else "grade_failed",
                            "winner": winner,
                            "graded_at": now.isoformat(),
                        })
                        if not ok:
                            send_telegram(f"FAILED: {ms.get('team1','?')} vs {ms.get('team2','?')} grading failed. Winner: {winner}. Check auto_pilot.log.")
                        state["matches"][match_key] = ms
                        save_state(state)

    # ── Phase 3: consolidation check ─────────────────────────────────────
    graded_count = sum(1 for v in state["matches"].values() if v.get("status") == "graded")
    last_consol = state.get("last_consolidation_count", 0)
    if graded_count >= last_consol + 3:
        log(f"CONSOLIDATION: {graded_count} graded (last ran at {last_consol})")
        if not dry_run:
            r = subprocess.run(
                [sys.executable, str(PROJECT_ROOT / "run_consolidate.py")],
                capture_output=True, text=True, timeout=300,
                cwd=str(PROJECT_ROOT),
            )
            if r.returncode == 0:
                state["last_consolidation_count"] = graded_count
                log("  consolidation complete")
                send_telegram(f"Consolidation ran after {graded_count} matches. Reflection Log rules updated.\nSee reflection/learning_log.md and reflection/experiments.md")
            else:
                log(f"  consolidation FAILED: {r.stderr[:300]}")

    maybe_send_heartbeat(state)
    save_state(state)
    log("tick complete")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def install_cron():
    python = sys.executable
    script = Path(__file__).resolve()
    cron_line = f"*/5 * * * * cd {PROJECT_ROOT} && {python} {script} >> {LOG_FILE} 2>&1"
    marker = "# cricket-auto-pilot"

    result = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
    existing = result.stdout if result.returncode == 0 else ""

    if marker in existing:
        print("Auto-pilot cron already installed:")
        for line in existing.splitlines():
            if marker in line or "auto_pilot" in line:
                print(f"  {line}")
        return

    new_crontab = existing.rstrip() + f"\n{cron_line} {marker}\n"
    proc = subprocess.run(["crontab", "-"], input=new_crontab, capture_output=True, text=True)
    if proc.returncode == 0:
        print(f"Cron installed (every 5 min)")
        print(f"  Log: {LOG_FILE}")
        print(f"  State: {STATE_FILE}")
    else:
        print(f"Failed: {proc.stderr}")


def show_status():
    state = load_state()
    matches = state.get("matches", {})

    print(f"State file: {STATE_FILE}")
    print(f"Matches tracked: {len(matches)}\n")

    by_status = {}
    for ms in matches.values():
        s = ms.get("status", "?")
        by_status.setdefault(s, []).append(ms)

    for status in ["discovered", "rain_delay", "triggered", "graded", "missed",
                    "trigger_failed", "grade_failed", "result_timeout"]:
        group = by_status.get(status, [])
        if not group:
            continue
        print(f"  {status.upper()} ({len(group)}):")
        for ms in group:
            t1 = ms.get("team1", "?")
            t2 = ms.get("team2", "?")
            cid = ms.get("case_id", "")
            extra = f" → {ms['winner']}" if ms.get("winner") else ""
            print(f"    {t1} vs {t2}  {cid}{extra}")
    print()

    result = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
    if "auto_pilot" in result.stdout:
        print("Cron: INSTALLED")
    else:
        print("Cron: NOT INSTALLED (run --install)")


if __name__ == "__main__":
    if "--install" in sys.argv:
        install_cron()
    elif "--status" in sys.argv:
        show_status()
    elif "--dry-run" in sys.argv:
        run(dry_run=True)
    else:
        if not acquire_lock():
            print("Another auto_pilot instance is running. Exiting.")
            sys.exit(0)
        run()
