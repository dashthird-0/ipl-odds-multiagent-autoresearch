# Frozen Evidence Discipline

## Principle

Every case study must be verifiable. A reader should be able to open any case study directory
and confirm:

1. What evidence was available before the toss
2. What the agents produced from that evidence
3. Whether any post-toss information contaminated the analysis

This makes "no hindsight" demonstrable, not just claimed.

## Implementation

### Evidence Cutoff

Each case study has an `evidence_cutoff.md` that records:
- The exact ISO8601 timestamp before which evidence is admissible
- The match date and estimated toss time
- Whether this is a forward-looking or retrospective study

### Cutoff Enforcement

**Cricket Stats Analyst:** All queries include a `cutoff_date` parameter. The query tool
filters matches strictly before this date. If the tool doesn't support date filtering,
the agent applies it manually and flags the risk.

**News & Conditions Analyst:** Receives the `evidence_cutoff` as an explicit input.
Must filter web search results by publication date. Undated sources are flagged as such.

**Market Reader:** Records the exact timestamp of the market snapshot. For retrospective
studies where live data isn't available, uses `manual_snapshot.json`.

### Source Tracking

`allowed_sources.md` lists every external source used, with:
- URL
- Publication date
- Brief description

This allows a reviewer to verify that all sources predate the evidence cutoff.

## Retrospective vs Forward-Looking

**Forward-looking** (live IPL 2026 matches):
- Evidence packet built in real-time before the toss
- Market snapshot is a live API fetch
- News is current-day press research
- Highest credibility — no hindsight possible

**Retrospective** (past matches):
- Evidence cutoff is set to pre-toss time
- Market snapshot uses `manual_snapshot.json` with documented rationale
- News research uses only sources published before cutoff
- Agent must ignore the known result
- Lower credibility (harder to guarantee no leakage), but still valuable if done carefully

## What Can Go Wrong

1. **Stats leakage:** Cricsheet data includes the match being studied → query tool must
   filter `< cutoff_date`, not `<= cutoff_date`
2. **News leakage:** A post-toss article cited as "pre-match preview" → Source Quality
   Clerk should catch undated or suspicious sources
3. **Implicit knowledge:** Agent "knows" the result from training data → this is unavoidable
   for retrospective studies of well-known matches. We acknowledge it in the README rather
   than pretending it doesn't exist. Forward-looking studies are the clean test.
4. **Market snapshot timing:** Price moved after toss announcement → for forward-looking
   studies, take the snapshot before the toss window (>30 minutes pre-toss)
