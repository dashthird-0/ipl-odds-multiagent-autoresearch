# ipl-odds-multiagent-autoresearch

ipl-odds-multiagent-autoresearch is a self-updating IPL forecasting research system. It produces a pre-match forecast before each IPL match, grades the forecast against the actual outcome, and rewrites its own reasoning rules across the season without any human intervention. The rule library mutates based on Brier score performance alone. Whether that mutation improves calibration over the season is the experiment.

It's built on [Claude Code](https://claude.ai/code) with seven specialist subagents. The multi-agent part is table stakes at this point; the interesting piece is the autoresearch loop on top.

The architecture is general (any domain with public prediction markets), but right now it's pointed at IPL 2026 with [Polymarket](https://polymarket.com/) as the calibration anchor.

## How It Works

```
  ┌──────────────────────────────────────────────────────────┐
  │                    BEFORE EACH MATCH                     │
  │                                                          │
  │  Market Reader ──┐                                       │
  │  Stats Analyst ──┼──→ Skeptic ──→ Synthesizer ──→ MEMO  │
  │  News Analyst ───┤                                       │
  │       │          │                                       │
  │  Source Clerk ───┘                                       │
  └──────────────────────────────────────────────────────────┘
                            │
                      ══════════════
                      ║ MATCH PLAYS ║
                      ══════════════
                            │
  ┌──────────────────────────────────────────────────────────┐
  │                    AFTER EACH MATCH                      │
  │                                                          │
  │  Post-Match Grader ──→ Brier Score ──→ Reflection Log   │
  │                                                          │
  │  Every 3 matches:                                        │
  │  Consolidation ──→ prune / strengthen / generate rules   │
  └──────────────────────────────────────────────────────────┘
                            │
                      ┌─────┘
                      ▼
               Next match forecast
          (informed by updated rules)
```

