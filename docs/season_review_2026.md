# Season review: IPL 2026

The system ran the full IPL 2026 season on a VPS with no human in the loop for any forecast, grade, or rule change. 23 matches, May 9 to May 31. Every pre-match band, every Brier score, every rule mutation happened on a cron. I fixed code and chased bugs. I never touched a forecast.

Here is what came out of it.

## The numbers

Final mean Brier was 0.242. Coin flip is 0.25. So the model beat the baseline by 0.008 across 23 matches.

That is a thin margin and I want to be honest about how thin. 0.008 over 23 matches is not a result you would build a season around. It is directionally positive and nothing more.

Band coverage was 91% (21 of 23 outcomes fell inside the model band). The two misses were PBKS vs MI and SRH vs RR, which were also the two worst-scored matches of the season (0.325 and 0.336). When the band was wrong, it was wrong on the matches where an underdog won outright. That is exactly where a probability model should expect to bleed.

Calibration improved over the season. The first 12 matches averaged 0.255. The last 11 averaged 0.227. That drift lines up with the rule library maturing, but at this sample size I cannot separate "the rules got better" from "the back half had more predictable matches."

## Did it match the market?

This was the real question, so I scored Polymarket's implied probabilities with the same Brier function on the same matches.

On the 17 matches with a liquid market, the model and the market were indistinguishable: 0.237 model versus 0.241 market. On the 9 deepest markets, the market edged the model: 0.244 versus 0.253.

One caveat on the market's raw average. Thin markets wreck it. A $25 market on CSK vs SRH resolved against the model and ate a 0.933 Brier by itself, which drags the market's unfiltered mean up and flatters the model by comparison. Once you drop the junk markets and compare like for like, the deep market is at least as sharp as the model, and slightly sharper on the matches where the most money was down.

So, no free lunch. The multi-agent system matched the deep market's calibration and found nothing the deep market missed. Both were capped by the same thing: T20 is high variance, and no amount of reasoning collapses a coin flip into a certainty.

## What the loop actually learned

The autoresearch loop generated 32 rules over the season. Three validated, two deprecated, the rest stayed tentative. Most rules never reached the 5-application threshold that consolidation needs before it acts. At 23 matches there was not enough evidence per rule.

The three that validated:

- **Bowling gaps compound, they do not add** (entry_2). When one side has a clear bowling-quality advantage and the other has lost its frontline spinner, the two effects multiply rather than stack. It first fired when GT posted 229 against a Bishnoi-less Rajasthan attack.
- **Fade the must-win premium** (entry_20). A team that is must-win and on a 3+ match losing streak is not a team playing with desperation-fuelled intensity. The streak amplifies the negative. When the market prices must-win as a positive, it tends to be wrong.
- **Take the end of the range the evidence favours** (entry_25). When the Skeptic hands the Synthesizer a range and the evidence inside that range leans one way, the memo should take the leaning end. Left neutral, memos default to the midpoint and quietly wash out the signal.

The two rules that got cut are more interesting than the three that stuck.

entry_11 said to segment a venue's scoring history by era instead of blending 2015 and 2026 into one average. That rule was correct. Era gaps were real and large all season (30 to 69 runs between the stale blended average and the actual first-innings score). It still got deprecated, because the matches it touched happened to score worse than the season average and the ratchet only reads Brier.

That is the v1 limitation in one example. The system prunes on outcome, not on reasoning. A rule can be right about cricket and still get cut for being attached to unlucky matches. I built it that way on purpose (Brier is the one thing the machine can compute without me in the loop), but the season made the cost of that choice concrete.

## What broke

Twelve production bugs in the first two days. All fixed, then it ran clean to the end.

The instructive ones: `--dry-run` was silently writing state before I caught it (twice), a lock-file race let two cron instances score the same match and grew the scorecard to 82 duplicate rows, and the band parser inverted a prediction whenever the team was named by abbreviation (CSK 58% got scored as CSK 42%). Each one is in [handoff.md](handoff.md) with its fix. Autonomous means every failure mode is yours to find.

## Next steps

**A reasoning-validity gate.** Brier-only pruning is the known hole, and entry_11 is the proof. A second signal that scores whether a rule's logic held, separate from whether its match won, would stop the loop from cutting correct rules for unlucky reasons. This is the main v2 item.

**More volume.** The deep-market comparison had an n of 9. Rules needed applications the season could not supply. A higher-liquidity market, or simply more matches, is the cheapest way to get real answers on which rules work.

**Re-running.** The auto-pilot is wound down (both crons removed). `python3 auto_pilot.py --install` re-adds the 5-minute loop for the next season. The 30-minute snapshot cron is added back by hand (line in [handoff.md](handoff.md)).
