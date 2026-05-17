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

**Status:** tentative | **Applications:** 8 (Exp 3: RCB vs MI — rule applied; Chinnaswamy venue data correctly excluded from Raipur analysis; the extreme case where venue priors were not merely contradicted but entirely inapplicable. Exp 4: PBKS vs DC — rule applied; PBKS's 6-8 Dharamsala record used to negate home advantage; PBKS lost again, extending to 6-9. Exp 5: GT vs SRH — Skeptic checked Entry 1 and correctly found no contradiction; GT's 3-2 NMS record supported standard home advantage. Entry 1 was consulted but NOT triggered — a correct non-application. Exp 6: RCB vs KKR — Skeptic correctly applied Entry 1: RCB's win at Raipur 3 days prior overrode the "slow pitch hurts aggressive batting" narrative. RCB chased 193 comfortably, validating the application. Exp 7: PBKS vs MI — Entry 1 was invoked for the wrong venue. The memo applied it to Mullanpur (6-8 overall, 3-1 in 2026), concluding "moderate home advantage." The match was at Dharamsala, where PBKS's record is 6-9 (extended to 6-10 with this loss). At the correct venue, Entry 1 would have found NO contradiction — the structural prior (home disadvantage) is consistently supported. The lesson: Entry 1's framework is sound, but it requires correct venue identification upstream. See Entry 13. Exp 8: LSG vs CSK — Entry 1 correctly triggered. LSG's 0W-3L in clear results at Ekana in 2026 produced 0pp home advantage. LSG won, making it 1W-3L, but the 0pp call remains valid: a team winning at ~45-50% implied probability at home is consistent with no home advantage. Exp 9: KKR vs GT — Entry 1 correctly triggered. KKR's 1W-2L at Eden Gardens in 2026 reduced home advantage to +1-2pp. KKR won via Allen's explosive 93(35), not venue familiarity — posting 247 anywhere would win most matches. The discount remains appropriate. Exp 10: PBKS vs RCB — Entry 1 correctly triggered. PBKS 0-2 at Dharamsala in 2026, home advantage capped at +0-2pp. PBKS then lost a third consecutive Dharamsala match, extending to 0-3 in 2026 and 6-11+ all-time. Collapsed to ~3/3 in the powerplay chasing 222. The 0-3 pattern at one venue in one season now exceeds "discount by 50%" territory — consider 0pp or negative home advantage when a team has lost 3+ consecutive home matches at the same venue in the same season. Exp 11: DC vs RR — Entry 1 applied to discount DC's 6-3 venue H2H vs RR based on DC's 1-6 overall home record in 2026. DC then WON — extending the H2H to 7-3. This reveals a scope limitation: Entry 1's "same-team, same-venue" discount was designed for when a team's general home results contradict the structural prior. But DC's 1-6 was against SIX DIFFERENT opponents. The venue H2H (DC vs RR specifically) captures a persistent matchup dynamic that the general home record doesn't address. Entry 1's discount should be REDUCED (to ~25% rather than 50%+) when the "contradicting" evidence comes from games against different opponents than the specific H2H opponent. See new Entry 21.)

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

**Status:** tentative | **Applications:** 5 (Exp 4: PBKS vs DC — rule applied to DC but not reciprocally to PBKS. DC's replacement XI was flagged as an uncertainty, but PBKS's own surprise change — Ferguson out, Dwarshuis debut — was not modeled. Additionally, the rule needs extension: replacement XIs should be assessed for BOTH ceiling and floor, not assumed to be a downgrade. DC's 5 changes produced a team that won. Exp 5: GT vs SRH — rule correctly applied to Travis Head's impact sub status. The memo assessed SRH's starting XI without Head and noted it was weaker than aggregate stats. Head was used as impact sub and scored 0(4). However, the rule was applied asymmetrically again: GT's impact sub Prasidh Krishna 2/23 was not equivalently modeled. Exp 6: RCB vs KKR — Salt's absence correctly modeled with Bethell replacement. Varun's injury correctly flagged as uncertainty with conditional adjustment. However, the actual XI surprises (Venkatesh Iyer in, Suyash Sharma out, Jacob Duffy in) were not anticipated, leading to fragile matchup analysis. See new Entry 12. Exp 7: PBKS vs MI — the asymmetric application pattern recurred for the fourth time. MI's XI uncertainty was correctly flagged as "the largest unresolved variable," but PBKS's own rotation (Stoinis dropped, Ferguson out, Bartlett in for Vyshak) was not anticipated or modeled. Stoinis was PBKS's 5th-highest run scorer (178 runs, SR 174.5) — his absence materially weakened batting depth. This is now a persistent bias: the memo models opposition uncertainty thoroughly but assumes the favored team will field their expected XI. Exp 8: LSG vs CSK — Entry 3 correctly applied to Overton's absence. The 3-5pp adjustment was directionally correct but too narrowly scoped. The actual bowling collapse came from Kamboj (0/63 in 2.4 overs), not from the replacement Prashant Veer. The rule's scope should extend beyond one-for-one replacement quality to cascading role-reassignment effects — see new Entry 15.)

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

**Status:** tentative | **Applications:** 2 (Exp 8: LSG vs CSK — Entry 5 correctly applied for both Mohsin Khan and Josh Inglis, who returned from niggles that ruled them out of the May 7 match. Both were confirmed in the XI. Inglis scored 36(32) and shared a 135-run opening partnership with Marsh. The rule continues to hold. Exp 9: KKR vs GT — Entry 5 correctly applied to Varun Chakaravarthy, returning from a hairline toe fracture. Confirmed in XI, injury discounted by 75%. Figures: 0/47 in 4 overs, economy 11.75. Poor individually, but on a surface where 465 total runs were scored — Rashid Khan 0/57, Tyagi 0/59 — poor economy is indistinguishable from venue conditions. Entry 5's framework holds: presence in XI implies clearance; subsequent performance variance is normal match noise.)

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

**Status:** validated | **Applications:** 7 (Exp 5: GT vs SRH — rule applied. DC's 5-change rotation was an extreme case; in Exp 5, GT's bowling ceiling was the dominant factor regardless of total posted. The principle that replacement/rotated XIs should be assessed for ceiling as well as floor is validated. Exp 7: PBKS vs MI — rule correctly applied. The memo explicitly dismissed the dead-rubber motivation narrative: "no probability adjustment for MI's 'lack of motivation.'" MI — virtually eliminated, missing captain Pandya and vice-captain SKY, with Rohit as impact sub — won by 6 wickets. This is the third consecutive validation that dead-rubber teams are unpredictable, not systematically weaker. Exp 8: LSG vs CSK — fourth consecutive validation. LSG, mathematically eliminated and 2W-6L in last 8, won by 7 wickets with 20 balls to spare. Marsh scored 90(38) — his best innings of the season — in a dead-rubber match. The memo correctly applied 0pp dead-rubber adjustment. Upgraded from "tentative" to "validated." Exp 9: KKR vs GT — fifth consecutive validation. KKR, 10th with 4 points and effectively eliminated, posted 247/2 — their highest total of the season — and won by 29 runs against GT on a 5-match winning streak. Allen 93(35) with 10 sixes, Raghuvanshi 82*(44), Green 52*(28), all playing without consequence-pressure. Five validations across five different teams (DC, GT, MI, LSG, KKR) with zero counter-examples. Exp 10: PBKS vs RCB — sixth consecutive validation, extending the pattern beyond dead-rubber rotation. Patidar (318 runs, SR 186.0, RCB captain) was ruled out. Memo applied -3pp absence adjustment per Entry 7. RCB won by 23 runs with 222/4 — Venkatesh Iyer 73*(40), Kohli 58(37), Padikkal 45(25) compensated fully. Jitesh Sharma captained competently. This is the first non-dead-rubber application: a key player absence in a team still competing for playoff position. Six validations across six different scenarios with zero counter-examples. This is the pipeline's most validated and highest-confidence rule. Exp 11: DC vs RR — seventh application. The memo correctly applied Entry 7 to dismiss DC's "must-win desperation" as non-directional: "motivation is not a directional factor for either team." DC were near-eliminated; the memo applied 0pp motivation adjustment. DC won — not through desperation-driven intensity but through structural quality (Starc's 4/40, Rahul-Porel 105-run stand). Axar Patel's "next year" comments from May 11 had suggested possible psychological concession, yet DC won their next two matches. Entry 7's principle (motivation is unpredictable, assess squad quality not narrative) holds for the seventh consecutive time.)

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

**Status:** tentative | **Applications:** 4 (Exp 5: GT vs SRH — Entry 8 correctly applied. The memo placed GT at 55% vs market's 45.5%, a 9.5pp contrarian gap explained by toss overpricing, H2H dominance, and bowling quality. GT won by 82 runs. The base-rate estimate was more accurate than the market. Exp 6: RCB vs KKR — Entry 8 applied again: memo placed RCB at 54% vs market's 57.5%, a 3.5pp lean BELOW the market. RCB won by 6 wickets. The contrarian direction was against RCB, and RCB won — a mixed result. The memo attributed the market's premium to "anchoring and name recognition," but table position and Kohli's match-winning century (105*) suggest the premium reflected real factors. Entry 8's principle remains sound, but the attribution of WHY the market diverges matters: when the gap is explainable by cognitive biases, lean strongly away; when explainable by verifiable strengths, lean more modestly. Exp 7: PBKS vs MI — Entry 8 applied correctly in direction. The memo placed PBKS at 57% vs market's 61.5%, a 4.5pp lean toward MI. MI won. The lean was directionally correct but insufficiently aggressive — the base-rate analysis (H2H 17-17, home disadvantage, dead-rubber dismissal) pointed closer to 50-53% PBKS, not 57%. Exp 10: PBKS vs RCB — Entry 8 applied correctly for the fourth consecutive time. Market had PBKS 51.5%, memo leaned 3.5pp to ~48% PBKS / ~52% RCB. RCB won by 23 runs. The market premium for PBKS was driven by home advantage anchoring + must-win narrative — both correctly identified as biases. The lean was again directionally correct but magnitude was timid: retrospective fair value ~55-58% RCB vs memo's ~52% RCB. Four consecutive applications show Entry 8's direction is reliable but the lean magnitude is consistently 3-5pp too conservative. When multiple independent factors explain the market divergence, aim for the center of the base-rate range, not its lower bound. Exp 11: DC vs RR — Entry 8 did NOT trigger because the gap between base-rate estimate (~44% DC) and market (43.5% DC) was <3pp. DC won. This reveals a failure mode: when the base-rate estimate agrees with the market, Entry 8 stays silent — but the agreement may itself reflect market anchoring rather than independent confirmation. Three independent signals (Entry 19 form trajectory, venue H2H 6-3, Rahul's ceiling) all pointed toward DC being underpriced. The Skeptic's contrarian view (DC at 47-48%) was closer to truth. See new Entry 22 for the "absence of gap" failure mode.)

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

**Status:** tentative | **Applications:** 2 (Exp 6: RCB vs KKR — Entry 9 was partially applicable but conditions differed. Raipur humidity was moderate (29% rising to 61%), dew-point gap ~15-20C at match start. The memo correctly capped the toss adjustment at +3-5pp. The chasing team (RCB) won, consistent with a moderate — not extreme — toss advantage. Unlike Exp 5 where weather data contradicted the dew narrative, here the weather was ambiguous, and the correct response was a bounded toss adjustment rather than a 0pp cap. Exp 8: LSG vs CSK — Entry 9 correctly applied. Lucknow in May: humidity 42-66%, dewpoints 20-23C, temperatures 30-35C. Multiple sources confirmed "very low chances of dew in Lucknow in peak summer." The memo capped the toss at +2-3pp for LSG (who won toss, elected to field). The toss winner won, but the decisive factor was Marsh's powerplay onslaught (86/0 in 6 overs), not second-innings dew. Capping the toss adjustment was correct — the match confirmed that batting-friendly conditions can favor the chasing team without dew being a factor.)

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

**Status:** tentative | **Applications:** 1 (Exp 9: KKR vs GT — Eden Gardens venue splits from 2017-2019 showed avg first-innings score of 178 from 23 matches. The actual first innings was 247 — 69 runs above the stale average. The match aggregate of 465 was over 100 runs above what the stale data would suggest. The memo correctly refused to anchor on the 178 figure and explicitly acknowledged "venue stats are from 2017-2019 only, providing no reliable 2026-era baseline." Entry 11's warning was vindicated in the starkest possible terms.)

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

**Status:** tentative | **Applications:** 2 (Exp 7: PBKS vs MI — rule correctly applied. The memo explicitly cited Entry 12 and refused to build detailed matchups against MI's unconfirmed XI: "I assess team-level quality only." MI's actual XI differed significantly from the last known XI (Pandya out, SKY out, Rohit demoted to impact sub, Thakur returned). Had the memo built matchups around the May 4 XI, they would have collapsed. Exp 10: PBKS vs RCB — rule correctly applied. The memo noted "per Entry 12, both XIs are unconfirmed, so this is assessed at team-level quality, not specific matchup depth." Multiple sources disagreed on PBKS's bowling combination (Jansen vs Bartlett vs Dwarshuis) and RCB's overseas/spinner slot (Rasikh vs Duffy vs Shepherd). The actual XIs included Rasikh Salam as RCB impact sub (3/36) and Stoinis as PBKS impact sub (37(25)) — neither of whom appeared in any predicted starting XI. Team-level quality assessment correctly captured RCB's bowling superiority without fragile matchup reasoning.)

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

**Status:** tentative | **Applications:** 2 (Exp 8: LSG vs CSK — the name-mismatch pattern recurred. The stats engine returned zero venue matches for "BRSABV Ekana Cricket Stadium," the same systemic issue. The memo correctly identified and disclosed this gap: "the stats engine returned ZERO venue matches due to a name mismatch — all venue-specific statistical splits are missing." The venue was correct (confirmed via multiple match-day sources), but the stats pipeline's venue name format does not match Cricsheet's naming convention. The memo adapted by using news-sourced venue data (five 2026 Ekana match results), which proved adequate. However, the underlying pipeline bug remains unfixed — the same error will recur for any venue whose name in the stats engine differs from Cricsheet's format. Exp 10: PBKS vs RCB — third application, same Dharamsala venue. Stats engine queried "Maharaja Yadavindra Singh International Cricket Stadium" (Mullanpur), returned zero matches. The match was at HPCA Stadium, Dharamsala — confirmed by 6+ independent sources. The memo correctly identified the mismatch, disclosed it transparently, and used 2026 ESPNcricinfo scorecards (avg ~213 from 5 matches) as a substitute. Actual first innings: 222, consistent with the substitute data. The pipeline venue bug remains unfixed after three consecutive occurrences.)

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

**Status:** tentative | **Applications:** 1 (Exp 10: PBKS vs RCB — first application, immediately validated. PBKS entered on a 5-match losing streak including two home losses at Dharamsala (vs DC May 11, vs MI May 14). The memo applied -3 to -5pp per Entry 14. PBKS then lost their 6th consecutive match, collapsing to ~3/3 in the powerplay — Priyansh Arya 0(3), Prabhsimran Singh 2(5), Shreyas Iyer 1(3). The "confidence erosion" mechanism Entry 14 identifies was visible in the top-order failures: three experienced batters managing a combined 3 runs against Bhuvneshwar's powerplay spell. The "must-win desperation" narrative, which the market appeared to price as a positive, was empirically worthless — see new Entry 20.)

## Entry 15 — from Exp 8: LSG vs CSK (2026-05-15), Grade: B+

**When** a key bowler is absent, **model** the cascading effect on the remaining bowling unit's
role assignments — not just the one-for-one replacement quality — because the absent bowler's
workload must be redistributed among teammates who may be exposed in unfamiliar phases.
**Because:** Overton's absence from CSK was assessed as a 3-5pp adjustment based on the quality
gap between Overton and his replacement Prashant Veer. But the actual bowling collapse came from
Kamboj (0/63 in 2.4 overs, economy 23.63) — the bowler cited as proof CSK "retained" bowling
strength. Kamboj may have been forced into death-overs or power-hitter-facing roles that Overton
normally shared. The one-for-one swap framework (Entry 3) correctly identifies the replacement
but misses how the absence reorganizes the entire bowling plan. The true impact is the sum of
the replacement quality gap PLUS the role-reassignment exposure of remaining bowlers. This
extends Entry 3: model not just who replaces the absent player, but who else is pushed into
higher-pressure or unfamiliar roles by the absence.

**Status:** tentative | **Applications:** 0

## Entry 16 — from Exp 8: LSG vs CSK (2026-05-15), Grade: B+

**When** analyzing bowling or batting matchups based on confirmed playing XIs, **acknowledge**
that the impact substitution rule means the actual bowling/batting composition may differ by
1-2 players from the starting XI — and widen uncertainty accordingly.
**Because:** Akash Singh was not in LSG's confirmed XI of 11 but delivered the most impactful
bowling performance of the match (3/26, dismissing CSK's entire top 3). CSK also used impact
subs that changed their bowling attack (Spencer Johnson and Gurjapneet Singh bowled instead of
players from the confirmed XI). The impact sub rule allows teams to introduce match-condition
specialists after the toss — a swing bowler for overcast powerplay conditions, an extra spinner
for a turning pitch, or an explosive batter for a low chase. Pre-match analysis locked to the
confirmed XI systematically underestimates the range of bowling/batting compositions that may
take the field. While individual impact sub choices are unpredictable, the RANGE of possible
compositions is wider than the starting XI implies. This should widen the band or temper
confidence in any analysis that depends on specific matchup comparisons.

**Status:** tentative | **Applications:** 2 (Exp 9: KKR vs GT — Pathirana was KKR's impact sub (not in confirmed starting XI, and pre-match intelligence had him incorrectly attributed to GT). He bowled 1.2 overs before a hamstring injury, leaving KKR one bowler short. Tewatia was GT's impact sub, replacing Siraj in the batting innings. Both substitutions materially altered team composition from confirmed XIs. The pre-match intelligence error on Pathirana's team affiliation demonstrates that impact sub uncertainty extends beyond WHAT substitutions will be made to WHO is even available for substitution. Exp 10: PBKS vs RCB — Rasikh Salam was RCB's impact sub, not in the starting XI. He bowled 3/36 in 4 overs — the match's most decisive bowling spell, dismissing Shreyas Iyer, Shashank Singh (56 off 27, the chase's best batter), and Omarzai in the death overs. Stoinis was PBKS's impact sub, scoring 37(25) — their most composed innings. Two consecutive matches now where impact subs delivered match-defining performances. The starting XI alone is increasingly an unreliable predictor of the actual bowling/batting composition that takes the field.)

## Entry 17 — from Exp 8: LSG vs CSK (2026-05-15), Grade: B+

**When** a prediction market has extreme thin liquidity (<$200 volume), **discard** the price
entirely rather than treating it as a weak signal — build the probability estimate from base
rates only and widen the band by ±2-3pp to compensate for the missing anchor.
**Because:** The Exp 8 Polymarket pool had $52.83 volume at 84.9% LSG. This reflected approximately
one participant's position, not aggregated information. The memo correctly discarded it and built
from base rates, producing a near-coin-flip estimate (CSK 50-55%, LSG 45-50%) that captured the
result within a wide band. Anchoring even partially on 84.9% LSG would have been directionally
correct (LSG won) but for the wrong reasons — the "market" contained no information, and
reinforcing reliance on noise is worse than being directionally wrong for sound analytical reasons.
Entry 8 (lean toward base-rate estimate over market) assumes a functioning market exists to lean
away from. When the market is non-functional, Entry 8 does not apply — there is no "market view"
to diverge from. The correct response is: (a) discard the price explicitly, (b) acknowledge the
informational gap, (c) widen the band to compensate for the absent anchor. Thin markets create
negative informational value: they offer false confidence about a price that reflects positioning,
not probability.

**Status:** tentative | **Applications:** 0

## Entry 18 — from Exp 9: KKR vs GT (2026-05-16), Grade: B

**When** a batter's international T20 profile (career SR 160+, proven power-hitter, multiple
high-six-count innings) dramatically exceeds their current-season IPL strike rate, **weight**
the profile over the season stat for ceiling-probability assessment — the gap signals a player
playing below their known ceiling whose probability of an explosive day is higher than the
season average implies.
**Because:** Finn Allen's season SR was 130.7 from limited matches (not even in KKR's top-5
batters by runs). His international T20 profile (SR 160+ for New Zealand, multiple 10-six
innings in T20 career) indicated a ceiling far above what IPL season stats showed. On a flat
Eden Gardens surface with short boundaries, Allen struck 93(35) at SR 265.71 with 10 sixes —
more than doubling his season average. This mirrors Exp 8 where Marsh (season SR 148.0,
international pedigree of 150+ T20I SR) scored 90(38) at SR 236.84. In both cases, the stats
snapshot's season figures masked batters with demonstrated ceilings far above their current-season
central tendency. Season IPL strike rates describe average performance across varied conditions;
international profiles describe the distribution's upper tail. When conditions favor power-hitting
(flat pitch, short boundaries, batting-friendly surface), profile-based ceiling probability should
inform band width. A recently returned player (Allen was dropped earlier in the season,
suppressing his aggregates) with known explosive ability is especially likely to be systematically
undercounted by season-aggregate batting rankings.

**Status:** tentative | **Applications:** 2 (Pattern observed in Exp 8: Marsh 90(38) and Exp 9: Allen 93(35) — both had international profiles far exceeding their season stats, both produced explosive innings on flat surfaces. Exp 10: PBKS vs RCB — not explicitly applied in the memo but retrospectively relevant. Venkatesh Iyer's IPL pedigree (370 runs in IPL 2021 for KKR, career T20 SR above 140) indicated a ceiling far above his role as a middle-order bat in the stats. He scored 73*(40) at SR 182.5 with 8 fours and 4 sixes — Man of the Match. The memo assessed RCB's batting depth via Kohli, Padikkal, and Tim David but missed Iyer's ceiling. This echoes both the Allen (Exp 9) and Marsh (Exp 8) pattern: the match winner was a middle-order player whose ceiling was underappreciated because the analytical frame focused on top-order stars. Exp 11: DC vs RR — pattern extends to BOWLERS. Mitchell Starc's international pedigree (World Cup final winner, 143 T20I wickets, multiple 3+ haul T20 spells) indicated a ceiling far above what DC's aggregate bowling stats (porous beyond Starc and Ngidi) suggested. Starc took 4/40 including 3 wickets in 4 balls when RR were 161/2, collapsing them to 193/8. Man of the Match. The memo assessed DC's bowling through its WEAKNESS (Kuldeep 10.3, Mukesh 10.27) rather than Starc's CEILING. This is the fourth match-winner in four experiments whose ceiling was underappreciated by season averages — now covering batters (Marsh, Allen, Iyer) AND bowlers (Starc). See new Entry 23 for bowler-specific extension.)

## Entry 19 — from Exp 9: KKR vs GT (2026-05-16), Grade: B

**When** a team's "last N" form record contains a significant trend reversal (e.g., a 4+ match
winning streak within an overall poor record), **decompose** the trajectory rather than averaging
across the window — the recent trend is more informative than the headline figure when the team
has demonstrably changed quality mid-season.
**Because:** KKR's 2W-6L in their last 8 completed matches was the primary form signal driving
GT's +5-8pp advantage. But KKR had actually won 4 consecutive matches before losing to RCB on
May 13 — and that loss came against Kohli's 105(60). The 2W-6L figure was heavily influenced by
early-season losses (SRH by 65 runs on April 2, LSG by 3 wickets on April 9) that no longer
reflected mid-May quality. KKR then posted 247/2 against GT — their highest score of the season.
The pipeline has Entry 14 for detecting negative momentum (extended losing streaks) but no
equivalent mechanism for positive momentum reversals, creating an asymmetry that systematically
underprices improving teams. The Skeptic noted KKR were "not on a current losing streak" but
framed this as a negative finding (Entry 14 doesn't trigger) rather than positive evidence
(KKR's quality had improved). When the recent sub-window (last 4-5 matches) shows a pattern
directionally opposite to the full window (last 8), the sub-window should dominate.

**Status:** tentative | **Applications:** 1 (Exp 11: DC vs RR — first application, immediately validated. DC's 2W-6L in the stats snapshot masked a recent improvement: DC beat RR on May 1 (7 wickets) and beat PBKS on May 11 (chasing 211). The memo identified this trajectory and applied 2-3pp uplift per the Skeptic's recommendation. DC then won their third in four matches — beating RR by 5 wickets chasing 193. The form trajectory was partly tactical (Porel replacing Nissanka at the top, new lineup gelling) — not just win/loss noise. The tactical adaptation signal strengthens the trajectory assessment: when a team changes personnel AND wins, the improvement is more likely structural than random.)

## Entry 20 — from Exp 10: PBKS vs RCB (2026-05-17), Grade: B+

**When** a team combines "must-win" situational pressure with an extended losing streak (3+
matches), **treat** the combination as amplifying the negative momentum, not offsetting it —
"must-win desperation" is not a positive performance predictor and has no empirical backing
in this pipeline.
**Because:** PBKS were in a must-win situation (loss effectively eliminates from playoffs) on a
5-match losing streak. The market priced PBKS at 51.5% — a slight favorite — apparently
anchoring on home advantage and the must-win motivation narrative. PBKS collapsed to ~3/3 in
the powerplay (Arya 0, Prabhsimran 2, Iyer 1) and lost by 23 runs. The "desperation = intensity"
narrative predicted improved performance; the actual outcome was the opposite — a top-order
capitulation consistent with confidence erosion under compounding pressure. Entry 7 (6 consecutive
validations that low-pressure teams perform well) provides the inverse evidence: pressure-free
teams play with liberation, while desperate teams on losing streaks face compounding psychological
weight. When the market prices "must-win" as a positive factor for a team on an extended losing
streak, the market is wrong — fade the must-win premium and apply Entry 14's negative adjustment
without offset.

**Status:** tentative | **Applications:** 1 (Exp 11: DC vs RR — Entry 20 was not directly triggered because DC were not on an extended losing streak. However, the inverse pattern was relevant: DC were in a "must-win" situation but on an IMPROVING trajectory (2-3 wins in last 4). The memo correctly applied 0pp for motivation — neither boosting DC for desperation nor penalizing them. DC won. Entry 20's framework (desperation + losing streak = amplified negative) was respected in the negative: desperation alone (without a losing streak) is neutral, not positive. The entry's core principle — that must-win pressure is not a performance enhancer — holds.)

## Entry 21 — from Exp 11: DC vs RR (2026-05-17), Grade: C+

**When** a team's opponent-specific venue H2H record (e.g., 6-3 vs a particular team at a
particular ground) conflicts with the team's general home record in the current season (e.g.,
1-6 at home overall), **weight** the opponent-specific H2H more heavily than the general record
for that specific matchup — the H2H captures persistent matchup dynamics (bowling style vs
batting approach, psychological factors, tactical patterns) that the general record cannot.
**Because:** DC were 6-3 vs RR at Arun Jaitley Stadium (spanning multiple years and squad
compositions) but 1-6 at home in IPL 2026 overall. Entry 1 was applied to discount the 6-3
H2H by 50%+ based on the 1-6 general record, reducing the venue H2H uplift from +8-10pp to
+2-3pp. DC then won — extending the H2H to 7-3. The 1-6 general record reflected DC's
struggles against CSK, RCB, PBKS, SRH, and GT — none of which are RR. The opponent-specific
signal captures something persistent: DC have won 7 of 10 against RR at this ground across
different eras, different squads, and different conditions. This is now strong enough to
qualify under Entry 10's framework (persistent venue dynamics >=3-0). Entry 1's discount
should apply at full strength when the contradiction comes from the SAME opponent (e.g., team
lost to RR twice at the same venue this season). When the contradiction comes from different
opponents, reduce the discount to ~25% because the opponent-specific matchup dynamic may
persist even when general form is poor.

**Status:** tentative | **Applications:** 0

## Entry 22 — from Exp 11: DC vs RR (2026-05-17), Grade: C+

**When** Entry 8 fails to trigger because the gap between base-rate estimate and market is
<3pp, **check** whether the absence of a gap reflects genuine market-model agreement OR whether
the base-rate estimate is being anchored by the market — particularly when multiple independent
analytical factors (form trajectory, venue H2H, individual player ceiling) all point toward
the same team being underpriced.
**Because:** The market had DC at 43.5%. The memo's base-rate estimate landed at ~44% DC — gap
<1pp, so Entry 8 did not trigger ("no confident directional divergence from the market is
warranted"). But three independent analytical signals all pointed toward DC being higher:
(1) Entry 19's form trajectory (DC won 2-3 of last 4 matches); (2) venue H2H (DC 6-3 vs RR
at Arun Jaitley); (3) KL Rahul's extraordinary form (445 runs, SR 172.5, 152* at this venue).
DC won. The Skeptic's Anchoring Check identified all three factors and noted DC "should be
closer to 47-48%" — but labeled this "contrarian" rather than "primary estimate." The error
was framing market agreement as confirmation rather than questioning whether the base-rate
estimate was being pulled toward the market anchor. Entry 8's 3pp threshold is designed to
prevent unnecessary contrarianism — but it should not suppress a lean when the base-rate
calculation itself is being conservatively anchored. When 3+ independent factors point in the
same direction and the estimate still matches the market, ask: "Am I constructing the base
rate from first principles, or am I rationalizing my way back to the market price?"

**Status:** tentative | **Applications:** 0

## Entry 23 — from Exp 11: DC vs RR (2026-05-17), Grade: C+

**When** assessing a team's bowling quality, **distinguish** between the team's bowling floor
(what happens when all bowlers perform at their season average) and the team's bowling ceiling
(what happens when the elite bowler produces a match-winning spell) — particularly in T20
cricket where one transformative over can collapse an innings.
**Because:** DC's bowling was assessed through team-level weakness: Kuldeep 10.3 economy,
Mukesh Kumar 10.27, Natarajan 10.45. The narrative was "DC's bowling is porous beyond Starc
and Ngidi." In the match, Starc took 3 wickets in 4 balls when RR were 161/2 heading for 220+,
collapsing them to 193/8 — a 27-run swing on a single over that changed the match's win
probability from ~35% DC to ~65% DC. Starc's international pedigree (World Cup final winner,
143 T20I wickets, multiple 3+ hauls) indicated exactly this ceiling — but the memo's bowling
narrative focused on the floor. This extends Entry 18 to bowlers: when one world-class bowler
is present in an otherwise weak attack, the team's AVERAGE bowling performance is poor but
the CEILING is high. In T20 cricket, where one death-overs spell can collapse an innings, the
ceiling probability is more relevant to band assessment than the average. The bowling "quality
gap" between teams should be assessed as a distribution (floor-to-ceiling), not a point
estimate (season economy averages).

**Status:** tentative | **Applications:** 0