1. **Before the match:** Seven agents produce a pre-match forecast. Market Reader fetches Polymarket prices. Stats Analyst queries 1,219 IPL matches from [Cricsheet](https://cricsheet.org/). News Analyst searches for team news, pitch reports, weather. Source Quality Clerk audits every source. Base-Rate Skeptic pushes back on narrative overreach. Fair Value Synthesizer writes the forecast.

2. **After the match:** Post-Match Grader evaluates the reasoning (not just whether we got it right) and proposes rules for the Reflection Log.

3. **Every 3 matches:** Consolidation runs automatically. It prunes rules that worsen calibration, strengthens rules that improve it, and generates new candidates from cross-match patterns.

The forecast pipeline alone is a standard multi-agent system. The loop on top is what makes it self-improving.

## The Autoresearch Loop

The Reflection Log (`reflection/learning_log.md`) is the system's mutable knowledge. Rules are pattern-level ("When X, do Y because Z"), not match-specific facts. Each rule tracks how many times it's been applied and whether it's tentative, validated, or deprecated.

The ratchet metric is **Brier score**: `(prediction - outcome)²`, lower is better, 0.25 = coin flip. Rules need 5+ applications before consolidation can act on them. This prevents overfitting to small samples.

The frozen rules of the game (`reflection/program.md`) define what the loop can and cannot touch. Consolidation can rewrite the Reflection Log but cannot modify `program.md`, agent definitions, or the scoring function. Mutable surface, immutable program. That's what makes it safe to run without supervision.

Important limitation: Brier is the only ratchet metric. The system may reward correct forecasts for the wrong reasons, and bad reasoning that produces a well-calibrated number can still strengthen a rule. Reasoning-quality failures are logged but don't drive rule mutation in v1. Keeping the ratchet simple makes the experiment auditable. Will evaluate adding a reasoning-validity gate as v2.

## No Human in the Loop

There's no human approval gate on rule changes. After consolidation, updates go straight to the Reflection Log. Git tracks every mutation and `experiments.md` logs the numbers behind each decision, but nobody reviews the changes before they take effect.

I want to be explicit about why this matters. Most multi-agent systems that claim self-improvement have a human reviewer filtering out bad rule mutations. The system looks disciplined, but the discipline is coming from the human, not the mechanism. Here, the discipline comes from two things: the pre-committed rules in `program.md` (frozen at season start) and the Brier score (computed automatically). That's it.

At small N (15-22 matches over IPL 2026), some rule decisions will be wrong. Those mistakes show up in `experiments.md` as part of the result.

This is the first time I'm running a system like this with fully autonomous rule mutation. End-of-season blog post will cover what worked and what didn't.

## How This Differs from Council and Debate Patterns

Council and debate patterns (CrewAI, multi-agent debate papers) are typically single-shot: agents debate, produce a decision, done. This project is different in two ways.

The agents don't debate. They hand off through files. Stats Analyst writes query results to JSON. News Analyst writes structured markdown. Skeptic reads both and writes its review. Synthesizer reads everything and writes the forecast. It's a pipeline, not a conversation.

More importantly, it's not single-shot. After each match, the Grader scores the forecast. Every few matches, consolidation rewrites the rule library based on what's actually working. Council patterns don't have this layer.

## Run It Yourself

```bash
# Build evidence + run agents for an upcoming match
python3 run_pipeline.py RR GT "Sawai Mansingh Stadium" 2026-05-10

# Score a completed match
python3 run_score.py case_studies/exp_001_rr_vs_gt --winner "Gujarat Titans"

# Run consolidation (after 3+ graded matches)
python3 run_consolidate.py

# Full auto-pilot (discovers matches, triggers, grades, consolidates)
python3 auto_pilot.py --install    # cron every 5 min
python3 auto_pilot.py --status     # check state machine
python3 auto_pilot.py --dry-run    # preview without acting
```

The auto-pilot runs on a VPS. It discovers matches from Polymarket, triggers at toss + 15 minutes (post-toss, pre-first-ball), detects results from market resolution, auto-grades, and runs consolidation. See `auto_pilot.py` for the trigger logic and state machine.

## Output Format

Forecasts output probability bands, not point estimates:

```
Anchor price:      GT 51.5% (Polymarket, $112K volume)
Model band:        GT 48-56%
Directional view:  Slight GT lean, effectively a coin flip
Confidence:        Medium
Main uncertainty:  First-time captain, reconfigured bowling attack
```

## Frozen Evidence Discipline

Every case study is a self-contained evidence packet:
- `evidence_cutoff.md` - what was knowable before first ball
- `market_snapshot.json` - frozen Polymarket state (VPS-captured pre-toss)
- `stats_snapshot.json` - Cricsheet query results
- `sources_fetched.md` - every external source, with URL and date
- Full agent outputs (news, source quality, skeptic review, pre-match forecast (memo.md), grade)

Evidence packets are built once, before first ball, and never modified after that. The agents run against the frozen packet, not against live web search at forecast-generation time. Anyone reading the case study folder can verify exactly what the agents could and couldn't see. See [docs/evidence_discipline.md](docs/evidence_discipline.md).

## Status

| Match | Date | Forecast | Result | Brier | Grade |
|-------|------|-----------|--------|-------|-------|
| [RR vs GT](case_studies/exp_001_rr_vs_gt/) | 2026-05-09 | GT 45-55% | GT won by 77 runs | 0.250 | C+ |
| [CSK vs LSG](case_studies/exp_002_csk_vs_lsg/) | 2026-05-10 | CSK 53-63% | CSK won by 5 wickets | 0.176 | B+ |
| [RCB vs MI](case_studies/exp_003_rcb_vs_mi/) | 2026-05-10 | RCB 52-62% | RCB won by 2 wickets | 0.185 | B |
| [PBKS vs DC](case_studies/exp_004_pbks_vs_dc/) | 2026-05-11 | PBKS 49-61% | DC won by 3 wickets | 0.303 | B+ |
| [GT vs SRH](case_studies/exp_005_gt_vs_srh/) | 2026-05-12 | GT 49-61% | GT won by 82 runs | 0.203 | A- |
| [RCB vs KKR](case_studies/exp_006_rcb_vs_kkr/) | 2026-05-13 | RCB 46-62% | RCB won by 6 wickets | 0.212 | B+ |
| [PBKS vs MI](case_studies/exp_007_pbks_vs_mi/) | 2026-05-14 | PBKS 53-61% | MI won by 6 wickets | 0.325 | C+ |

**Running Brier: 0.236** across 7 matches (0.25 = coin flip). Band coverage: 86% (6/7).

Live through IPL 2026. Scorecard: [`scorecard.json`](scorecard.json). Experiment log: [`reflection/experiments.md`](reflection/experiments.md).

## Frozen Rules of the Game

[`reflection/program.md`](reflection/program.md) is frozen at season start. It defines:
- Brier score as the sole ratchet metric
- Alphabetically-first team as reference (removes scoring ambiguity)
- 5-application threshold before rules can be validated
- Forward-only constraint (no retrospective matches)
- Post-toss, pre-first-ball evidence cutoff
- 8 frozen search query templates for news gathering
- What consolidation can and cannot modify

No agent and no consolidation step can change this file.

## Data Sources

- **[Cricsheet](https://cricsheet.org/)** - 1,219 IPL matches, ball-by-ball, CC0 license
- **[Polymarket](https://polymarket.com/)** - public Gamma API for market-implied probabilities (no auth)
- **Web search** - team news, pitch reports, weather. The search queries are frozen in `program.md`, but the returned source set varies per match. The Source Quality Clerk audits each source's reliability and timestamp after the fact.

## FAQ

**"T20 is a super high variance game. Is it even practical to model it?"**
Yes, and that's the point. We might get to the end of the season and realize this is useless. But I'm genuinely curious if a self-improving AI system can learn to model T20 madness, or is it just noise all the way down.

**"Isn't it too early to claim the model is better than prediction markets?"**
Of course. Sample is too low to make any conclusions. Treating these as interesting early reads.

**"Why Polymarket? Why not Cricbuzz or Cricinfo?"**
A prediction market with $50-100K in real money on each match is a harder benchmark than an expert panel. Also, Cricbuzz and Cricinfo don't publish these probabilities in a reliable way.

**"You say zero human inputs but I see commits in the repo?"**
Code changes and bug fixes are human driven. The forecasts, grades, rules, and scoring run autonomously on a VPS cron. No human reviews the memo before the match or approves rule changes after grading. Git history shows which commits are mine (code) vs the auto-pilot's (output).

## What This Is Not

- Does not claim to beat market prices
- Does not place, recommend, or automate trades
- Does not interact with any trading frontend

Polymarket's trading frontend is geo-restricted in India. This project does not interact with that interface. The public data API is queried for research purposes only, to study how multi-agent reasoning calibrates against public market prices. See [docs/legality_note.md](docs/legality_note.md).

## License

MIT

---

Built by [Sid](https://github.com/dashthird-0) with Claude Code.
