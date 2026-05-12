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

**Status:** tentative | **Applications:** 2 (Exp 3: RCB vs MI — rule applied; Chinnaswamy venue data correctly excluded from Raipur analysis; the extreme case where venue priors were not merely contradicted but entirely inapplicable. Exp 4: PBKS vs DC — rule applied; PBKS's 6-8 Dharamsala record used to negate home advantage; PBKS lost again, extending to 6-9.)

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

**Status:** tentative | **Applications:** 1 (Exp 4: PBKS vs DC — rule applied to DC but not reciprocally to PBKS. DC's replacement XI was flagged as an uncertainty, but PBKS's own surprise change — Ferguson out, Dwarshuis debut — was not modeled. Additionally, the rule needs extension: replacement XIs should be assessed for BOTH ceiling and floor, not assumed to be a downgrade. DC's 5 changes produced a team that won.)

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

**Status:** tentative | **Applications:** 0

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

**Status:** tentative | **Applications:** 0
