"""
Evidence packet builder.

Creates and populates the frozen evidence directory for a case study.
Enforces the discipline: all evidence is timestamped and frozen at the
evidence cutoff (pre-toss). The resulting packet makes "no hindsight"
demonstrable and verifiable.
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
CASE_STUDIES_DIR = PROJECT_ROOT / "case_studies"

# Add parent to path for imports
import sys
sys.path.insert(0, str(PROJECT_ROOT / "tools"))
from cricsheet.query import CricsheetDB
from polymarket.fetch import get_market_snapshot


def create_case_study(
    match_id: str,
    team1: str,
    team2: str,
    venue: str,
    date: str,
    evidence_cutoff: str,
    toss_time: str = None,
) -> Path:
    """
    Create a new case study directory and populate it with frozen evidence.

    Args:
        match_id: identifier like "match_001"
        team1, team2: team names
        venue: ground name
        date: match date YYYY-MM-DD
        evidence_cutoff: ISO8601 timestamp — nothing after this is admissible
        toss_time: optional ISO8601 toss time (defaults to evidence_cutoff)
    """
    case_dir = CASE_STUDIES_DIR / match_id
    case_dir.mkdir(parents=True, exist_ok=True)

    if toss_time is None:
        toss_time = evidence_cutoff

    # 1. Evidence cutoff document
    cutoff_doc = f"""# Evidence Cutoff

**Match:** {team1} vs {team2}
**Venue:** {venue}
**Date:** {date}
**Evidence cutoff:** {evidence_cutoff}
**Toss time:** {toss_time}

## Rules

All evidence used by agents in this case study must be sourced from
before the evidence cutoff timestamp above. Any source without a clear
publication date must be flagged by the Source Quality Clerk.

This packet was built at: {datetime.now(timezone.utc).isoformat()}
"""
    (case_dir / "evidence_cutoff.md").write_text(cutoff_doc)

    # 2. Stats snapshot from Cricsheet
    print(f"Building stats snapshot (cutoff: {date})...")
    db = CricsheetDB()
    stats = db.full_stats(team1, team2, venue, date)
    (case_dir / "stats_snapshot.json").write_text(json.dumps(stats, indent=2))

    # 3. Market snapshot from Polymarket (or manual fallback)
    print("Fetching market snapshot...")
    market = get_market_snapshot(team1, team2, venue, date, str(case_dir))
    (case_dir / "market_snapshot.json").write_text(json.dumps(market, indent=2))

    # 4. Allowed sources placeholder (to be filled by News Analyst run)
    allowed_sources_doc = f"""# Allowed Sources

**Evidence cutoff:** {evidence_cutoff}

Sources used by the News & Conditions Analyst for this case study.
Each entry includes URL, title, publication date, and access timestamp.

## Sources

_To be populated during agent run._
"""
    if not (case_dir / "allowed_sources.md").exists():
        (case_dir / "allowed_sources.md").write_text(allowed_sources_doc)

    # 5. Placeholder files for agent outputs
    for fname in ["memo.md", "result.md", "post_match_grade.md"]:
        fpath = case_dir / fname
        if not fpath.exists():
            fpath.write_text(f"# {fname.replace('.md','').replace('_',' ').title()}\n\n_Pending._\n")

    print(f"Case study created: {case_dir}")
    return case_dir


def freeze_manual_snapshot(case_dir: str, team1: str, team2: str, prob1: float, prob2: float, source_note: str):
    """Write a manual_snapshot.json for cases where Polymarket data isn't available."""
    snapshot = {
        "source": "manual_snapshot",
        "team1": {"name": team1, "implied_probability": prob1},
        "team2": {"name": team2, "implied_probability": prob2},
        "volume_usd": None,
        "bid_ask_spread_pct": None,
        "liquidity_flag": None,
        "notes": source_note,
        "frozen_at": datetime.now(timezone.utc).isoformat(),
    }
    path = Path(case_dir) / "manual_snapshot.json"
    path.write_text(json.dumps(snapshot, indent=2))
    print(f"Manual snapshot written: {path}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # Build a test case study for the upcoming RR vs GT match
        case_dir = create_case_study(
            match_id="match_001_rr_vs_gt",
            team1="Rajasthan Royals",
            team2="Gujarat Titans",
            venue="Sawai Mansingh Stadium",
            date="2026-05-10",
            evidence_cutoff="2026-05-10T14:00:00+05:30",
            toss_time="2026-05-10T19:00:00+05:30",
        )
        print(f"\nContents:")
        for f in sorted(case_dir.iterdir()):
            size = f.stat().st_size
            print(f"  {f.name} ({size} bytes)")
    else:
        print("Usage: python build.py test")
        print("       Creates a test case study for RR vs GT")
