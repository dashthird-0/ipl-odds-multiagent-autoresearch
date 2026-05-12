# Post-Match Grade: Royal Challengers Bengaluru vs Mumbai Indians
## 2026-05-10, Shaheed Veer Narayan Singh International Stadium, Raipur

**Result:** Royal Challengers Bengaluru won by 2 wickets (off the last ball)
**Memo directional view:** RCB slightly favored. Season quality gap is the strongest signal; toss+dew gives a moderate chasing edge; RCB bowling materially superior; venue is a complete unknown.
**Band:** 52-62% RCB / 38-48% MI — Result **inside band** (RCB won, but barely — a last-ball finish is consistent with a close, low-confidence matchup)

## Reasoning Grade: B

### What the memo got right

- **Bhuvneshwar Kumar was correctly identified as the key bowling edge, and he was the decisive player.** The memo named "Bhuvneshwar Kumar (17 wickets, 7.46 economy)" as the linchpin of RCB's bowling superiority over MI. Bhuvneshwar delivered 4/23 at an economy of 5.75, won Player of the Match, and then hit the six in the final over that swung the chase. The bowling quality gap was the memo's strongest qualitative claim, and it was validated decisively.

- **The directional call was correct.** The memo favored RCB at 52-62%, the market had RCB at 55.5%, and RCB won. The midpoint of the band (~57%) implied a close match, and a last-ball 2-wicket win is exactly the kind of margin consistent with a ~57/43 probability split. The band width (10pp) was appropriately wide given the venue uncertainty.

- **The toss+dew analysis was well-calibrated.** The memo correctly identified the toss win as a +2 to +5pp advantage, correctly dismissed the 4/6 Raipur chase rate as statistically meaningless (n=6, decade-old), and relied on IPL-wide toss/dew base rates. RCB chose to bowl (as all sources predicted), chased, and won — but the chase was agonizing (167/8 off 20 overs), suggesting the dew advantage was real but not overwhelming.

- **Pandya/SKY availability was handled with appropriate uncertainty.** The memo treated Pandya as "game-time decision" and SKY as "very likely but not confirmed." The actual resolution — Pandya OUT, SKY played but captained and scored a golden duck (0 off 1 ball) — validated the memo's framework. The Skeptic's challenge that "Pandya's 2026 form does not support treating his absence as a major MI disadvantage" was prescient: Pandya's absence did not prevent MI from posting a competitive 166/7, and his replacement (Raj Angad Bawa) contributed 16 runs and took a wicket.

- **The venue data void was correctly identified and handled.** The memo's strongest analytical contribution was recognizing that stats_snapshot.json contained Chinnaswamy data for a Raipur match, and entirely excluding it. The Evidence Quality Note explicitly stated "stats_snapshot.json venue splits are for M Chinnaswamy Stadium (the WRONG venue) and have been entirely excluded." This prevented a data contamination error that could have fundamentally distorted the analysis. The Skeptic reinforced this with an explicit "DO NOT use the Chinnaswamy venue splits" directive.

- **The pitch uncertainty was correctly framed as the main unknown.** The memo identified historical Raipur average of 146 vs pundit expectations of 180-190 as an unresolvable gap. The actual first-innings score of 166 landed almost exactly between these two anchors, confirming neither was reliable and the memo was right to avoid committing to either.

### What the memo got wrong

- **The memo under-weighted MI's bowling quality in specific conditions.** While correctly identifying RCB's bowling superiority as the strongest signal, the memo gave insufficient attention to the possibility that MI's bowling could be competitive on the right surface. Corbin Bosch (4/26) and Deepak Chahar (2/33) were excellent; Bumrah conceded only 20 runs from 4 overs. RCB were 39/3 and later 131/6 and 157/8 — nearly losing from a position where they were chasing only 167. The memo treated MI's bowling as uniformly leaky (citing Shardul Thakur's 11.63 economy and Pandya's 10.74), but Thakur didn't play and Pandya was absent. The actual MI bowling unit that took the field — Bumrah, Chahar, Bosch, Ghazanfar — was significantly stronger than the one the memo analyzed. This is a lesson: when key personnel are uncertain, the analysis must model the actual likely XI, not just reference season averages that include players who may not feature.

- **Salt's absence was correctly identified but Bethell's contribution was under-predicted.** The memo cited Bethell's scores of 14, 20, 5, 4 and treated his inclusion as a "genuine downgrade." Bethell scored 27(27) — his best innings of the season — suggesting the memo may have been too anchored to a small sample of four previous outings. The broader point (Salt's absence is priced in, RCB went 2-2 without him) was correct, but the per-innings downgrade was overstated.

