# Source Quality Assessment: Royal Challengers Bengaluru vs Kolkata Knight Riders

## Overall Evidence Quality: Mixed

This report operates under significant structural uncertainty. The two highest-value claims for any pre-match memo -- toss result and confirmed playing XIs -- are both unavailable due to rain delay. The News Analyst has done a commendable job flagging discrepancies (venue, standings), but the core evidence base rests on journalist preview articles (CricTracker, CricketAddictor), a single news report (Sunday Guardian Live), and weather APIs. No official team announcements or press conference quotes are available for team selection. The venue correction is well-sourced from official match pages, but Raipur venue statistics come from a tiny 7-match sample. Multiple material uncertainties (Salt, Allen, Varun fitness) remain unresolved with conflicting source signals.

## Claim-by-Claim Audit

| # | Claim | Source | Dated | Rating | Flag |
|---|-------|--------|-------|--------|------|
| 1 | Venue is Shaheed Veer Narayan Singh International Stadium, Raipur, not Chinnaswamy | ESPNcricinfo, IPL official site, Outlook India | May 13, 2026 | **confirmed** | Cross-verified across 3+ official/reputable platforms |
| 2 | Stats snapshot standings are outdated; RCB actually P11/W7/14pts, KKR P10/W4/9pts | CricTracker, CricketAddictor | ~May 12-13, 2026 | **probable** | Two independent sources agree, but neither is an official league table |
| 3 | Toss delayed due to rain; ground under covers; inspection at 8:15 PM IST | Outlook India, NewsX | May 13, 2026 | **confirmed** | Live match-day reporting from multiple independent sources |
| 4 | RCB predicted XI (Bethell opening, no Salt, Krunal included) | CricTracker, CricketAddictor | Undated / ~May 12-13 | **speculative** | Journalist predictions, NOT confirmed XIs. CricketAddictor contradicts by including Salt |
| 5 | KKR predicted XI (Rahane opens, Allen as impact sub or starter) | CricTracker, CricketAddictor | Undated / ~May 12-13 | **speculative** | Journalist predictions with sources disagreeing on Allen's role |
| 6 | Phil Salt not cleared to play; finger injury from DC match | Sunday Guardian Live | May 13, 2026 | **probable** | Single named source with specific detail. Directly contradicted by CricketAddictor's predicted XI |
| 7 | Krunal Pandya fit despite cramps; rested Tuesday practice | Sunday Guardian Live | May 13, 2026 | **probable** | Single source, dated. Consistent with inclusion in all predicted XIs |
| 8 | Varun Chakravarthy managing leg injury; crutches/knee braces; "likely to push through" | CricketGully, LokmaTimes, IndiaTV | May 12-13, 2026 | **probable** | Multiple sources corroborate injury. Shane Watson quote cited. Selection is editorial inference |
| 9 | Matheesha Pathirana sidelined with hamstring strain | Sunday Guardian Live | May 13, 2026 | **probable** | Single source, dated. No official team announcement |
| 10 | Virat Kohli has back-to-back ducks despite 379 runs overall at SR 156.6 | CricTracker preview | ~May 12-13, 2026 | **probable** | Verifiable statistical claim from reputable site |
| 11 | Pitch: black-soil, slow and low, inconsistent bounce, good early carry | Sportskeeda, IPL.com, CricTracker | ~May 12-13, 2026 | **speculative** | No curator quote. Journalist characterizations. "Slow and low" vs "good bounce and carry early" is partially contradictory |
| 12 | Boundaries ~80m at Raipur | CricTracker / Sportskeeda | ~May 12-13, 2026 | **probable** | Physical venue characteristic, consistent across sources |
| 13 | Par score at Raipur: 149-165 range | CricTracker / Sportskeeda | ~May 12-13, 2026 | **speculative** | Derived from 7-match average. Far too small for reliable estimate |
| 14 | Average 1st innings score at Raipur: ~147-149 from 7 matches | Sportskeeda, IPL.com, CricTracker | ~May 12-13, 2026 | **probable** | Multiple sources agree. But 7-match sample has huge confidence intervals |
| 15 | Chase wins 5 of 7 at Raipur (71.4%) | Sportskeeda, IPL.com, CricTracker | ~May 12-13, 2026 | **probable** | Verifiable but 5/7 is tiny sample -- true rate could be 30-95% |
| 16 | Weather: 33C, humidity 29% rising to 61% by 9PM, wind 13km/h SE | wttr.in API | May 13, 2026, ~13:40 UTC | **probable** | Current conditions reliable; forecast humidity carries error bars |
| 17 | Rain: 0% from 7:30 PM per AccuWeather/Skymet | The Dakia | May 13, 2026 | **probable** | Contradicted by IMD yellow alert and Sunday Guardian's 50% claim |
| 18 | IMD yellow alert for thunderstorms in Chhattisgarh; 50% rain per IMD | Sunday Guardian | May 13, 2026 | **probable** | Cites official IMD but "50%" may be journalist interpretation |
| 19 | Dew moderate-to-high in second innings | Multiple sources (unspecified) | Undated | **speculative** | Generic venue lore. No quantitative measurement. Humidity/dew-point gap is moderate |
| 20 | KKR on a 4-match winning streak | CricTracker, CricketAddictor | ~May 12-13, 2026 | **probable** | Two sources agree. Verifiable |
| 21 | RCB won vs MI on May 10 at this venue (last-ball, 2-wicket win) | CricTracker, CricketAddictor | ~May 12-13, 2026 | **probable** | Two sources agree on specific details |
| 22 | Finn Allen scored 100 off 47 vs DC (unbeaten century) | CricketAddictor | ~May 12-13, 2026 | **probable** | Single source with specific scorecard detail |
| 23 | Overall H2H: RCB 15, KKR 20 from 35 matches; KKR won 4 of last 5 | CricketAddictor + stats snapshot | ~May 12-13, 2026 | **probable** | Overall figures consistent between web and snapshot |
| 24 | Bhuvneshwar Kumar is Purple Cap holder with 21 wickets in 11 matches | CricTracker | ~May 12-13, 2026 | **probable** | Conflicts with snapshot (17 in 10). Discrepancy likely from stale snapshot |
| 25 | Bhuvneshwar took 4/23 at this ground vs MI | CricTracker preview | ~May 12-13, 2026 | **probable** | Specific scorecard reference. Verifiable but not cross-checked |
| 26 | If washed out, both teams get 1 point each | IPL rules | N/A | **confirmed** | Standard regulation |

