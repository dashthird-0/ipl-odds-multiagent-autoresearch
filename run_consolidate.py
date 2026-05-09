#!/usr/bin/env python3
"""
Cricket Pricing Room — Consolidation Runner

Runs the Karpathy ratchet: validates existing rules, generates new candidates,
and mutates the Reflection Log based on Brier performance.

Triggers automatically every 3-5 graded matches. No human approval gate.

Usage:
    python3 run_consolidate.py

    # Dry run (show what would change, don't mutate):
    python3 run_consolidate.py --dry-run

    # Force run even if < 3 new matches since last consolidation:
    python3 run_consolidate.py --force
"""

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
SCORECARD_PATH = PROJECT_ROOT / "scorecard.json"
LEARNING_LOG_PATH = PROJECT_ROOT / "reflection" / "learning_log.md"
EXPERIMENTS_PATH = PROJECT_ROOT / "reflection" / "experiments.md"
PROGRAM_PATH = PROJECT_ROOT / "reflection" / "program.md"

EVIDENCE_THRESHOLD = 5
CONSOLIDATION_INTERVAL = (3, 5)


def load_scorecard() -> dict:
    if not SCORECARD_PATH.exists():
        return {"matches": [], "aggregates": {}}
    return json.loads(SCORECARD_PATH.read_text())


def count_matches_since_last_consolidation() -> int:
    experiments = EXPERIMENTS_PATH.read_text()
    scorecard = load_scorecard()
    n_matches = len(scorecard["matches"])

    consolidation_matches = re.findall(r"Matches at time of run: (\d+)", experiments)
    if consolidation_matches:
        last_n = int(consolidation_matches[-1])
        return n_matches - last_n
    return n_matches


def compute_rule_performance(scorecard: dict) -> dict:
    """Compute per-rule Brier averages from scorecard entries that track active rules."""
    rule_stats = {}
    for match in scorecard["matches"]:
        active_rules = match.get("active_rules", [])
        brier = match["brier_score"]
        for rule_id in active_rules:
            if rule_id not in rule_stats:
                rule_stats[rule_id] = {"applications": 0, "total_brier": 0.0, "scores": []}
            rule_stats[rule_id]["applications"] += 1
            rule_stats[rule_id]["total_brier"] += brier
            rule_stats[rule_id]["scores"].append(brier)

    for rule_id, stats in rule_stats.items():
        stats["avg_brier"] = round(stats["total_brier"] / stats["applications"], 4)

    return rule_stats


def generate_consolidation_report(scorecard: dict, rule_perf: dict, dry_run: bool) -> str:
    """Generate the consolidation report for experiments.md."""
    now = datetime.now(timezone.utc).isoformat()
    n = len(scorecard["matches"])
    agg = scorecard.get("aggregates", {})

    report = f"""
## Consolidation Run — {now}

Matches at time of run: {n}
Mean Brier: {agg.get('mean_brier', 'N/A')}
Rolling Brier (last 5): {agg.get('rolling_brier_5', 'N/A')}
Band coverage rate: {agg.get('band_coverage_rate', 'N/A')}
vs Coin flip: {agg.get('vs_coinflip', 'N/A')}
Mode: {'DRY RUN' if dry_run else 'LIVE'}

### Rule Performance

"""
    if not rule_perf:
        report += "_No rules with tracked applications yet._\n"
    else:
        report += "| Rule | Applications | Avg Brier | Status |\n"
        report += "|------|-------------|-----------|--------|\n"
        for rule_id, stats in sorted(rule_perf.items()):
            status = "tentative" if stats["applications"] < EVIDENCE_THRESHOLD else "ready for validation"
            report += f"| {rule_id} | {stats['applications']} | {stats['avg_brier']} | {status} |\n"

    report += "\n### Actions Taken\n\n"
    actions = []

    for rule_id, stats in rule_perf.items():
        if stats["applications"] >= EVIDENCE_THRESHOLD:
            overall_avg = agg.get("mean_brier", 0.25)
            if stats["avg_brier"] < overall_avg - 0.02:
                actions.append(f"- VALIDATED: {rule_id} (avg {stats['avg_brier']} vs overall {overall_avg})")
            elif stats["avg_brier"] > overall_avg + 0.02:
                actions.append(f"- DEPRECATED: {rule_id} (avg {stats['avg_brier']} vs overall {overall_avg})")
            else:
                actions.append(f"- KEPT (neutral): {rule_id} (avg {stats['avg_brier']} ≈ overall {overall_avg})")

    if not actions:
        report += "_No rules reached the 5-application evidence threshold yet._\n"
    else:
        report += "\n".join(actions) + "\n"

    report += "\n### New Candidates Generated\n\n"
    report += "_Candidate generation requires Claude Code agent invocation (see below)._\n"

    return report


def main():
    parser = argparse.ArgumentParser(description="Run consolidation cycle")
    parser.add_argument("--dry-run", action="store_true", help="Show what would change without mutating")
    parser.add_argument("--force", action="store_true", help="Run even if < 3 matches since last")
    args = parser.parse_args()

    scorecard = load_scorecard()
    n_matches = len(scorecard["matches"])

    if n_matches == 0:
        print("No matches in scorecard. Nothing to consolidate.")
        return

    new_since_last = count_matches_since_last_consolidation()
    print(f"Matches in scorecard: {n_matches}")
    print(f"New since last consolidation: {new_since_last}")

    if new_since_last < CONSOLIDATION_INTERVAL[0] and not args.force:
        print(f"Need at least {CONSOLIDATION_INTERVAL[0]} new matches. Use --force to override.")
        return

    rule_perf = compute_rule_performance(scorecard)
    report = generate_consolidation_report(scorecard, rule_perf, args.dry_run)

    print("\n" + "=" * 60)
    print(report)
    print("=" * 60)

    if not args.dry_run:
        experiments_text = EXPERIMENTS_PATH.read_text()
        if "_No consolidation runs yet" in experiments_text:
            experiments_text = "# Experiments Log\n\nAudit trail of every consolidation cycle.\n\n---\n"
        experiments_text += report
        EXPERIMENTS_PATH.write_text(experiments_text)
        print(f"\nAppended to {EXPERIMENTS_PATH}")

        print(f"""
To complete consolidation, tell Claude Code:

  "Run consolidation analysis on the scorecard.
   Read {SCORECARD_PATH} and {LEARNING_LOG_PATH}.
   For rules with 5+ applications:
   - If avg Brier < overall mean - 0.02: validate (mark as validated)
   - If avg Brier > overall mean + 0.02: deprecate (mark as deprecated)
   - If never triggered: remove as too narrow
   Generate 1-3 new candidate rules from cross-match patterns.
   Mutate {LEARNING_LOG_PATH} directly.
   Log all changes to {EXPERIMENTS_PATH}."
""")
    else:
        print("\nDry run — no files modified.")


if __name__ == "__main__":
    main()
