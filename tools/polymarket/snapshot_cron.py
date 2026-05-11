#!/usr/bin/env python3
"""
Polymarket IPL snapshot cron job.

Runs every 30 minutes. If any IPL match-winner market has gameStartTime
within the next 8 hours, captures a timestamped snapshot.

Multiple snapshots per match provide redundancy. The pipeline uses the
last snapshot captured before toss as the official market anchor.

Usage:
    # Run once (for testing):
    python3 tools/polymarket/snapshot_cron.py

    # Install cron (runs every 30 min):
    python3 tools/polymarket/snapshot_cron.py --install

    # Check status:
    python3 tools/polymarket/snapshot_cron.py --status
"""

import json
import os
import subprocess
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError

PROJECT_ROOT = Path(__file__).parent.parent.parent
SNAPSHOTS_DIR = PROJECT_ROOT / "market_snapshots"
LOG_FILE = SNAPSHOTS_DIR / "capture_log.jsonl"

GAMMA_API = "https://gamma-api.polymarket.com/events"
IPL_TAG_ID = "101988"
LOOKAHEAD_HOURS = 8


def fetch_active_ipl_markets() -> list[dict]:
    url = f"{GAMMA_API}?tag_id={IPL_TAG_ID}&active=true&closed=false&limit=50&order=id&ascending=false"
    req = Request(url, headers={"User-Agent": "CricketPricingRoom/1.0"})
    try:
        with urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
    except (URLError, TimeoutError) as e:
        log_event("fetch_error", {"error": str(e)})
        return []

    matches = []
    for event in data:
        event_title = event.get("title", "")
        if any(x in event_title for x in ["Most Sixes", "Toss Match", "Top Batter", "Top Bowler"]):
            continue
        for market in event.get("markets", []):
            volume = float(market.get("volume", "0") or "0")
            game_start = market.get("gameStartTime", "")
            if not game_start:
                continue
            matches.append({
                "event_title": event.get("title", ""),
                "market_id": market.get("id", ""),
                "condition_id": market.get("conditionId", ""),
                "clob_token_ids": market.get("clobTokenIds", ""),
                "game_start_time": game_start,
                "outcomes": market.get("outcomes", ""),
                "outcome_prices": market.get("outcomePrices", ""),
                "volume": volume,
                "last_trade_price": market.get("lastTradePrice", ""),
                "best_bid": market.get("bestBid", ""),
                "best_ask": market.get("bestAsk", ""),
                "spread": market.get("spread", ""),
            })
            break
    return matches


def parse_game_time(game_start_str: str) -> datetime:
    s = game_start_str.strip()
    if s.endswith("+00"):
        s = s + ":00"
    for fmt in ["%Y-%m-%d %H:%M:%S%z", "%Y-%m-%dT%H:%M:%S%z"]:
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    try:
        dt = datetime.strptime(s[:19], "%Y-%m-%d %H:%M:%S")
        return dt.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def should_capture(game_start_str: str) -> bool:
    now = datetime.now(timezone.utc)
    game_time = parse_game_time(game_start_str)
    if not game_time:
        return False
    hours_until = (game_time - now).total_seconds() / 3600
    return -4 < hours_until < LOOKAHEAD_HOURS


def save_snapshot(market: dict) -> Path:
    SNAPSHOTS_DIR.mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc)
    timestamp = now.strftime("%Y%m%dT%H%M%SZ")
    game_date = market["game_start_time"][:10].replace("-", "")

    title = market["event_title"]
    # Extract team names from title like "Indian Premier League: Team A vs Team B"
    match_part = title.split(":", 1)[-1].strip() if ":" in title else title
    slug = match_part.lower().replace(" vs ", "_vs_").replace(" ", "_")[:40]

    filename = f"{game_date}_{slug}_{timestamp}.json"
    filepath = SNAPSHOTS_DIR / filename

    snapshot = {
        "captured_at": now.isoformat(),
        "game_start_time": market["game_start_time"],
        **market,
    }

    filepath.write_text(json.dumps(snapshot, indent=2))
    return filepath


def log_event(event_type: str, data: dict):
    SNAPSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event": event_type,
        **data,
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")


def run_capture():
    markets = fetch_active_ipl_markets()
    if not markets:
        log_event("no_markets", {"note": "No active IPL match markets found"})
        return []

    captured = []
    for market in markets:
        if should_capture(market["game_start_time"]):
            filepath = save_snapshot(market)
            captured.append(filepath)
            log_event("captured", {
                "file": str(filepath.name),
                "title": market["event_title"],
                "game_start": market["game_start_time"],
                "prices": market["outcome_prices"],
                "volume": market["volume"],
            })
            print(f"Captured: {filepath.name}")
            print(f"  {market['event_title']}")
            print(f"  Prices: {market['outcome_prices']}, Vol: ${market['volume']:,.0f}")
        else:
            gt = parse_game_time(market["game_start_time"])
            if gt:
                hours = (gt - datetime.now(timezone.utc)).total_seconds() / 3600
                print(f"Skipped (starts in {hours:.1f}h): {market['event_title'][:50]}")
            else:
                print(f"Skipped (bad game time): {market['event_title'][:50]}")

    if not captured:
        log_event("no_capture", {"note": "No matches within capture window", "markets_found": len(markets)})
        print("No matches within 8-hour capture window.")

    return captured


def get_cron_line() -> str:
    python = sys.executable
    script = Path(__file__).resolve()
    return f"*/30 * * * * {python} {script} >> {SNAPSHOTS_DIR}/cron_stdout.log 2>&1"


def install_cron():
    cron_line = get_cron_line()
    marker = "# cricket-pricing-room-snapshot"

    result = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
    existing = result.stdout if result.returncode == 0 else ""

    if marker in existing:
        print("Cron job already installed. Current entry:")
        for line in existing.splitlines():
            if marker in line or "snapshot_cron" in line:
                print(f"  {line}")
        return

    new_crontab = existing.rstrip() + f"\n{cron_line} {marker}\n"
    proc = subprocess.run(["crontab", "-"], input=new_crontab, capture_output=True, text=True)
    if proc.returncode == 0:
        print(f"Cron installed: {cron_line}")
        print(f"Snapshots will be saved to: {SNAPSHOTS_DIR}/")
        print(f"Log: {LOG_FILE}")
    else:
        print(f"Failed to install cron: {proc.stderr}")


def show_status():
    print(f"Snapshots dir: {SNAPSHOTS_DIR}")
    if not SNAPSHOTS_DIR.exists():
        print("  (not yet created — no captures yet)")
        return

    snapshots = sorted(SNAPSHOTS_DIR.glob("*.json"))
    print(f"  Snapshots captured: {len(snapshots)}")
    if snapshots:
        print(f"  Latest: {snapshots[-1].name}")

    if LOG_FILE.exists():
        lines = LOG_FILE.read_text().strip().splitlines()
        print(f"  Log entries: {len(lines)}")
        if lines:
            last = json.loads(lines[-1])
            print(f"  Last event: {last.get('event')} at {last.get('timestamp','')[:19]}")

    # Check cron
    result = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
    if "snapshot_cron" in result.stdout:
        print("  Cron: INSTALLED")
    else:
        print("  Cron: NOT INSTALLED (run with --install)")


if __name__ == "__main__":
    if "--install" in sys.argv:
        install_cron()
    elif "--status" in sys.argv:
        show_status()
    else:
        captured = run_capture()
        if not captured:
            print("\nTo install cron (every 30 min): python3 tools/polymarket/snapshot_cron.py --install")
