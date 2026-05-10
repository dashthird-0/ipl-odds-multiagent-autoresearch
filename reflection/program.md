# Program — Frozen Rules of the Game

Set once at season start. Not modifiable by the consolidation step or any agent.
This is the Karpathy `program.md` analog: the rules that define what the autoresearch
loop can and cannot do.

---

## Metric

**Brier score** is the sole ratchet metric.
- Prediction = memo's probability for the alphabetically-first team
- Outcome = 1 if that team won, 0 otherwise
- Brier = (prediction - outcome)²
- Lower is better. Baseline (coin flip) = 0.25

## Reference Team Convention

Always use the alphabetically-first team as the reference.
"Gujarat Titans vs Rajasthan Royals" → reference team = Gujarat Titans.
This removes all ambiguity from scoring.

## Evidence Threshold

A rule requires **5+ applications** before the consolidation step can validate or prune it.
Below 5, rules are "tentative" — tracked but not acted on by the ratchet.

## Secondary Diagnostic

**Band coverage rate** — did the outcome fall on the expected side given the band?
Reported in the scorecard. NOT used for rule pruning. Brier is the sole ratchet.

## Consolidation Trigger

Every **3-5 matches**, consolidation runs automatically.
No human approval gate. Changes are logged in `reflection/experiments.md`.

## What Consolidation CAN Do

- Validate or prune rules in `reflection/learning_log.md` based on Brier performance
- Generate new candidate rules from cross-match pattern analysis
- Modify rule wording for clarity
- Mark rules as tentative, validated, or deprecated

## What Consolidation CANNOT Do

- Modify this file (`program.md`)
- Modify agent definitions (`.claude/agents/*.md`)
- Modify the scoring function (`tools/scoring/brier.py`)
- Exclude matches from the scorecard
- Change the evidence threshold (5 applications)
- Change the ratchet metric (Brier)
- Change the reference team convention (alphabetical)

## Season Scope

IPL 2026 second half. Target: 15-22 forward matches (Match 52 onward).
Post-season audit reads `reflection/experiments.md` to assess system performance.

## Forward-Only Constraint

All experiments use **live Polymarket prices captured pre-toss** from the automated
VPS snapshot cron. No retrospective matches in the experiment set.

Rationale: historical Polymarket prices are not recoverable after market resolution
(API purges timeseries for closed markets). Synthetic/constructed anchors would mean
calibrating model against itself. Retrospective memos are contaminated by the model's
knowledge of outcomes. Forward-only eliminates both problems.

The Reflection Log starts empty. Rules emerge from forward grading only.

## Evidence Cutoff: Post-Toss, Pre-First-Ball

All agents operate on evidence available after the toss but before the first ball is bowled.
This means:
- Toss result is known (who bats/bowls first)
- Confirmed playing XIs are known (announced at toss)
- Market price reflects toss outcome and confirmed XIs
- Both the system and the market have the same information set

This is deliberate: we are testing whether multi-agent reasoning adds value over an
informed market, not whether we can predict coin flips (toss) or guess team selections.

## News Search Protocol

The News & Conditions Analyst uses open web search with a frozen query protocol.
Source-set variance is expected across matches; the protocol is what's frozen.

### Search Query Templates

For a match {Team1} vs {Team2} at {Venue} on {Date}, execute these searches:

1. `"{Team1} vs {Team2} playing XI {Date}"` — confirmed/likely team selections
2. `"{Team1} vs {Team2} team news injury"` — injury updates, availability
3. `"{Venue} pitch report IPL 2026"` — pitch behavior, curator comments
4. `"{Team1} vs {Team2} weather forecast {Date}"` — match-day conditions
5. `"{Team1} IPL 2026 form"` — recent team performance context
6. `"{Team2} IPL 2026 form"` — recent team performance context
7. `"{Team1} vs {Team2} preview IPL 2026"` — journalist previews, tactical signals
8. `"IPL 2026 points table playoff scenarios"` — standings context

### Date Window

- Earliest: match-day minus 3 days
- Latest: toss time (post-toss sources allowed only for toss result + confirmed XI)
- Sources without a visible publication date: flagged as "undated" in sources log

### Inclusion Rule

Any cricket-relevant page returned by the template queries within the date window.
No manual exclusion based on content — the Source Quality Clerk handles discrimination.

### Exclusion Rule (hard, applied before Clerk)

- Published outside the date window
- Non-English
- Off-topic (not about this match, these teams, or this venue)
- Paywalled content not accessible via search snippet
- On double-header days: results/post-match coverage from the earlier match must not
  inform the later match's memo. Each match's date window ends at its own toss time.

### Source Logging

Every source fetched is logged to `case_studies/{case_id}/sources_fetched.md`:

```
| # | URL | Published | Query | Role |
|---|-----|-----------|-------|------|
| 1 | https://... | 2026-05-09 | query_1 | team news |
| 2 | https://... | undated | query_3 | pitch report |
```

This is the audit artifact. The Source Quality Clerk reads this + the News Analyst
output to perform its 3-tier assessment.

### Variance Acknowledgment

Different runs of the same match may produce different source sets (search results
vary by time, personalization, availability). This is expected and acceptable.
What's frozen is the protocol, not the output. Comparability across experiments
comes from the consistent query structure and the Clerk's standardized audit.

## Market Anchor

- Source: Polymarket Gamma API (tag_id=101988)
- Captured by: VPS cron at VPS_IP_REDACTED, every 30 minutes
- Official snapshot: last VPS capture before first ball (post-toss). This is the hard
  physical anchor — toss time is fixed, memo-generation time varies. Do not change mid-season.
- Minimum volume for valid anchor: $10,000 (markets below this are flagged as thin)

## Human Role

- **Before season:** Write this file. Freeze it.
- **During season:** Trigger match pipelines. Record results. Everything else is autonomous.
- **After season:** Audit `experiments.md`. Write the blog post.
