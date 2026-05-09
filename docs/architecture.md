# Architecture

## Subagent Topology

Seven specialist agents coordinated by a central orchestrator (the Claude Code session).
No subagent spawns further subagents. Communication is file-based: each agent reads
upstream outputs and writes its own output to the case study directory.

```
                    ┌─────────────────┐
                    │   Orchestrator   │
                    │  (Claude Code)   │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
     ┌────────────┐  ┌────────────┐  ┌────────────────┐
     │   Market   │  │  Cricket   │  │    News &      │
     │   Reader   │  │   Stats    │  │  Conditions    │
     │            │  │  Analyst   │  │   Analyst      │
     └─────┬──────┘  └─────┬──────┘  └───────┬────────┘
           │                │                  │
           │                │                  ▼
           │                │         ┌────────────────┐
           │                │         │ Source Quality  │
           │                │         │     Clerk      │
           │                │         └───────┬────────┘
           │                │                  │
           └────────────────┼──────────────────┘
                            │
                            ▼
                   ┌─────────────────┐
                   │   Base-Rate     │
                   │    Skeptic      │
                   └────────┬────────┘
                            │
                            ▼
                   ┌─────────────────┐
                   │   Fair Value    │
                   │  Synthesizer    │
                   └────────┬────────┘
                            │
                            ▼
                       [ MEMO.md ]
                            │
                    ════════════════
                    ║ MATCH PLAYS ║
                    ════════════════
                            │
                            ▼
                   ┌─────────────────┐
                   │   Post-Match    │
                   │     Grader      │
                   └────────┬────────┘
                            │
                            ▼
                  [ REFLECTION LOG ]
```

## Execution Sequence

**Phase 1 — Data Collection (parallel)**
- Market Reader fetches Polymarket implied probabilities
- Cricket Stats Analyst queries Cricsheet for statistical priors
- News & Conditions Analyst researches press/weather/team news

**Phase 2 — Evidence Audit (sequential)**
- Source Quality Clerk audits the News Analyst's output

**Phase 3 — Challenge (sequential)**
- Base-Rate Skeptic reads all upstream outputs and the Reflection Log
- Produces challenges and a band-width recommendation

**Phase 4 — Synthesis (sequential)**
- Fair Value Synthesizer reads everything and produces the memo
- Resolves Skeptic challenges explicitly

**Phase 5 — Grading (post-match)**
- Post-Match Grader evaluates reasoning quality
- Proposes Reflection Log entries (durable rules, not facts)

## Data Flow

All inter-agent communication is via files in the case study directory:

```
case_studies/match_NNN/
  market_snapshot.json     ← Market Reader writes
  stats_snapshot.json      ← Stats Analyst writes (via Python tool)
  news_conditions.md       ← News Analyst writes
  source_quality.md        ← Source Quality Clerk writes
  skeptic_review.md        ← Base-Rate Skeptic writes
  memo.md                  ← Fair Value Synthesizer writes
  result.md                ← Human fills after match
  post_match_grade.md      ← Post-Match Grader writes
```

The Reflection Log (`reflection/learning_log.md`) is a shared read artifact:
- Skeptic reads it to raise relevant past lessons
- Synthesizer reads it to resolve those lessons
- Grader proposes new entries
- Orchestrator (human) approves and appends entries

## Why This Architecture

- **No inter-agent messaging or revision loops.** Each agent writes once. Disagreement is surfaced
  in the Skeptic's review and resolved by the Synthesizer. This bounds cost and prevents quality collapse
  from unbounded iteration.
- **File-based communication makes audit easy.** Anyone can read the case study directory and verify
  what each agent saw and produced.
- **Frozen evidence discipline is enforced by the directory structure.** Agents can only read files
  that exist in the case study directory at their execution time.
- **The Reflection Log is the only cross-session state.** Each case study is self-contained;
  the log carries durable reasoning rules forward.