## Flagged Issues

1. **No confirmed XIs or toss result.** The most critical pre-match inputs are absent. All team composition claims are journalist predictions with material disagreements (Salt, Allen). This is the single largest evidence gap.

2. **Phil Salt availability contradicted.** Sunday Guardian says "not cleared." CricketAddictor includes him in predicted XI. Neither cites an official RCB announcement. Salt opening vs Bethell opening materially changes RCB's batting profile.

3. **Finn Allen's role unresolved.** Sources disagree on starter vs impact sub. His 100 off 47 vs DC makes this material for KKR's approach.

4. **Raipur venue stats rest on 7-match sample.** The 71.4% chase rate and ~149 average have enormous confidence intervals. Treating these as reliable venue characteristics is statistically dubious.

5. **Pitch report lacks curator quote.** "Black-soil, slow and low, inconsistent bounce" is journalist venue lore, partially internally contradictory. Use as soft prior, not hard constraint.

6. **Conflicting rain forecasts.** AccuWeather/Skymet say 0% post-7:30 PM; IMD yellow alert active; Sunday Guardian says 50%. Irreconcilable -- one set is wrong.

7. **Dew claims weakly sourced.** "Multiple sources confirm" without naming them. Weather data (29% humidity, dew point 11-13C, temp 33C) suggests a significant gap, making heavy dew uncertain.

8. **Approximate dates throughout.** Most sources dated "~May 12-13." CricTracker predicted XI is "undated." Impossible to verify recency of team news.

9. **Bhuvneshwar wicket count discrepancy.** Web says 21 in 11; snapshot says 17 in 10. Plausible if snapshot is stale (4 wickets in 1 match is possible -- he took 4/23 vs MI). Not independently confirmed.

10. **Circular sourcing risk.** CricTracker and CricketAddictor may draw from similar sources. Their "agreement" may reflect shared inputs, not independent verification.

## Recommendation for Synthesizer

**Weight heavily:**
- Venue correction to Raipur (confirmed -- load-bearing for entire analysis)
- Toss not yet taken; no confirmed XIs (confirmed)
- Rain delay is real; match may be shortened (confirmed)
- General standings direction: RCB ahead, KKR behind (probable, two sources)

**Weight moderately:**
- Injury reports: Salt (not cleared, probable), Krunal (fit, probable), Varun (doubtful, probable), Pathirana (out, probable)
- Weather current conditions (reliable for current, forecast carries error)
- H2H overall direction (KKR lead; consistent between web and snapshot)
- KKR 4-match streak (probable from two sources)
- Bhuvneshwar's form and venue-specific performance (probable)

**Discount or widen uncertainty bands around:**
- All predicted playing XIs -- speculative with known disagreements. Do not treat any player's inclusion as settled.
- Raipur venue stats (7-match sample) -- use directional signal only, widen bands significantly
- Pitch characterization -- no curator quote; journalist venue lore
- Dew intensity claims -- weakly sourced, partially contradicted by weather data
- Rain probability for match -- genuinely conflicting signals (0% vs 50%). Assign material but not dominant probability
- Par score "149-165" -- over-precise from inadequate data
- All tactical framing (spin battle, Narine vs Patidar) -- editorial speculation

**Critical note:** This memo must be priced with unusually wide uncertainty bands. The absence of toss and confirmed XIs, venue data mismatch requiring wholesale correction, conflicting player availability, and conflicting weather forecasts all compound.
