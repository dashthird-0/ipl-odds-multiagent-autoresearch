#!/usr/bin/env python3
"""
Cricket Pricing Room — Full Pipeline Runner

Builds the evidence packet (data layer) and then invokes Claude Code
subagents in sequence via the Agent tool to produce a complete pre-match memo.

This script handles Phase 0 (mechanical data collection via Python).
Phases 1-4 (reasoning agents) are invoked by Claude Code's Agent tool
when the user runs: "Run the pipeline on case_studies/{case_id}"

Usage:
    # Build evidence + run full pipeline:
    python3 run_pipeline.py RR GT "Sawai Mansingh Stadium" 2026-05-10

    # Just build evidence (no agent invocation):
    python3 run_pipeline.py RR GT "Sawai Mansingh Stadium" 2026-05-10 --data-only

    # Run agents on existing case study:
    python3 run_pipeline.py --case case_studies/match_001_rr_vs_gt

    # Post-match grading:
    python3 run_pipeline.py --grade case_studies/match_001_rr_vs_gt --winner "Gujarat Titans" --by "6 wickets"
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "tools"))

PROJECT_ROOT = Path(__file__).parent
CASE_STUDIES_DIR = PROJECT_ROOT / "case_studies"

TEAM_SHORT = {
    "RR": "Rajasthan Royals",
    "GT": "Gujarat Titans",
    "CSK": "Chennai Super Kings",
    "MI": "Mumbai Indians",
    "RCB": "Royal Challengers Bengaluru",
    "DC": "Delhi Capitals",
    "SRH": "Sunrisers Hyderabad",
    "KKR": "Kolkata Knight Riders",
    "LSG": "Lucknow Super Giants",
    "PBKS": "Punjab Kings",
}


def resolve_team(name: str) -> str:
    return TEAM_SHORT.get(name.upper(), name)


def make_case_id(team1: str, team2: str, date: str) -> str:
    t1 = team1.split()[-1].lower()[:4]
    t2 = team2.split()[-1].lower()[:4]
    d = date.replace("-", "")
    return f"match_{d}_{t1}_vs_{t2}"


def find_pretoss_snapshot(team1: str, team2: str, date: str) -> dict | None:
    """Find the last pre-toss VPS snapshot for this match."""
    from datetime import datetime, timezone

    snapshots_dir = PROJECT_ROOT / "market_snapshots"
    if not snapshots_dir.exists():
        return None

    date_prefix = date.replace("-", "")
    candidates = []
    for f in snapshots_dir.glob(f"{date_prefix}_*.json"):
        try:
            data = json.loads(f.read_text())
            title = data.get("event_title", "").lower()
            t1_last = team1.split()[-1].lower()
            t2_last = team2.split()[-1].lower()
            if t1_last in title and t2_last in title:
                captured_at = data.get("captured_at", "")
                game_start = data.get("game_start_time", "")
                if game_start and captured_at:
                    try:
                        cap_dt = datetime.fromisoformat(captured_at)
                        gs_raw = game_start.strip()
                        if gs_raw.endswith("+00"):
                            gs_raw = gs_raw + ":00"
                        gs_dt = datetime.fromisoformat(gs_raw.replace(" ", "T"))
                        if cap_dt >= gs_dt:
                            continue
                    except ValueError:
                        pass
                candidates.append((captured_at, data))
        except (json.JSONDecodeError, KeyError):
            continue

    if not candidates:
        return None

    candidates.sort(key=lambda x: x[0])
    _, snapshot = candidates[-1]
    return snapshot


def snapshot_to_market(snapshot: dict, team1: str, team2: str, venue: str, date: str) -> dict:
    """Convert a VPS snapshot to the market_snapshot.json format."""
    outcomes = json.loads(snapshot.get("outcomes", "[]")) if isinstance(snapshot.get("outcomes"), str) else snapshot.get("outcomes", [])
    prices = json.loads(snapshot.get("outcome_prices", "[]")) if isinstance(snapshot.get("outcome_prices"), str) else snapshot.get("outcome_prices", [])

    t1_prob, t2_prob = None, None
    if len(outcomes) == 2 and len(prices) == 2:
        for i, outcome in enumerate(outcomes):
            price = float(prices[i])
            if team1.split()[-1].lower() in outcome.lower() or team1.split()[0].lower() in outcome.lower():
                t1_prob = price
            elif team2.split()[-1].lower() in outcome.lower() or team2.split()[0].lower() in outcome.lower():
                t2_prob = price

    if t1_prob is None and t2_prob is None and len(prices) == 2:
        t1_prob = float(prices[0])
        t2_prob = float(prices[1])

    volume = snapshot.get("volume", 0)
    if volume > 50000:
        liquidity = "deep"
    elif volume > 10000:
        liquidity = "moderate"
    else:
        liquidity = "thin"

    return {
        "match": f"{team1} vs {team2}",
        "venue": venue,
        "date": date,
        "snapshot_timestamp": snapshot.get("captured_at", ""),
        "source": "polymarket_vps_archive",
        "market_id": snapshot.get("market_id", ""),
        "condition_id": snapshot.get("condition_id", ""),
        "team1": {"name": team1, "implied_probability": t1_prob},
        "team2": {"name": team2, "implied_probability": t2_prob},
        "volume_usd": volume,
        "liquidity_flag": liquidity,
    }


def build_evidence_packet(case_id, team1, team2, venue, date, evidence_cutoff):
    from cricsheet.query import CricsheetDB
    from polymarket.fetch import get_market_snapshot

    case_dir = CASE_STUDIES_DIR / case_id
    case_dir.mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc).isoformat()

    (case_dir / "evidence_cutoff.md").write_text(
        f"""# Evidence Cutoff

