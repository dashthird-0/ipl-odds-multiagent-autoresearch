# Can an AI system teach itself to predict cricket?

Seven AI agents forecast every IPL 2026 match, graded their own work, and rewrote their own playbook. No human in the loop. This repo is the full record of what they did and how it went.

## The experiment

I wanted to know if an AI system could get better at something on its own, without me correcting it.

So I picked something hard to call: IPL cricket. Before every match of the 2026 season, seven AI agents read the team news, dug through 1,219 past matches, and checked what the prediction market thought. Then they wrote a forecast. After the match, the system graded its own forecast and rewrote the rules it uses to reason. Every match, for a full season. I fixed bugs and watched. I never wrote or changed a forecast.

It runs on [Claude Code](https://claude.ai/code). The multi-agent forecasting is the ordinary part. The part I cared about is the loop on top, where the system scores itself and edits its own rulebook with nobody approving the changes.

## What happened

It came out slightly better than a coin flip, and it drew level with the prediction market without beating it.

To keep score I used the method weather forecasters are judged by. You lose more points the more confident you are when you turn out wrong. Lower is better, and a coin flip scores 0.25. The system averaged 0.242 across 23 matches. Better than guessing, but only just.

The result I found more interesting: on the matches that had real money behind them, the system matched the market almost exactly and found nothing the market had missed. T20 cricket is close to a coin flip, and a system that teaches itself runs into the same wall the market does.

| Question | Answer |
|---|---|
| Beat a coin flip? | Yes, barely (0.242 vs 0.25) |
| Matched the prediction market? | Yes (0.237 vs 0.241 on liquid markets) |
| Beat the market? | No |
| Ran a full season with no human in the loop? | Yes |

The full write-up is in [docs/season_review_2026.md](docs/season_review_2026.md): how it scored, whether it beat the market, what the self-editing loop actually learned, and what I would change next. Everything below is the machinery, for anyone who wants it.

## How it works

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

1. **Before the match:** Seven agents produce a forecast. Market Reader fetches Polymarket prices. Stats Analyst queries 1,219 IPL matches from [Cricsheet](https://cricsheet.org/). News Analyst searches for team news, pitch reports, and weather. Source Quality Clerk checks every source. Base-Rate Skeptic pushes back on narrative overreach. Fair Value Synthesizer writes the forecast.

2. **After the match:** Post-Match Grader scores the reasoning, not just whether the pick was right, and proposes rules for the Reflection Log.

3. **Every 3 matches:** Consolidation runs on its own. It prunes rules that hurt calibration, keeps rules that help, and generates new candidates from patterns across matches.

The agents don't debate. They hand off through files. Stats Analyst writes JSON, News Analyst writes markdown, the Skeptic reads both and writes its review, the Synthesizer reads everything and writes the forecast. It's a pipeline, not a conversation.

## The self-improving part

The Reflection Log ([`reflection/learning_log.md`](reflection/learning_log.md)) is the system's mutable memory. Rules are patterns ("when X, do Y because Z"), not match facts. Each rule tracks how many times it has been applied and whether it is tentative, validated, or deprecated.

The score that drives everything is the same weather-forecaster score from above (the Brier score: prediction minus outcome, squared). Rules need 5 or more applications before consolidation can act on them, so a short hot streak can't validate a rule.

The frozen rules of the game ([`reflection/program.md`](reflection/program.md)) set what the loop can and can't touch. Consolidation can rewrite the Reflection Log. It cannot touch `program.md`, the agent definitions, or the scoring function. Mutable memory, immutable rules. That is what makes it safe to leave running.

There is no human approval step. After consolidation, rule changes go straight into the Reflection Log. Most systems that claim self-improvement keep a person filtering out the bad rule changes, and that person is where the discipline actually comes from. Here the discipline comes from two things only: the frozen `program.md` and the automatic score. At 23 matches, some of the rule decisions were wrong, and those are in [`reflection/experiments.md`](reflection/experiments.md) as part of the result.

One honest limitation: the score is the only thing that prunes rules. The system can keep a well-scored rule for bad reasons, or cut a sound rule because the matches it touched happened to go the other way. That happened this season. A fix for it is the main next step below.

None of this is cricket-specific. It works for any domain with a public prediction market to grade against. Cricket is the hard test case I picked.

## See it yourself

Every match is a self-contained evidence packet, built once before the first ball and never touched again:
- `evidence_cutoff.md` - what was knowable before the first ball
- `market_snapshot.json` - frozen Polymarket state, captured pre-toss
- `stats_snapshot.json` - the Cricsheet query results
- `sources_fetched.md` - every external source, with URL and date
- the full agent outputs (news, source quality, skeptic review, the forecast, the grade)

Anyone can open a case study folder and see exactly what the agents could and couldn't know. Start with [exp_014_kkr_vs_mi](case_studies/exp_014_kkr_vs_mi/), the best-scored match of the season, or browse the [full list](case_studies/). More on why the packet is frozen: [docs/evidence_discipline.md](docs/evidence_discipline.md).

Forecasts come out as probability bands, not single numbers:

```
Anchor price:      GT 51.5% (Polymarket, $112K volume)
Model band:        GT 48-56%
Directional view:  Slight GT lean, effectively a coin flip
Confidence:        Medium
Main uncertainty:  First-time captain, reconfigured bowling attack
```

Run it yourself:

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

The auto-pilot ran on a VPS. It discovered matches from Polymarket, triggered post-toss and pre-first-ball, detected results from market resolution, auto-graded, and ran consolidation. See `auto_pilot.py` for the trigger logic and state machine.

## Full results

Final score: 0.242 average Brier across 23 matches (0.25 is a coin flip), so it beat the baseline by 0.008. The band held 91% of the time (21 of 23 results landed inside the model's range). The first 12 matches averaged 0.255 and the last 11 averaged 0.227, so it calibrated a little better as the rulebook matured.

<details>
<summary>Match-by-match table (all 23 matches)</summary>

| Match | Date | Forecast | Result | Brier | Grade |
|-------|------|-----------|--------|-------|-------|
| [RR vs GT](case_studies/exp_001_rr_vs_gt/) | 2026-05-09 | GT 45-55% | GT won by 77 runs | 0.250 | C+ |
| [CSK vs LSG](case_studies/exp_002_csk_vs_lsg/) | 2026-05-10 | CSK 53-63% | CSK won by 5 wickets | 0.176 | B+ |
| [RCB vs MI](case_studies/exp_003_rcb_vs_mi/) | 2026-05-10 | RCB 52-62% | RCB won by 2 wickets | 0.185 | B |
| [PBKS vs DC](case_studies/exp_004_pbks_vs_dc/) | 2026-05-11 | PBKS 49-61% | DC won by 3 wickets | 0.303 | B+ |
| [GT vs SRH](case_studies/exp_005_gt_vs_srh/) | 2026-05-12 | GT 49-61% | GT won by 82 runs | 0.203 | A- |
| [RCB vs KKR](case_studies/exp_006_rcb_vs_kkr/) | 2026-05-13 | RCB 46-62% | RCB won by 6 wickets | 0.212 | B+ |
| [PBKS vs MI](case_studies/exp_007_pbks_vs_mi/) | 2026-05-14 | PBKS 53-61% | MI won by 6 wickets | 0.325 | C+ |
| [LSG vs CSK](case_studies/exp_008_lsg_vs_csk/) | 2026-05-15 | CSK 45-55% | LSG won by 7 wickets | 0.250 | B+ |
| [KKR vs GT](case_studies/exp_009_kkr_vs_gt/) | 2026-05-16 | GT 51-63% | KKR won by 29 runs | 0.325 | B |
| [PBKS vs RCB](case_studies/exp_010_pbks_vs_rcb/) | 2026-05-17 | RCB 48-56% | RCB won by 23 runs | 0.230 | B+ |
| [DC vs RR](case_studies/exp_011_dc_vs_rr/) | 2026-05-17 | RR 48-64% | DC won by 5 wickets | 0.314 | C+ |
| [CSK vs SRH](case_studies/exp_012_csk_vs_srh/) | 2026-05-18 | CSK 47-61% | SRH won | 0.292 | B- |
| [RR vs LSG](case_studies/exp_013_rr_vs_lsg/) | 2026-05-19 | RR 53-63% | RR won | 0.176 | B+ |
| [KKR vs MI](case_studies/exp_014_kkr_vs_mi/) | 2026-05-20 | KKR 53-66% | KKR won | 0.164 | B+ |
| [GT vs CSK](case_studies/exp_015_gt_vs_csk/) | 2026-05-21 | GT 51-66% | GT won | 0.172 | B+ |
| [SRH vs RCB](case_studies/exp_016_srh_vs_rcb/) | 2026-05-22 | RCB 42-58% | SRH won | 0.250 | B- |
| [LSG vs PBKS](case_studies/exp_017_lsg_vs_pbks/) | 2026-05-23 | PBKS 50-58% | PBKS won | 0.212 | B+ |
| [MI vs RR](case_studies/exp_018_mi_vs_rr/) | 2026-05-24 | RR 49-59% | RR won | 0.212 | A- |
| [KKR vs DC](case_studies/exp_019_kkr_vs_dc/) | 2026-05-24 | KKR 47-63% | DC won | 0.302 | B- |
| [RCB vs GT](case_studies/exp_020_rcb_vs_gt/) | 2026-05-26 | GT 43-59% | RCB won | 0.260 | C+ |
| [SRH vs RR](case_studies/exp_021_srh_vs_rr/) | 2026-05-27 | SRH 53-63% | RR won | 0.336 | B- |
| [GT vs RR](case_studies/exp_022_gt_vs_rr/) | 2026-05-29 | GT 47-63% | GT won | 0.203 | B+ |
| [RCB vs GT](case_studies/exp_023_rcb_vs_gt/) | 2026-05-31 | RCB 49-59% | RCB won | 0.212 | B |

</details>

Machine-readable scorecard: [`scorecard.json`](scorecard.json). Consolidation audit trail: [`reflection/experiments.md`](reflection/experiments.md). The rulebook ended with 32 rules: 3 validated, 2 deprecated, the rest tentative.

## What's next

**A reasoning check.** Right now the score is the only thing that prunes rules, which means a sound rule can get cut because its matches went the wrong way. A second signal that grades whether a rule's logic held, separate from whether the match won, would fix that. This is the main v2 item.

**More matches.** The deep-market comparison only had 9 matches with real liquidity, and most rules never reached the 5-application bar. A higher-volume market or a longer season is the cheapest way to get real answers on which rules work.

**Running it again.** The auto-pilot is wound down for now. `python3 auto_pilot.py --install` restarts the 5-minute loop for the next season.

## Frozen rules of the game

[`reflection/program.md`](reflection/program.md) is frozen at season start. It defines:
- Brier score as the sole score that mutates rules
- Alphabetically-first team as the reference (removes scoring ambiguity)
- 5-application threshold before a rule can be validated
- Forward-only constraint (no retrospective matches)
- Post-toss, pre-first-ball evidence cutoff
- 8 frozen search query templates for news gathering
- what consolidation can and cannot modify

No agent and no consolidation step can change this file.

## Data sources

- **[Cricsheet](https://cricsheet.org/)** - 1,219 IPL matches, ball-by-ball, CC0 license
- **[Polymarket](https://polymarket.com/)** - public Gamma API for market-implied probabilities (no auth)
- **Web search** - team news, pitch reports, weather. The search queries are frozen in `program.md`, but the returned source set varies per match. The Source Quality Clerk rates each source's reliability and timestamp after the fact.

## FAQ

**"T20 is a super high variance game. Is it even practical to model it?"**
That was the point. I might get to the end of the season and find it's useless. But I was genuinely curious whether a self-improving AI system could learn to model T20 madness, or whether it's noise all the way down.

**"Isn't it too early to claim the model is better than prediction markets?"**
Yes, and I don't claim that. The sample is too small to conclude anything. These are early reads.

**"Why Polymarket? Why not Cricbuzz or Cricinfo?"**
A prediction market with $50-100K in real money on each match is a harder benchmark than an expert panel. Cricbuzz and Cricinfo also don't publish these probabilities in a reliable way.

**"You say zero human inputs but I see commits in the repo?"**
Code changes and bug fixes are mine. The forecasts, grades, rules, and scoring ran on their own on a VPS cron. No human reviewed a forecast before a match or approved a rule change after grading. Git history shows which commits are mine (code) and which are the auto-pilot's (output).

## What this is not

- It does not claim to beat market prices.
- It does not place, recommend, or automate trades.
- It does not interact with any trading frontend.

Polymarket's trading frontend is geo-restricted in India. This project does not interact with that interface. The public data API is queried for research only, to study how multi-agent reasoning calibrates against public market prices. See [docs/legality_note.md](docs/legality_note.md).

## License

MIT

---

Built by [Sid](https://github.com/dashthird-0) with Claude Code.
