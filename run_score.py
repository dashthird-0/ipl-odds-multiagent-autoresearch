#!/usr/bin/env python3
"""
Cricket Pricing Room — Score a completed match

Reads the memo's prediction, computes Brier score, updates scorecard.

Usage:
    python3 run_score.py case_studies/match_001_rr_vs_gt --winner "Gujarat Titans"

    # With explicit prediction override (if memo parsing fails):
    python3 run_score.py case_studies/match_001_rr_vs_gt --winner "Gujarat Titans" --prediction 0.52 --band 0.48,0.56
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "tools"))
from scoring.brier import alphabetical_reference_team, compute_match_score, update_scorecard

PROJECT_ROOT = Path(__file__).parent
SCORECARD_PATH = PROJECT_ROOT / "scorecard.json"


def extract_teams_from_case(case_dir: Path) -> tuple[str, str]:
    """Extract team names from evidence_cutoff.md."""
    cutoff = (case_dir / "evidence_cutoff.md").read_text()
    match = re.search(r"\*\*Match:\*\*\s*(.+?)\s+vs\s+(.+)", cutoff)
    if match:
        return match.group(1).strip(), match.group(2).strip()
    raise ValueError(f"Could not extract teams from {case_dir}/evidence_cutoff.md")


def extract_prediction_from_memo(case_dir: Path, ref_team: str, team1: str, team2: str) -> tuple[float, tuple[float, float]]:
    """Parse the memo to extract prediction and band for the reference team."""
    memo = (case_dir / "memo.md").read_text()

    band_match = re.search(
        r"\*{0,2}[Mm]odel [Bb]and:?\*{0,2}\s*(\d+)\s*[\-–—]\s*(\d+)\s*%\s*\(([^)]+)\)",
        memo,
    )
    if not band_match:
        raise ValueError("Could not parse model band from memo")

    band_low = int(band_match.group(1)) / 100
    band_high = int(band_match.group(2)) / 100
    band_team_fragment = band_match.group(3).strip()
    midpoint = (band_low + band_high) / 2

    if ref_team.split()[-1].lower() in band_team_fragment.lower() or ref_team.split()[0].lower() in band_team_fragment.lower():
        return midpoint, (band_low, band_high)
    else:
        return 1 - midpoint, (1 - band_high, 1 - band_low)


def main():
    parser = argparse.ArgumentParser(description="Score a completed match")
    parser.add_argument("case_dir", help="Path to case study directory")
    parser.add_argument("--winner", required=True, help="Winning team name")
    parser.add_argument("--prediction", type=float, help="Override: prediction for alphabetical ref team")
    parser.add_argument("--band", help="Override: band for ref team as low,high (e.g., 0.48,0.56)")
    parser.add_argument("--rules", nargs="*", default=[], help="Active rule IDs for this match")
    args = parser.parse_args()

    case_dir = Path(args.case_dir)
    if not case_dir.exists():
        print(f"Error: {case_dir} does not exist")
        sys.exit(1)

    team1, team2 = extract_teams_from_case(case_dir)
    ref_team, other_team = alphabetical_reference_team(team1, team2)

    print(f"Match: {team1} vs {team2}")
    print(f"Reference team (alphabetical): {ref_team}")
    print(f"Winner: {args.winner}")

    if args.prediction and args.band:
        prediction = args.prediction
        band_parts = args.band.split(",")
        band = (float(band_parts[0]), float(band_parts[1]))
    else:
        prediction, band = extract_prediction_from_memo(case_dir, ref_team, team1, team2)

    print(f"Prediction for {ref_team}: {prediction:.3f}")
    print(f"Band: [{band[0]:.3f}, {band[1]:.3f}]")

    result = compute_match_score(prediction, band, args.winner, team1, team2)

    print(f"\nBrier score: {result['brier_score']}")
    print(f"Band coverage: {result['band_coverage']}")
    print(f"vs Coin flip (0.25): {'+' if result['brier_score'] < 0.25 else ''}{result['brier_score'] - 0.25:.4f}")

    date_match = re.search(r"\*\*Date:\*\*\s*(.+)", (case_dir / "evidence_cutoff.md").read_text())
    match_date = date_match.group(1).strip() if date_match else "unknown"

    match_entry = {
        "case_id": case_dir.name,
        "date": match_date,
        "teams": [team1, team2],
        "active_rules": args.rules,
        **result,
    }

    scorecard = update_scorecard(str(SCORECARD_PATH), match_entry)
    agg = scorecard["aggregates"]
    print(f"\nScorecard updated ({agg['n_matches']} matches)")
    print(f"  Mean Brier: {agg['mean_brier']}")
    print(f"  vs Coin flip: {agg['vs_coinflip']:+.4f}")
    print(f"  Band coverage: {agg['band_coverage_rate']:.0%}")


if __name__ == "__main__":
    main()