**Match:** {team1} vs {team2}
**Venue:** {venue}
**Date:** {date}
**Evidence cutoff:** {evidence_cutoff}

All evidence used by agents must be sourced before the evidence cutoff.
Packet built at: {now}
"""
    )

    print("Loading Cricsheet data...")
    db = CricsheetDB()
    print(f"  {len(db.matches)} matches loaded")

    print(f"Building stats snapshot (cutoff: {date})...")
    stats = db.full_stats(team1, team2, venue, date)
    (case_dir / "stats_snapshot.json").write_text(json.dumps(stats, indent=2))

    h2h = stats["head_to_head"]["overall"]
    print(f"  H2H: {h2h['team1']} {h2h['team1_wins']}-{h2h['team2_wins']} {h2h['team2']}")

    # Try VPS archived snapshot first, fall back to live API
    print("Looking for pre-toss VPS snapshot...")
    vps_snapshot = find_pretoss_snapshot(team1, team2, date)
    if vps_snapshot:
        market = snapshot_to_market(vps_snapshot, team1, team2, venue, date)
        print(f"  Using archived snapshot from {market['snapshot_timestamp'][:19]}")
    else:
        print("  No archived snapshot found, fetching live...")
        market = get_market_snapshot(team1, team2, venue, date, str(case_dir))

    (case_dir / "market_snapshot.json").write_text(json.dumps(market, indent=2))

    t1p = market["team1"].get("implied_probability")
    t2p = market["team2"].get("implied_probability")
    if t1p is not None and t2p is not None:
        print(f"  {team1}: {t1p*100:.1f}% | {team2}: {t2p*100:.1f}%")
        print(f"  Volume: ${market.get('volume_usd', 0):,.0f} ({market.get('liquidity_flag', '?')})")
    else:
        print("  No market data found (will use live fetch during agent run)")

    for fname in ["news_conditions.md", "source_quality.md", "skeptic_review.md",
                  "memo.md", "result.md", "post_match_grade.md"]:
        fpath = case_dir / fname
        if not fpath.exists():
            fpath.write_text(f"# {fname.replace('.md','').replace('_',' ').title()}\n\n_Pending._\n")

    return case_dir


def print_agent_invocation(case_dir: Path, team1: str, team2: str, date: str, cutoff: str):
    print(f"""
{'='*60}
Evidence packet ready: {case_dir}
{'='*60}

To run the full agent pipeline, tell Claude Code:

  "Run the memo pipeline on {case_dir}.
   Match: {team1} vs {team2}, {date}.
   Evidence cutoff: {cutoff}"

