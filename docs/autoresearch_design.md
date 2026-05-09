# Autoresearch Implementation: What We're Building

## The Karpathy Loop (reference)

```
Hypothesize → Modify mutable surface → Run experiment → Measure scalar metric → Keep if improved, revert if not
```

Three structural requirements: single mutable surface, scalar metric, ratchet.

## Our Loop

```
Match happens → Brier score computed automatically → Rule performance updated →
Every 3-5 matches: consolidation runs automatically →
  validates existing rules, generates new candidates, mutates Reflection Log directly →
Next matches run with updated rules
```

No human approval gate in the loop. The system mutates the Reflection Log based on
Brier performance. Human role is experiment designer (writes `program.md` once) and
post-season auditor (reads `experiments.md` after), not in-loop approver.

### Mutable surface: `reflection/learning_log.md`

This is functionally part of the executable. The Skeptic and Synthesizer read the Reflection
Log at runtime — modifying the log modifies agent behavior on the next match. This is
equivalent to Karpathy modifying `train.py`: the file that changes is the file that produces
the output being measured.

### Scalar metric: Brier score

Prediction = memo's probability for Team A (teams ordered alphabetically, always).
Outcome = 1 if Team A won, 0 if not.
Brier score = (prediction - outcome)². Lower is better. Baseline (coin flip) = 0.25.

Alphabetical reference team removes ambiguity. Memos that say "no meaningful gap" still
produce a prediction (e.g., 0.52 for Team A) — that gets scored. No memos are excluded
from the experiment set.

**Secondary diagnostic:** band coverage rate (did the outcome fall within the stated band?).
Reported in scorecard, not used for rule pruning. Brier is the sole ratchet metric.

Computed automatically from prediction + binary outcome. No human judgment required.

### Fixed-cost experiment: one IPL match

Each match produces exactly one prediction, one outcome, one Brier score.
Cost is bounded (7 agent calls per match). Experiments are directly comparable.

### Ratchet: consolidation with evidence bar

Rules require **5+ applications** before the consolidation step acts on them.
Below that, rules are "tentative" — tracked but not validated.

Once a rule has 5+ applications:
- If it correlates with better Brier scores → strengthened (kept, possibly generalized)
- If it correlates with worse or no improvement → removed or modified
- If it's never triggered → flagged as too narrow, removed to reduce prompt noise

The consolidation step runs automatically. No approval gate. Every change is logged
in `experiments.md` with the metric values that justified it. Git tracks every mutation.
The system's mistakes at small N are part of the honest result, not something to prevent.

### Hypothesis generation: the piece that closes the loop

Karpathy's loop doesn't just validate — it generates new hypotheses from scratch.

Our consolidation step does both:

**Validation** (of existing rules):
- Which rules improved Brier? Which didn't?
- Prune, modify, or keep based on the ratchet.

**Generation** (of new candidate rules):
- Read all grades and scorecard entries
- Look for patterns the Reflection Log doesn't yet capture:
  - Matches where agents agreed but result diverged — what signal was missed?
  - Systematic band-width errors (too narrow? too wide?)
  - Contexts where specific evidence types (toss, weather, H2H) had outsized impact
- Each pattern becomes a **candidate rule** marked as "tentative"
- Applied for next 5 matches, then validated or discarded

This is the full Karpathy loop: generate, test, keep, repeat.

## The `program.md` Analog

Karpathy has `program.md` — the human-written rules of the game that the agent cannot
modify. Ours is `reflection/program.md`:

- Evidence threshold: 5 applications before a rule is validated or pruned
- Ratchet metric: Brier score (lower is better)
- Reference team: alphabetical (always score Team A's probability)
- Secondary diagnostic: band coverage (reported, not used for pruning)
- Consolidation trigger: every 3-5 matches
- What consolidation cannot do: modify program.md, modify agent definitions,
  modify the scoring function, exclude matches from the scorecard

These are set once at season start and frozen. The post-season audit checks whether
the consolidation logic operated correctly within these rules.

## What Gets Built (6 components)

### 1. `reflection/program.md`
The frozen rules of the game. Set once, never modified during the season.
The Karpathy `program.md` analog.

### 2. `tools/scoring/brier.py`
Computes Brier score from prediction + outcome. One function, no dependencies.
Also computes band coverage (boolean: did outcome fall in band?).

### 3. `scorecard.json`
Running experiment journal. Updated after every grading cycle. Tracks per-match:
prediction (Team A probability), outcome (binary), Brier score, band, band coverage,
which rules were active, grade. Aggregates: mean Brier, rolling Brier, band coverage
rate, vs coin-flip baseline (0.25).

### 4. Rule performance annotations on Reflection Log
Each rule entry gets tracked metadata: which matches it was active for, avg Brier
when active, status (tentative / validated / deprecated).

### 5. `run_consolidate.py`
The consolidation script. Runs automatically with no approval gate:
- Computes rule performance from scorecard
- Applies ratchet: prune, strengthen, or modify rules with 5+ applications
- Generates new candidate rules from cross-match pattern analysis
- Mutates `reflection/learning_log.md` directly
- Logs everything to `reflection/experiments.md`

### 6. `reflection/experiments.md`
Audit trail of every consolidation cycle: what was proposed, what was committed,
what the aggregate Brier was before and after, what new candidates were generated.
This is the post-season audit artifact.

## How Close to Karpathy This Gets

| Karpathy's Autoresearch | Ours | Gap |
|---|---|---|
| Mutable surface (train.py) | Reflection Log (read by agents at runtime) | Equivalent |
| Scalar metric (val_bpb) | Brier score (alphabetical team reference) | Equivalent |
| Fixed-cost experiment (5 min training) | One IPL match (7 agent calls) | Equivalent |
| Ratchet (commit if improved, revert if not) | 5-application evidence bar, then commit/revert | Equivalent (higher bar, appropriate for N) |
| Hypothesis generation (agent proposes code changes) | Consolidation proposes new rules from cross-match patterns | Equivalent |
| Full autonomy (never pauses for human) | Full autonomy (no approval gate, human audits after) | Equivalent |
| program.md (frozen rules of the game) | reflection/program.md (frozen season rules) | Equivalent |
| 700 experiments in 2 days | 15-20 experiments over one season | Scale gap (domain constraint, not design gap) |

**Honest framing for README:** This is autoresearch applied to probabilistic sports forecasting.
The loop structure matches Karpathy's (generate → test → measure → ratchet) with no human
in the loop. The scale doesn't (15-20 experiments vs 700) — that's a domain constraint, not
a design gap. At small N, some rule decisions will be wrong. Those mistakes are part of the
honest result, reported in experiments.md, not papered over by selective approval.

## What This Is NOT

- Not a claim that 15 matches gives statistical power equivalent to 700 experiments
- Not modifying agent prompts directly (that's v2, after more data)
- Not claiming the system "discovers" novel cricket insights — it discovers which
  reasoning patterns improve calibration for this specific forecasting task
- Not claiming zero human involvement — human designs the experiment (program.md)
  and audits afterward (experiments.md). Human is not in the loop during execution.

## Human Role (Experiment Designer + Post-Season Auditor)

**Before the season:** Write `program.md`. Define the rules. Freeze them.

**During the season:** Trigger each match's memo pipeline. Record results. The rest
(scoring, rule tracking, consolidation, log mutation) runs without intervention.

**After the season:** Read `experiments.md`. Assess:
- Did consolidation do what it was supposed to?
- Were any rule decisions clearly wrong in retrospect?
- Do validated rules generalize beyond this season?
- What would you change in `program.md` for next season?

This audit is the blog post.
