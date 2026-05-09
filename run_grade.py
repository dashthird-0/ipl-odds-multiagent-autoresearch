#!/usr/bin/env python3
"""
Cricket Pricing Room — Post-Match Grading Workflow

Records the match result and prints instructions for running the
Post-Match Grader agent and updating the Reflection Log.

Usage:
    # Record result interactively:
    python3 run_grade.py case_studies/match_001_rr_vs_gt

    # Record result inline:
    python3 run_grade.py case_studies/match_001_rr_vs_gt --winner "Gujarat Titans" --by "6 wickets"
"""

import argparse
from datetime import datetime, timezone
from pathlib import Path


def record_result(case_dir: Path, winner: str, margin: str, notes: str = ""):
    result_doc = f"""# Match Result

**Winner:** {winner}
**Margin:** {margin}
**Recorded at:** {datetime.now(timezone.utc).isoformat()}

{f'## Notes{chr(10)}{notes}' if notes else ''}
"""
    (case_dir / "result.md").write_text(result_doc)
    print(f"Result recorded: {winner} won by {margin}")


def print_grading_steps(case_dir: Path):
    print(f"""
{'='*60}
Post-match grading workflow
{'='*60}

In Claude Code, run:

  1. "Run Post-Match Grader for {case_dir.name}.
     Read all files in {case_dir}/.
     Grade the memo's reasoning against the result.
     Write to {case_dir}/post_match_grade.md."

  2. "Read the grade at {case_dir}/post_match_grade.md.
     Extract the 'Lessons for Reflection Log' section.
     Append those lessons to reflection/learning_log.md
     in the established format."

This completes the case study cycle.
""")


def main():
    parser = argparse.ArgumentParser(description="Record match result and trigger grading")
    parser.add_argument("case_dir", help="Path to case study directory")
    parser.add_argument("--winner", help="Winning team name")
    parser.add_argument("--by", help="Winning margin (e.g., '6 wickets', '23 runs')")
    parser.add_argument("--notes", help="Additional notes about the match", default="")
    args = parser.parse_args()

    case_dir = Path(args.case_dir)
    if not case_dir.exists():
        print(f"Error: {case_dir} does not exist")
        return

    if args.winner and args.by:
        record_result(case_dir, args.winner, args.by, args.notes)
    else:
        print(f"Case study: {case_dir.name}")
        print()
        winner = input("Winner: ").strip()
        margin = input("Margin (e.g., '6 wickets'): ").strip()
        notes = input("Notes (optional): ").strip()
        if winner and margin:
            record_result(case_dir, winner, margin, notes)
        else:
            print("Skipped — no result recorded")

    print_grading_steps(case_dir)


if __name__ == "__main__":
    main()
