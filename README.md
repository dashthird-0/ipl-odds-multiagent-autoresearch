# Cricket Pricing Room

A multi-agent research desk that reads public market-implied probabilities for IPL matches from [Polymarket](https://polymarket.com/), combines them with cricket statistics, team news, and match conditions, and produces probability-band memos before each match. After the match, the system grades its own reasoning and updates a Reflection Log that informs future memos.

Built with [Claude Code](https://claude.ai/code) subagents as a study in multi-agent orchestration.

## What It Does

Before a match:
- **Market Reader** fetches current implied probabilities from Polymarket's public API
- **Cricket Stats Analyst** queries [Cricsheet](https://cricsheet.org/) ball-by-ball data for statistical priors (head-to-head, venue splits, recent form, key players)
- **News & Conditions Analyst** researches team news, pitch reports, weather, and dew conditions
- **Source Quality Clerk** audits every piece of evidence for reliability (confirmed / probable / speculative)
- **Base-Rate Skeptic** attacks narrative overreach against statistical base rates
- **Fair Value Synthesizer** produces a probability-band memo

After the match:
- **Post-Match Grader** evaluates reasoning quality (not the outcome)
- Durable lessons are added to the **Reflection Log**

## Architecture

```
  Market Reader ──┐
  Stats Analyst ──┼──→ Base-Rate Skeptic ──→ Fair Value Synthesizer ──→ MEMO
  News Analyst ───┤                                                       │
       │          │                                                  [match]
  Source Clerk ───┘                                                       │
                                                               Post-Match Grader
                                                                       │
                                                              Reflection Log
```

Seven specialist agents, defined as `.claude/agents/*.md` files, coordinated by a central orchestrator. No subagent spawns further subagents. Communication is file-based: each agent reads upstream outputs and writes to the case study directory.

See [docs/architecture.md](docs/architecture.md) for the full topology and execution sequence.

## Output Format

Memos output probability bands, never point estimates:

```
Anchor price:      GT 51.5% — source: Polymarket ($112K volume)
Model band:        GT 48-56%
Directional view:  Slight GT lean, effectively a coin flip
Confidence:        Medium
Main uncertainty:  First-time captain, reconfigured bowling attack
```

## Case Studies

| Match | Date | Memo Call | Result | Grade |
|-------|------|-----------|--------|-------|
| [SRH vs PBKS](case_studies/match_retro_srh_vs_pbks/) | 2026-05-06 | SRH 53-63% (favored) | SRH won by 33 runs | A |
| [RR vs GT](case_studies/match_001_rr_vs_gt/) | 2026-05-09 | GT 48-56% (slight lean) | Pending | — |

Each case study is a self-contained evidence packet with frozen data, timestamped sources,
and a complete agent trace. See [docs/evidence_discipline.md](docs/evidence_discipline.md).

## Frozen Evidence Discipline

Every case study includes:
- `evidence_cutoff.md` — exactly what was knowable before the toss
- `market_snapshot.json` — frozen market state
- `stats_snapshot.json` — Cricsheet query results
- `allowed_sources.md` — every external source used, with URL and date
- Full agent outputs (news, source quality, skeptic review, memo, grade)

This makes "no hindsight" demonstrable, not just claimed.

## Data Sources

- **[Cricsheet](https://cricsheet.org/)** — 1,219 IPL matches, ball-by-ball, CC0 license
- **[Polymarket](https://polymarket.com/)** — public data API for market-implied probabilities (no auth required)
- **Cricbuzz / ESPNcricinfo** — team news, pitch reports (web research)
- **Weather APIs** — match-day forecasts

## Quick Start

```bash
# Build an evidence packet for an upcoming match
python3 run_memo.py RR GT "Sawai Mansingh Stadium" 2026-05-10

# Record a result and trigger grading
python3 run_grade.py case_studies/match_001_rr_vs_gt --winner "Gujarat Titans" --by "6 wickets"
```

Then open Claude Code in this directory and follow the printed instructions to run agents.

## What This Is

A learning project studying how multi-agent reasoning systems calibrate against public market prices. Built over 2-3 weekends as a portfolio piece demonstrating Claude Code's subagent orchestration.

## What This Is Not

- Does not claim to beat market prices
- Does not claim to be a better forecaster than statistical models
- Does not place, recommend, or automate trades
- Does not interact with any trading frontend
- Does not advise users to access geo-restricted interfaces
- Does not claim the probability bands are profitably tradeable

## What It Does Claim

- Multi-agent orchestration is the right tool for this specific shape of problem (genuinely different lenses that legitimately disagree)
- Claude Code's subagent primitives map cleanly to the use case
- Frozen evidence discipline makes retrospective evaluation credible
- Bands-not-points is the right calibration practice
- Honest reporting — if the system is mediocre, the case studies show it

## Disclaimer

Cricket Pricing Room reads public market-implied probabilities from Polymarket's documented public API. The system does not place trades, recommend trades, automate orders, or advise users to access restricted trading interfaces. Polymarket's trading frontend is geo-restricted in India; this project does not interact with that interface. The public market data API is queried for research purposes only — to study how multi-agent reasoning systems calibrate against public market prices.

See [docs/legality_note.md](docs/legality_note.md) for full details.

## Why Claude Code, Not Managed Agents

Claude Code's subagent system (`.claude/agents/*.md`) is first-class multi-agent orchestration. Managed Agents is for production agents — long-running, async, cloud-hosted. This project is manually triggered, runs locally, and ships from a weekend scope. The Reflection Log approximates Managed Agents' dreaming primitive honestly.

See [docs/claude_code_vs_managed_agents.md](docs/claude_code_vs_managed_agents.md).

## Prior Work

This project is aware of and distinct from:
- [Polyseer](https://github.com/Polyseer) — Polymarket analysis tools
- [TradingAgents](https://github.com/TauricResearch/TradingAgents) — multi-agent financial trading
- [Polymarket Agents](https://github.com/polymarket) — official Polymarket tooling

None of these cover IPL-specific multi-agent reasoning with frozen evidence discipline.

## License

MIT

---

Built by [Sid](https://github.com/siddharth) with Claude Code.
