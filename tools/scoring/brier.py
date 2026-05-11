#!/usr/bin/env python3
"""
Brier score computation for Cricket Pricing Room.

Prediction = memo's probability for the alphabetically-first team.
Outcome = 1 if that team won, 0 if not.
Brier score = (prediction - outcome)^2. Lower is better. Baseline (coin flip) = 0.25.
"""

import json
import os
import tempfile
from pathlib import Path

TEAM_NORMALIZE = {
    "Royal Challengers Bangalore": "Royal Challengers Bengaluru",
    "Kings XI Punjab": "Punjab Kings",
    "Delhi Daredevils": "Delhi Capitals",
    "Rising Pune Supergiant": "Rising Pune Supergiants",
}


def alphabetical_reference_team(team1: str, team2: str) -> tuple[str, str]:
    teams = sorted([team1, team2])
    return teams[0], teams[1]


def brier_score(prediction: float, outcome: int) -> float:
    return (prediction - outcome) ** 2


def band_coverage_check(band_low: float, band_high: float, prediction: float, outcome: int) -> bool:
    """Check if the band's directional lean matched the outcome.

    Covered if: band midpoint > 0.5 and ref team won, or midpoint < 0.5 and ref team lost.
    Bands straddling 0.5 always count as covered (the forecast acknowledged uncertainty).
    """
    midpoint = (band_low + band_high) / 2
    if band_low <= 0.5 <= band_high:
        return True
    if outcome == 1:
        return midpoint > 0.5
    else:
        return midpoint < 0.5


def compute_match_score(memo_prediction: float, memo_band: tuple[float, float],
                        winner: str, team1: str, team2: str) -> dict:
    """Compute Brier score and band coverage for one match.

    Args:
        memo_prediction: the midpoint probability for the reference team (alphabetical)
        memo_band: (low, high) probability band for the reference team
        winner: name of the winning team
        team1, team2: the two teams in the match

    Returns:
        dict with brier_score, band_coverage, reference_team, prediction, outcome
    """
    ref_team, other_team = alphabetical_reference_team(team1, team2)
    normalized_winner = TEAM_NORMALIZE.get(winner.strip(), winner.strip())
    outcome = 1 if normalized_winner == ref_team else 0

    score = brier_score(memo_prediction, outcome)
    coverage = band_coverage_check(memo_band[0], memo_band[1], memo_prediction, outcome)

    return {
        "reference_team": ref_team,
        "other_team": other_team,
        "prediction": memo_prediction,
        "band": list(memo_band),
        "outcome": outcome,
        "winner": winner,
        "brier_score": round(score, 4),
        "band_coverage": coverage,
    }


def update_scorecard(scorecard_path: str, match_entry: dict) -> dict:
    """Append a match entry to the scorecard and recompute aggregates."""
    path = Path(scorecard_path)
    if path.exists():
        scorecard = json.loads(path.read_text())
    else:
        scorecard = {"matches": [], "aggregates": {}}

    existing_ids = {m["case_id"] for m in scorecard["matches"]}
    if match_entry.get("case_id") in existing_ids:
        return scorecard
    scorecard["matches"].append(match_entry)

    scores = [m["brier_score"] for m in scorecard["matches"]]
    coverages = [m["band_coverage"] for m in scorecard["matches"]]

    n = len(scores)
    mean_brier = sum(scores) / n
    coverage_rate = sum(coverages) / n

    last_5 = scores[-5:] if n >= 5 else scores
    rolling_brier = sum(last_5) / len(last_5)

    scorecard["aggregates"] = {
        "n_matches": n,
        "mean_brier": round(mean_brier, 4),
        "rolling_brier_5": round(rolling_brier, 4),
        "band_coverage_rate": round(coverage_rate, 4),
        "vs_coinflip": round(mean_brier - 0.25, 4),
    }

    tmp_fd, tmp_path = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
    try:
        with os.fdopen(tmp_fd, "w") as f:
            json.dump(scorecard, f, indent=2)
        os.replace(tmp_path, path)
    except Exception:
        os.unlink(tmp_path)
        raise
    return scorecard


if __name__ == "__main__":
    print("Brier score examples:")
    print(f"  Perfect prediction (1.0, won):  {brier_score(1.0, 1):.4f}")
    print(f"  Perfect prediction (0.0, lost): {brier_score(0.0, 0):.4f}")
    print(f"  Coin flip (0.5, won):           {brier_score(0.5, 1):.4f}")
    print(f"  Coin flip (0.5, lost):          {brier_score(0.5, 0):.4f}")
    print(f"  Confident wrong (0.8, lost):    {brier_score(0.8, 0):.4f}")
    print(f"  Slight lean correct (0.55, won):{brier_score(0.55, 1):.4f}")
    print()

    result = compute_match_score(
        memo_prediction=0.52,
        memo_band=(0.48, 0.56),
        winner="Gujarat Titans",
        team1="Rajasthan Royals",
        team2="Gujarat Titans",
    )
    print(f"Example: RR vs GT, GT wins, memo said GT 52%")
    print(f"  Reference team (alphabetical): {result['reference_team']}")
    print(f"  Prediction for ref team: {result['prediction']}")
    print(f"  Outcome: {result['outcome']} ({'ref team won' if result['outcome'] else 'ref team lost'})")
    print(f"  Brier score: {result['brier_score']}")
    print(f"  Band coverage: {result['band_coverage']}")