Claude Code will invoke these agents via the Agent tool:
  1. News & Conditions Analyst (sonnet) → news_conditions.md
  2. Source Quality Clerk (opus) → source_quality.md
  3. Base-Rate Skeptic (opus) → skeptic_review.md
  4. Fair Value Synthesizer (opus) → memo.md

Stats and market data are already frozen in the evidence packet.
""")


VPS_HOST = os.environ.get("IPL_VPS_HOST", "root@YOUR_VPS_IP")
VPS_SNAPSHOTS = "/root/ipl_snapshots/data/"


def sync_snapshots():
    """Pull latest snapshots from VPS."""
    import subprocess
    local_dir = PROJECT_ROOT / "market_snapshots"
    local_dir.mkdir(parents=True, exist_ok=True)
    cmd = ["rsync", "-avz", f"{VPS_HOST}:{VPS_SNAPSHOTS}", str(local_dir) + "/"]
    print(f"Syncing from {VPS_HOST}...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        snapshots = list(local_dir.glob("*.json"))
        print(f"  {len(snapshots)} snapshots synced to {local_dir}/")
    else:
        print(f"  Sync failed: {result.stderr}")
    return result.returncode == 0


def main():
    parser = argparse.ArgumentParser(description="Cricket Pricing Room pipeline")
    parser.add_argument("team1", nargs="?", help="Team 1 name or abbreviation")
    parser.add_argument("team2", nargs="?", help="Team 2 name or abbreviation")
    parser.add_argument("venue", nargs="?", help="Venue name")
    parser.add_argument("date", nargs="?", help="Match date (YYYY-MM-DD)")
    parser.add_argument("--id", help="Custom case study ID")
    parser.add_argument("--cutoff", help="Evidence cutoff (ISO8601). Defaults to now.")
    parser.add_argument("--data-only", action="store_true", help="Only build evidence packet")
    parser.add_argument("--case", help="Run agents on existing case study directory")
    parser.add_argument("--grade", help="Run post-match grading on case study directory")
    parser.add_argument("--winner", help="Match winner (for grading)")
    parser.add_argument("--by", help="Win margin (for grading)")
    parser.add_argument("--sync", action="store_true", help="Sync snapshots from VPS before building")
    args = parser.parse_args()

    if args.grade:
        case_dir = Path(args.grade)
        if not case_dir.exists():
            print(f"Error: {case_dir} does not exist")
            sys.exit(1)
        if args.winner and args.by:
            result_doc = f"""# Match Result

**Winner:** {args.winner}
**Margin:** {args.by}
**Recorded at:** {datetime.now(timezone.utc).isoformat()}
"""
            (case_dir / "result.md").write_text(result_doc)
            print(f"Result recorded: {args.winner} won by {args.by}")
        print(f"\nTo run the grader, tell Claude Code:")
        print(f'  "Grade {case_dir}. Read all files, write to post_match_grade.md, then update reflection/learning_log.md."')
        return

    if args.case:
        case_dir = Path(args.case)
        if not case_dir.exists():
            print(f"Error: {case_dir} does not exist")
            sys.exit(1)
        cutoff_file = case_dir / "evidence_cutoff.md"
        print(f"Case study: {case_dir}")
        print(f"\nTo run agents, tell Claude Code:")
        print(f'  "Run the memo pipeline on {case_dir}"')
        return

    if args.sync:
        sync_snapshots()
        if not args.team1:
            return

    if not all([args.team1, args.team2, args.venue, args.date]):
        parser.print_help()
        sys.exit(1)

    team1 = resolve_team(args.team1)
    team2 = resolve_team(args.team2)
    cutoff = args.cutoff or datetime.now(timezone.utc).isoformat()
    case_id = args.id or make_case_id(team1, team2, args.date)

    print(f"\n  Cricket Pricing Room")
    print(f"  {team1} vs {team2}")
    print(f"  {args.venue} | {args.date}")
    print(f"  Evidence cutoff: {cutoff}")
    print(f"  Case ID: {case_id}\n")

    case_dir = build_evidence_packet(case_id, team1, team2, args.venue, args.date, cutoff)

    if args.data_only:
        print(f"\nEvidence packet built: {case_dir}")
        print("Run with --case to invoke agents.")
    else:
        print_agent_invocation(case_dir, team1, team2, args.date, cutoff)


if __name__ == "__main__":
    main()