- **Krunal Pandya was entirely absent from the key analysis.** The memo named Kohli (379 runs), Patidar (318 runs), and Padikkal (316 runs) as the batting depth that would capitalize on MI's leaky bowling. None of them delivered: Kohli 0(1), Padikkal 12(11), Patidar 8(8). Instead, Krunal Pandya's 73(46) — listed only as a bowler (10 wickets, 8.54 economy) in the stats — was the match-winning innings. The memo did not identify Krunal as a batting threat. This is partially forgivable (Krunal's primary role is bowling), but it highlights a gap: all-rounders' batting contributions are systematically underweighted when they appear only in the bowling stats tables.

### What was missed

- **The compound effect of Pandya's absence on MI's bowling composition was under-analyzed.** The memo and Skeptic both noted that Pandya's bowling had been poor (10.74 economy), so his absence "may not weaken MI's bowling." But this framing missed the structural consequence: without Pandya, MI played Raj Angad Bawa as the replacement all-rounder. Bawa bowled 3 overs for 39 runs (economy 13.00) in the death — significantly worse than even Pandya's poor season average. The memo correctly identified that Pandya's absence had compound effects on "batting depth and captaincy" but did not trace the bowling composition chain: Pandya out → replacement all-rounder in → that replacement's bowling quality matters.

- **The "must-win" motivational factor was correctly dismissed by the Skeptic, and MI's performance confirmed this.** MI posted 166/7 and nearly defended it — this is a team performing at roughly their true ability, not one collapsing under pressure or rising to the occasion. The Skeptic's verdict ("no robust evidence that must-win situations systematically affect performance") was validated.

- **The memo did not model the scenario where RCB's top order collapses despite chasing a modest total.** RCB were 39/3 in the 7th over chasing 167 — a realistic scenario given Bumrah's presence and the unfamiliar pitch. The "What Would Change This View" section discussed high-scoring and low-scoring pitch scenarios but did not consider the possibility that even a modest MI total could challenge RCB if their top order misfired. In a ~57/43 match, the 43% scenario matters — and it nearly materialized.

### Skeptic Assessment

The Skeptic's work was excellent in this match — arguably the strongest component of the entire evidence chain.

**Strengths:** (1) The venue data exclusion was the single most important analytical decision, and the Skeptic was emphatic about it ("DO NOT use the Chinnaswamy venue splits"). (2) The dismissal of H2H records ("different squads, wrong venue") prevented a false signal that favored MI. (3) The toss+dew challenge was perfectly calibrated: the Skeptic accepted it as real (+2 to +5pp) while blocking the inflated 4/6 Raipur rate. (4) The Pandya challenge was validated — his absence was not the disaster the narrative suggested. (5) The "momentum" dismissal (RCB losing streak, MI's recent win) was correct: RCB won despite their "bad momentum" and MI lost despite their "good momentum."

**Weakness:** The Skeptic's anchoring table arrived at RCB 54-60% with a midpoint of ~57%. The market was at 55.5%. The Skeptic noted the market "sits within the base-rate range, at the low end" and flagged a possible contrarian case for RCB being underpriced. But the final recommendation — effectively "the market is about right" — was conservative when the Skeptic's own analysis suggested the market might be 1.5-2pp low. A more assertive read of the Skeptic's own evidence would have pushed the band center to 57-58% rather than letting it drift toward the market anchor.

### Decisive Factor

Bhuvneshwar Kumar's 4/23 restricted MI to 166/7 on a surface that could have yielded more, and Krunal Pandya's 73(46) rescued RCB from 39/3 — an innings the memo did not anticipate from him. The memo's core thesis (RCB's bowling superiority is the key differentiator) was correct in the first innings and became the decisive factor. However, the match was far closer than a simple "better team won" narrative suggests: RCB needed a last-ball scramble, and the outcome turned on a fumble by Bawa at mid-on.

## Lessons for Reflection Log

- **When key opposition personnel are uncertain (e.g., Pandya doubtful), model the ACTUAL likely replacement XI and its bowling/batting quality — not just the season averages that include the absent player.** MI's bowling in this match (Bumrah, Chahar, Bosch, Ghazanfar, Bawa) was structurally different from the season averages that included Shardul Thakur and Pandya. The memo's bowling comparison was stale because it described a lineup that didn't take the field. Modeling the replacement XI would have flagged that MI's bowling could be competitive (Bumrah + Chahar + Bosch) while their death bowling would be vulnerable (Bawa's high economy).

- **All-rounders who appear in stats tables as bowlers may have match-winning batting upside that is invisible in the standard analysis framework.** Krunal Pandya was listed only in RCB's bowling stats (10 wickets, 8.54 economy). His 73(46) was the match-winning innings. When building batting depth profiles, include all-rounders' batting records explicitly, not just the top-5 run scorers from the stats snapshot.
