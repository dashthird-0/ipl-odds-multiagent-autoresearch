# Claude Code vs Managed Agents

## Why Claude Code for This Project

This project uses Claude Code's first-class subagent system (`.claude/agents/*.md` files)
rather than Anthropic's Managed Agents API.

### What Claude Code Subagents Provide

- Separate agent definitions with distinct system prompts and tool restrictions
- Orchestrator-worker patterns with file-based communication
- Parallel and sequential execution via the Agent tool
- Full local development loop (edit, test, iterate in one session)
- No additional cost beyond the Claude Code subscription

### What Managed Agents Would Add

- **Dreaming:** Long-running async background processing that consolidates reasoning
  across many sessions. This is the single feature we'd genuinely use.
- **Persistent cloud containers:** For always-on agents. Not needed here (manual trigger).
- **Massive parallelism:** For scaling to hundreds of concurrent tasks. Not needed here
  (5-10 case studies, sequential).
- **Server-side session state:** For agents that run across days. Not needed here.
- **Outcomes tracking:** For production-grade evaluation. Nice but not essential for v1.

### Cost Comparison

| | Claude Code (Pro/Max) | Managed Agents |
|---|---|---|
| Billing | Subscription (flat) | API tokens + $0.08/session-hour |
| Estimated cost for this project | ~$0 marginal | $100-400 |
| Setup complexity | Already configured | API integration needed |

### The Honest Assessment

Managed Agents exists for **production agents** — long-running, async, scaled, persistent.
This project is a **weekend research artifact** — manually triggered, 5-10 runs, local-only.

The only Managed Agents primitive that would genuinely improve this project is **dreaming** —
the ability to consolidate reasoning patterns across many sessions without explicit
prompting. We approximate this with the Reflection Log, which is honest but manual.

### Future Work

If this project were extended (v2):
- Migrate to Managed Agents for the Reflection Log → dreaming replacement
- Use outcomes tracking for automated Brier score computation
- Run forward-looking memos as scheduled background agents before each match

For v1, Claude Code subagents are the right tool. The architecture is the same regardless
of runtime — the agents, their prompts, and their communication patterns would transfer
directly to Managed Agents if migrated.
