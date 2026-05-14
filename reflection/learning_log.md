# Reflection Log

Durable reasoning rules learned from post-match grading. Each entry captures a pattern,
not a fact. Facts go stale; rules endure.

Format: When [pattern], [do/don't do X] because [evidence from grading].

---

## Entry 1 — from Exp 1: RR vs GT (2026-05-09), Grade: C+

**When** structural priors (home advantage, chase advantage) are contradicted by the same
team's recent results at the same venue in the same season, **discount** the structural prior
by at least 50% rather than treating the contradiction as "unresolvable noise."
**Because:** RR had lost both 2026 home matches at Sawai Mansingh (one conceding a 226 chase),
yet the memo applied generic +6pp home advantage. Two data points showing the same pattern
is weak individually but strong against a generic base rate. False balance produces memos
that are technically defensible but practically uninformative.

**Status:** tentative | **Applications:** 5 (Exp 3: RCB vs MI — rule applied; Chinnaswamy venue data correctly excluded from Raipur analysis; the extreme case where venue priors were not merely contradicted but entirely inapplicable. Exp 4: PBKS vs DC — rule applied; PBKS's 6-8 Dharamsala record used to negate home advantage; PBKS lost again, extending to 6-9. Exp 5: GT vs SRH — Skeptic checked Entry 1 and correctly found no contradiction; GT's 3-2 NMS record supported standard home advantage. Entry 1 was consulted but NOT triggered — a correct non-application. Exp 6: RCB vs KKR — Skeptic correctly applied Entry 1: RCB's win at Raipur 3 days prior overrode the "slow pitch hurts aggressive batting" narrative. RCB chased 193 comfortably, validating the application. Exp 7: PBKS vs MI — Entry 1 was invoked for the wrong venue. The memo applied it to Mullanpur (6-8 overall, 3-1 in 2026), concluding "moderate home advantage." The match was at Dharamsala, where PBKS's record is 6-9 (extended to 6-10 with this loss). At the correct venue, Entry 1 would have found NO contradiction — the structural prior (home disadvantage) is consistently supported. The lesson: Entry 1's framework is sound, but it requires correct venue identification upstream. See Entry 13.)

## Entry 2 — from Exp 1: RR vs GT (2026-05-09), Grade: C+

**When** a team has a clear bowling quality advantage AND the opposing team has lost its
primary spin bowler, **treat** the compound effect as multiplicative (raising the probability
of a high first-innings score), not merely additive.
**Because:** GT's elite batting (Gill, Sudharsan, Buttler all 149+ SR) attacked RR's bowling
minus Bishnoi (replaced by untested Punja). The memo treated these as independent +2-3pp
factors when the interaction shifts the entire first-innings scoring distribution upward,
activating the conditional bowling advantage. GT posted 229, well above the 185 threshold
the memo itself identified as the tipping point.

**Status:** tentative | **Applications:** 1 (Exp 3: RCB vs MI — rule referenced in memo; Bhuvneshwar's 4/23 validated that bowling quality gap was the strongest signal; MI posted 166 not 200+ because of this compound effect)

## Entry 3 — from Exp 3: RCB vs MI (2026-05-10), Grade: B

**When** key opposition personnel are uncertain (injury doubt, game-time decision), **model**
the actual likely replacement XI and assess its bowling/batting quality separately — do not
rely on season averages that include the absent player.
**Because:** The memo compared RCB's bowling against MI's season stats (Shardul Thakur 11.63
economy, Pandya 10.74 economy), but neither Thakur nor Pandya played. The actual MI bowling
unit (Bumrah 5.00, Chahar 8.25, Bosch 6.50) was materially stronger than the stats suggested,
while the replacement all-rounder (Bawa, 13.00 economy) was materially weaker. The memo's
bowling comparison described a lineup that didn't take the field, missing both MI's bowling
competitiveness and Bawa's death-overs vulnerability.

**Status:** tentative | **Applications:** 4 (Exp 4: PBKS vs DC — rule applied to DC but not reciprocally to PBKS. DC's replacement XI was flagged as an uncertainty, but PBKS's own surprise change — Ferguson out, Dwarshuis debut — was not modeled. Additionally, the rule needs extension: replacement XIs should be assessed for BOTH ceiling and floor, not assumed to be a downgrade. DC's 5 changes produced a team that won. Exp 5: GT vs SRH — rule correctly applied to Travis Head's impact sub status. The memo assessed SRH's starting XI without Head and noted it was weaker than aggregate stats. Head was used as impact sub and scored 0(4). However, the rule was applied asymmetrically again: GT's impact sub Prasidh Krishna 2/23 was not equivalently modeled. Exp 6: RCB vs KKR — Salt's absence correctly modeled with Bethell replacement. Varun's injury correctly flagged as uncertainty with conditional adjustment. However, the actual XI surprises (Venkatesh Iyer in, Suyash Sharma out, Jacob Duffy in) were not anticipated, leading to fragile matchup analysis. See new Entry 12. Exp 7: PBKS vs MI — the asymmetric application pattern recurred for the fourth time. MI's XI uncertainty was correctly flagged as "the largest unresolved variable," but PBKS's own rotation (Stoinis dropped, Ferguson out, Bartlett in for Vyshak) was not anticipated or modeled. Stoinis was PBKS's 5th-highest run scorer (178 runs, SR 174.5) — his absence materially weakened batting depth. This is now a persistent bias: the memo models opposition uncertainty thoroughly but assumes the favored team will field their expected XI.)

## Entry 4 — from Exp 3: RCB vs MI (2026-05-10), Grade: B

**When** building batting depth profiles for a team, **include** all-rounders' batting records
explicitly, not just the top-5 run scorers from the stats snapshot.
**Because:** Krunal Pandya appeared only in RCB's bowling stats (10 wickets, 8.54 economy).
His 73(46) was the match-winning innings, rescuing RCB from 39/3. The memo named Kohli,
Patidar, and Padikkal as the key batting depth — all three failed (0, 8, 12). The systematic
exclusion of all-rounders from batting analysis creates blind spots for exactly the kind of
lower-order rescue innings that decide close matches.

**Status:** tentative | **Applications:** 0

## Entry 5 — from Exp 2: CSK vs LSG (2026-05-10), Grade: B+

**When** a player returning from injury is confirmed in the playing XI at toss, **do not**
treat the injury as a directional vulnerability or scenario-driver.
**Because:** The memo flagged "Inglis fails early due to thumb injury" as a scenario pushing
CSK toward 60-63%. Inglis was confirmed by Pant at toss and scored 85(33) — the most explosive
innings of the match. Team selection implies medical clearance by physios who have examined
the player. Once in the confirmed XI, discount injury-based performance concerns by at least
75%; reserve injury adjustments for genuine game-time decisions (player not yet selected).

**Status:** tentative | **Applications:** 0

## Entry 6 — from Exp 2: CSK vs LSG (2026-05-10), Grade: B+

**When** a venue has a high average first-innings score in the current season, **calibrate**
conditional scoring thresholds against the venue's scoring environment, not against a generic
difficulty standard.
**Because:** Chepauk's 2026 average first innings was 186 runs. The memo treated "LSG posts
190+" as shifting the band toward a coin-flip (CSK 50-55%). LSG posted 203/8 and CSK chased
it down with 5 wickets and 4 balls to spare, powered by Urvil Patel's 65(23). The same flat
conditions that enabled LSG's 200+ also enabled CSK's chase. A high total on a high-scoring
pitch is a different signal than a high total on a deteriorating surface. Conditional scenarios
must account for symmetry: if conditions help the batting-first team exceed par, they likely
help the chasing team too.

**Status:** tentative | **Applications:** 1 (Exp 4: PBKS vs DC — rule applied via Skeptic's pace symmetry challenge. However, the scoring environment lesson was partially missed: the memo discounted the "209 since 2023" average as distorted, but the actual first innings was 210/5, closer to the recent figure. The symmetry principle held — DC chased 211 successfully.)

## Entry 7 — from Exp 4: PBKS vs DC (2026-05-11), Grade: B+

**When** a captain publicly concedes the season and hints at lineup rotation, **model** the
replacement XI for both ceiling and floor — do not assume rotation equals a unilateral
downgrade.
**Because:** Axar Patel said "next year will come too" and hinted at giving bench players
chances. The memo's scenario assumed "3+ changes = rotation over competition = PBKS band
moves up 2-3pp." DC made 5 changes and WON — by 3 wickets with an over to spare. The
replacements included David Miller (51 off 28, proven finisher) and Madhav Tiwari (2/40 +
18* on IPL bowling debut). Dead-rubber rotations can produce a stronger XI (fresh legs, no
pressure, players auditioning for retention) just as easily as a weaker one. The "rotation =
weakness" assumption is a systematic bias. Assess the replacement players' individual quality
and the absence-of-pressure advantage, not just the fact of rotation.

**Status:** tentative | **Applications:** 2 (Exp 5: GT vs SRH — rule applied. DC's 5-change rotation was an extreme case; in Exp 5, GT's bowling ceiling was the dominant factor regardless of total posted. The principle that replacement/rotated XIs should be assessed for ceiling as well as floor is validated. Exp 7: PBKS vs MI — rule correctly applied. The memo explicitly dismissed the dead-rubber motivation narrative: "no probability adjustment for MI's 'lack of motivation.'" MI — virtually eliminated, missing captain Pandya and vice-captain SKY, with Rohit as impact sub — won by 6 wickets. This is the third consecutive validation that dead-rubber teams are unpredictable, not systematically weaker.)

## Entry 8 — from Exp 4: PBKS vs DC (2026-05-11), Grade: B+

**When** the Skeptic's base-rate analysis diverges from the market by 3+pp and the memo's own
analysis supports the Skeptic's direction, **lean toward the base-rate estimate** rather than
splitting the difference with the market.
**Because:** The market had PBKS at 60.5%. The Skeptic's midpoint was 54-55%. The memo
compromised at ~55%, siding mostly with the Skeptic but still 5.5pp below the market. DC won.
The gap was explained by specific, identifiable anchoring biases: full-season record vs
recent form (PBKS 4-4 in last 8), generic home advantage vs venue-specific record (PBKS 6-8
at Dharamsala). "Deep liquidity" is a weak argument for market efficiency when the divergence
is explained by concrete analytical findings. When your own analysis produces a consistent
reason for the gap, trust the analysis over the market anchor.

**Status:** tentative | **Applications:** 3 (Exp 5: GT vs SRH — Entry 8 correctly applied. The memo placed GT at 55% vs market's 45.5%, a 9.5pp contrarian gap explained by toss overpricing, H2H dominance, and bowling quality. GT won by 82 runs. The base-rate estimate was more accurate than the market. Exp 6: RCB vs KKR — Entry 8 applied again: memo placed RCB at 54% vs market's 57.5%, a 3.5pp lean BELOW the market. RCB won by 6 wickets. The contrarian direction was against RCB, and RCB won — a mixed result. The memo attributed the market's premium to "anchoring and name recognition," but table position and Kohli's match-winning century (105*) suggest the premium reflected real factors. Entry 8's principle remains sound, but the attribution of WHY the market diverges matters: when the gap is explainable by cognitive biases, lean strongly away; when explainable by verifiable strengths, lean more modestly. Exp 7: PBKS vs MI — Entry 8 applied correctly in direction. The memo placed PBKS at 57% vs market's 61.5%, a 4.5pp lean toward MI. MI won. The lean was directionally correct but insufficiently aggressive — the base-rate analysis (H2H 17-17, home disadvantage, dead-rubber dismissal) pointed closer to 50-53% PBKS, not 57%. Three consecutive applications now show that when Entry 8 fires, the contrarian direction has been correct every time, but the magnitude of the lean could be bolder.)

## Entry 9 — from Exp 5: GT vs SRH (2026-05-12), Grade: A-

**When** same-day weather data contradicts a venue's generic "dew advantage" narrative AND the
venue-level field-first win rate is ≤50%, **cap** the toss adjustment at 0pp and treat any
market swing >2pp as overpricing the toss.
**Because:** At NMS the field-first win rate was 50% (15/30, 2023-2026). Same-day humidity was
11-20% with a 23C dew-point gap (evening temp 33-34C, dew point 6-10C). The market moved 4pp
toward SRH post-toss. SRH chose to field and lost by 82 runs. The "significant dew" narrative
from the Times of India preview was unsupported by the weather API data. Venue-specific toss
data combined with same-day weather is more informative than generic evening dew narratives.
This is the strongest case in the experiment series of the market systematically overpricing
a toss.

**Status:** tentative | **Applications:** 1 (Exp 6: RCB vs KKR — Entry 9 was partially applicable but conditions differed. Raipur humidity was moderate (29% rising to 61%), dew-point gap ~15-20C at match start. The memo correctly capped the toss adjustment at +3-5pp. The chasing team (RCB) won, consistent with a moderate — not extreme — toss advantage. Unlike Exp 5 where weather data contradicted the dew narrative, here the weather was ambiguous, and the correct response was a bounded toss adjustment rather than a 0pp cap.)

## Entry 10 — from Exp 5: GT vs SRH (2026-05-12), Grade: A-

**When** a team's H2H dominance at a specific venue is ≥3-0 across different toss outcomes and
years, **weight** it at the upper end of the +5-8pp adjustment range — opponent squad
improvements reduce but do not eliminate the prior.
**Because:** GT's 3-0 at NMS (including 2 matches where SRH chose to field first) extended to
4-0. SRH's 2026 batting lineup — arguably their strongest ever (Abhishek SR 188.5, Ishan SR
181.0, Klaasen SR 149.2, plus Head available as impact sub) — was bowled out for 86. The market
had SRH at 54.5%, pricing as if the squad upgrade overrode the venue H2H. Venue-specific H2H
captures persistent dynamics (bowling attack vs batting style, pitch familiarity, crowd effect)
that survive opponent squad upgrades more than market participants typically expect. Small
samples (3-4 matches) at a specific venue are more informative than they appear when the pattern
is consistent across varying conditions (different toss outcomes, different years, different
squad compositions).

**Status:** tentative | **Applications:** 0

## Entry 11 — from Exp 6: RCB vs KKR (2026-05-13), Grade: B+

**When** a venue's match sample spans multiple IPL eras (e.g., 2014-2015 and 2026), **segment**
the scoring norms by era rather than blending them into a single average — and treat the
recent-era subset as more informative than the blended figure.
**Because:** Raipur's 7-match blended average was ~149. Five of those matches were from 2014-2015
(avg ~140); the two 2026 matches averaged ~180. KKR scored 192/4 — the highest-ever Raipur IPL
total, 43 runs above the cited average. T20 batting has evolved dramatically across eras: ball
composition, power-hitting depth, strategic intent, and squad quality have all shifted scoring
norms upward. A blended average that weights 2014-2015 equally with 2026 systematically
underestimates modern run-scoring. The memo treated ~149 as directionally informative for pitch
characterization and par score, but the era gap rendered it misleading. When most of a venue's
sample is from a prior era, acknowledge the era gap explicitly and anchor on the recent subset.

**Status:** tentative | **Applications:** 0

## Entry 12 — from Exp 6: RCB vs KKR (2026-05-13), Grade: B+

**When** playing XIs are unconfirmed at memo time, **do not** build detailed tactical matchups
(bowler X vs batter Y, spin attack comparisons) around predicted XIs — instead model overall
team quality and note that specific matchups are contingent on selection.
**Because:** The memo built significant reasoning around Suyash Sharma vs Narine/Varun as the
spin battle on a "spin-friendly" Raipur surface. In the event: Suyash Sharma was not selected
(replaced by Jacob Duffy, a pacer), Varun Chakravarthy was ruled out with injury, and the
surface played faster than expected. The Source Quality Clerk had explicitly rated all predicted
XIs as "speculative with known disagreements," but the memo still invested analytical space in
matchups that required those predictions to hold. Detailed matchup analysis creates fragile
reasoning that collapses if 1-2 selections differ. Reserve it for post-toss memos with confirmed
XIs; pre-toss memos should focus on team-level bowling/batting quality indices that are robust
to individual selection changes.

**Status:** tentative | **Applications:** 1 (Exp 7: PBKS vs MI — rule correctly applied. The memo explicitly cited Entry 12 and refused to build detailed matchups against MI's unconfirmed XI: "I assess team-level quality only." MI's actual XI differed significantly from the last known XI (Pandya out, SKY out, Rohit demoted to impact sub, Thakur returned). Had the memo built matchups around the May 4 XI, they would have collapsed. This is the strongest validation yet of Entry 12.)

## Entry 13 — from Exp 7: PBKS vs MI (2026-05-14), Grade: C+

**When** the pipeline assigns a venue to a match, **verify** the venue proactively against an
authoritative source (IPL fixture list, official team announcement, or multiple independent
press references) rather than relying on the absence of contradicting evidence.
**Because:** The Exp 7 memo analyzed PBKS vs MI as occurring at Maharaja Yadavindra Singh
International Cricket Stadium (Mullanpur/New Chandigarh). The match was actually played at HPCA
Stadium, Dharamsala. Every venue-specific data point — scoring norms (214.2 avg), toss impact
(66.7%), chase splits, PBKS's "3-1 in 2026" home record — was for the wrong ground. No agent
detected the discrepancy because the pipeline's venue-checking is reactive (catches contradictions
in sourced evidence) rather than proactive (independently verifies venue). In Exp 6, the venue
error was caught because the news agent surfaced a direct contradiction; here, no source within
the evidence window mentioned the correct venue, so the error propagated through all agents
unchecked. A single proactive verification step would have prevented the most consequential
analytical error in the experiment series.

**Status:** tentative | **Applications:** 0

## Entry 14 — from Exp 7: PBKS vs MI (2026-05-14), Grade: C+

**When** a team's losing streak extends beyond 3 matches and includes at least one home loss
or loss to a clearly weaker team, **increase** the momentum adjustment to -3-5pp (not -1-2pp)
and treat the streak as evidence of genuine decline rather than contextual noise.
**Because:** PBKS entered the match on a 3-match losing streak. The memo adjusted only -1-2pp,
reasoning that all losses were "to top-4 teams, mostly away." PBKS then lost their 4th straight — a home loss to dead-rubber MI (8th place, missing Pandya and
SKY). The contextual explanation ("strong opponents away from home") was invalidated by the home
loss to a weakened team. Streaks that cross 3+ games signal something beyond bad scheduling:
confidence erosion, tactical predictability, or structural issues that the opponent-quality
adjustment cannot explain. When the losing-streak context includes mixed conditions (some home,
some away, varying opponent strength), the streak itself becomes the signal.

**Status:** tentative | **Applications:** 0
