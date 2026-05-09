#!/usr/bin/env python3
"""
Cricket Pricing Room — Orchestrator

Builds a frozen evidence packet and runs all agents in sequence to produce
a pre-match probability-band memo.

Usage:
    python3 run_memo.py "Rajasthan Royals" "Gujarat Titans" "Sawai Mansingh Stadium" 2026-05-10

    # With custom case study ID:
    python3 run_memo.py "CSK" "MI" "Wankhede Stadium" 2026-05-12 --id match_003_csk_vs_mi

    # Retrospective (with manual evidence cutoff):
    python3 run_memo.py "RR" "GT" "Sawai Mansingh Stadium" 2026-04-15 --cutoff "2026-04-15T13:30:00Z"

After running, open the case study in Claude Code and invoke agents:
    1. Market Reader + Stats Analyst run automatically (data layer)
    2. Ask Claude Code to run News & Conditions Analyst (needs web search)
    3. Ask Claude Code to run Source Quality Clerk (reads news output)
    4. Ask Claude Code to run Base-Rate Skeptic (reads all upstream)
    5. Ask Claude Code to run Fair Value Synthesizer (produces memo)
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "tools"))
from cricsheet.query import CricsheetDB, normalize_team
from polymarket.fetch import get_market_snapshot

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


def build_evidence_packet(
    case_id: str,
    team1: str,
    team2: str,
    venue: str,
    date: str,
    evidence_cutoff: str,
) -> Path:
    case_dir = CASE_STUDIES_DIR / case_id
    case_dir.mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc).isoformat()

    # Evidence cutoff
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

    # Stats snapshot
    print("Loading Cricsheet data...")
    db = CricsheetDB()
    print(f"  {len(db.matches)} matches loaded ({db.matches[0].date} to {db.matches[-1].date})")

    print(f"Building stats snapshot (cutoff: {date})...")
    stats = db.full_stats(team1, team2, venue, date)
    (case_dir / "stats_snapshot.json").write_text(json.dumps(stats, indent=2))

    h2h = stats["head_to_head"]["overall"]
    print(f"  H2H: {h2h['team1']} {h2h['team1_wins']}-{h2h['team2_wins']} {h2h['team2']}")
    vs = stats["venue_splits"]
    if vs["matches_analyzed"] > 0:
        print(f"  Venue: {vs['bat_first_wins']}/{vs['chase_wins']} (bat/chase) from {vs['matches_analyzed']} matches")
    else:
        print(f"  Venue: no matches found at {venue}")

    # Market snapshot
    print("Fetching market snapshot...")
    market = get_market_snapshot(team1, team2, venue, date, str(case_dir))
    (case_dir / "market_snapshot.json").write_text(json.dumps(market, indent=2))

    t1p = market["team1"].get("implied_probability")
    t2p = market["team2"].get("implied_probability")
    if t1p is not None:
        print(f"  {team1}: {t1p*100:.1f}% | {team2}: {t2p*100:.1f}%")
        print(f"  Volume: ${market.get('volume_usd', 0):,.0f} ({market.get('liquidity_flag', '?')})")
    else:
        print("  No live market found — check manual_snapshot.json")

    # Placeholder files
    for fname, title in [
        ("news_conditions.md", "News & Conditions"),
        ("source_quality.md", "Source Quality Assessment"),
        ("skeptic_review.md", "Skeptic Review"),
        ("allowed_sources.md", "Allowed Sources"),
        ("memo.md", "Memo"),
        ("result.md", "Result"),
        ("post_match_grade.md", "Post-Match Grade"),
    ]:
        fpath = case_dir / fname
        if not fpath.exists():
            fpath.write_text(f"# {title}\n\n_Pending._\n")

    return case_dir


def print_next_steps(case_dir: Path, team1: str, team2: str):
    print(f"""
{'='*60}
Evidence packet ready: {case_dir}
{'='*60}

Next steps — run these in Claude Code:

  1. "Run News & Conditions Analyst for {team1} vs {team2}.
     Read the evidence cutoff at {case_dir}/evidence_cutoff.md.
     Write output to {case_dir}/news_conditions.md."

  2. "Run Source Quality Clerk on {case_dir}/news_conditions.md.
     Write output to {case_dir}/source_quality.md."

  3. "Run Base-Rate Skeptic. Read:
     - {case_dir}/stats_snapshot.json
     - {case_dir}/market_snapshot.json
     - {case_dir}/news_conditions.md
     - {case_dir}/source_quality.md
     - reflection/learning_log.md
     Write output to {case_dir}/skeptic_review.md."

  4. "Run Fair Value Synthesizer. Read all files in {case_dir}/.
     Read reflection/learning_log.md.
     Write the memo to {case_dir}/memo.md."

After the match:

  5. "Fill in {case_dir}/result.md with the match result."

  6. "Run Post-Match Grader on {case_dir}/.
     Write grade to {case_dir}/post_match_grade.md."

  7. "Update reflection/learning_log.md with lessons from the grade."
""")


def main():
    parser = argparse.ArgumentParser(description="Build evidence packet for a case study")
    parser.add_argument("team1", help="Team 1 name or abbreviation (e.g., RR, CSK)")
    parser.add_argument("team2", help="Team 2 name or abbreviation")
    parser.add_argument("venue", help="Venue name")
    parser.add_argument("date", help="Match date (YYYY-MM-DD)")
    parser.add_argument("--id", help="Custom case study ID")
    parser.add_argument("--cutoff", help="Evidence cutoff (ISO8601). Defaults to now.")
    args = parser.parse_args()

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
    print_next_steps(case_dir, team1, team2)


if __name__ == "__main__":
    main()
