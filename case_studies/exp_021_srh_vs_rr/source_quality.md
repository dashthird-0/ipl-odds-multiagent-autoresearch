# Source Quality Assessment: Sunrisers Hyderabad vs Rajasthan Royals (Eliminator)

## Overall Evidence Quality: Strong

This is the strongest evidence quality in the experiment series. Both playing XIs are confirmed at toss (not speculative), the toss result is confirmed, weather data is from a real-time API, and the venue correction is supported by 4+ independent sources. The only weak areas are impact player selections (unknown) and Parag's true fitness level (conflicting self-reports).

## Claim-by-Claim Audit

| # | Claim | Source | Dated | Rating | Flag |
|---|-------|--------|-------|--------|------|
| 1 | Venue is Maharaja Yadavindra Singh PCA Stadium, Mullanpur | Sportstar (4 independent articles) | 2026-05-27 | **confirmed** | Multiple independent sources agree |
| 2 | Evidence packet says Rajiv Gandhi International Cricket Stadium (Hyderabad) | evidence_cutoff.md | 2026-05-27 | **confirmed wrong** | Entry 13 venue error, 11th occurrence |
| 3 | SRH won toss and chose to bowl | Sportstar live updates + Cricbuzz ticker | 2026-05-27 | **confirmed** | Two independent sources |
| 4 | RR Playing XI (Jaiswal, Sooryavanshi, Jurel, Parag, Ferreira, Shanaka, Jadeja, Archer, Burger, Brijesh Sharma, Yash Raj Punja) | Sportstar (toss confirmation) | 2026-05-27 | **confirmed** | Official toss announcement |
| 5 | SRH Playing XI (Abhishek, Head, Ishan, Klaasen, Smaran, Nitish, Cummins, Shivang, Malinga, Sakib, Hinge) | Sportstar (toss confirmation) | 2026-05-27 | **confirmed** | Official toss announcement |
| 6 | Jadeja returns to RR XI | Sportstar live updates | 2026-05-27 | **confirmed** | Named in confirmed XI |
| 7 | Travis Head confirmed in SRH XI | Sportstar confirmed XI | 2026-05-27 | **confirmed** | Named in confirmed XI |
| 8 | Parag "fit to play" at toss | Sportstar live updates (captain's quote) | 2026-05-27 | **confirmed** | Direct quote at toss |
| 9 | Parag previously said "I'm definitely not fit" after MI match | Sportstar Parag fitness article | 2026-05-27 | **confirmed** | Direct quote from post-match interview |
| 10 | Parag unlikely to bowl due to hamstring | Sportstar key battles article | 2026-05-27 | **probable** | Journalist assessment, consistent with injury history |
| 11 | Pitch described as "absolutely flat" by Aaron Finch | Sportstar live updates | 2026-05-27 | **confirmed** | Direct quote from commentator at venue |
| 12 | SRH described as having "fully fit squad" | Sportstar live score article | 2026-05-27 | **probable** | No specific attribution to team management |
| 13 | Sooryavanshi: 583 runs in 14 outings, SR 232.27 | Sportstar key battles article | 2026-05-27 | **probable** | Single source but consistent with snapshot trajectory (404 runs from 10 matches in snapshot) |
| 14 | Sooryavanshi: 430 runs in 186 balls in PowerPlay | Sportstar key battles article | 2026-05-27 | **probable** | Internally consistent with overall numbers |
| 15 | Klaasen: 606 runs, 3rd Orange Cap | Sportstar Orange Cap article | 2026-05-27 | **confirmed** | Cross-referenced with Orange Cap standings article |
| 16 | Jurel: 458 runs, SR 149.67 | Sportstar key battles article | 2026-05-27 | **probable** | Consistent with snapshot trajectory (290 from 10 matches) |
| 17 | Jurel SR 129.82 vs spin, 161.45 vs pace | Sportstar key battles article | 2026-05-27 | **probable** | Detailed split; single source but plausible |
| 18 | Archer: 21 wickets in 14 matches, economy 8.76 (3rd Purple Cap) | Sportstar Purple Cap article | 2026-05-27 | **confirmed** | Cross-referenced across two Sportstar articles |
| 19 | Archer: 8 wickets at avg 17.12, economy 8.55 in PowerPlay | Sportstar key battles article | 2026-05-27 | **probable** | Detailed split; single source |
| 20 | Archer has dismissed Head 3 times, Abhishek once in T20s | Sportstar key battles article | 2026-05-27 | **probable** | Specific claim, plausible from career data |
| 21 | SRH "lack of genuine new ball bowler" | Sportstar analysis | 2026-05-27 | **probable** | Journalist assessment, consistent with bowling stats |
| 22 | SRH's "inexperienced bowling lineup" may struggle under pressure | Sportstar analysis | 2026-05-27 | **speculative** | Editorial opinion, not factual claim |
| 23 | Mullanpur 2026 avg first innings 214.2 (4 matches) | Cricsheet analysis | pre-cutoff | **confirmed** | Direct ball-by-ball data analysis |
| 24 | Mullanpur 2026 chase wins 3 of 4 (75%) | Cricsheet analysis | pre-cutoff | **confirmed** | Direct ball-by-ball data analysis |
| 25 | Weather: 6-9% humidity, -3C dew point at match time | wttr.in API | 2026-05-27 | **probable** | Real-time API; forecasts have inherent uncertainty but physics-based |
| 26 | Dew physically impossible | Derived from weather data | 2026-05-27 | **probable** | 37-45C temperature-dew point gap; physics supports this |
| 27 | SRH beat RR by 57 runs in first meeting (Hyderabad, Apr 13) | Sportstar + Cricsheet | 2026-04-13 | **confirmed** | Multiple sources |
| 28 | SRH beat RR by 5 wickets in second meeting (Jaipur, Apr 25) | Sportstar + Cricsheet | 2026-04-25 | **confirmed** | Multiple sources |
| 29 | Sooryavanshi scored 36-ball century in second meeting | Sportstar key battles article | 2026-05-27 | **confirmed** | Consistent with match records |
| 30 | RCB beat GT in Qualifier 1 (May 26) | Sportstar, case study exp_020 | 2026-05-26 | **confirmed** | Multiple sources |
| 31 | Eliminator format: loser eliminated, winner to Q2 vs GT | Sportstar streaming article | 2026-05-27 | **confirmed** | Tournament format |
| 32 | SRH three batters with 500+ runs | Sportstar key battles article | 2026-05-27 | **probable** | Klaasen confirmed at 606; Abhishek and Ishan likely surpassed 500 since snapshot |
| 33 | Parag's hamstring limits bowling contributions | Sportstar key battles article | 2026-05-27 | **probable** | Consistent with injury reports and fitness quotes |

## Flagged Issues

1. **Stats snapshot is stale for player statistics.** The snapshot captures data through approximately May 6 (SRH's last match in Cricsheet data). Since then, both teams have played additional matches. Key discrepancies:
   - Sooryavanshi: 404 runs in snapshot vs 583 reported (179-run gap, ~4 matches)
   - Klaasen: 494 runs in snapshot vs 606 confirmed (112-run gap)
   - Jurel: 290 runs in snapshot vs 458 reported (168-run gap)
   - Archer: 15 wickets in snapshot vs 21 confirmed (6-wicket gap)

2. **Venue data in stats snapshot is for the WRONG VENUE.** All venue splits, toss impact data, and venue H2H from the stats snapshot refer to Rajiv Gandhi International Cricket Stadium (Hyderabad), not Mullanpur. Must be completely discarded.

3. **SRH's bowling assessment as "inexperienced" (claim 22) is editorial opinion**, not sourced to team management or statistical evidence. However, it is consistent with the bowling stats: Malinga, Sakib Hussain, and Praful Hinge are all young or relatively unproven in playoff pressure.

4. **Parag's fitness is a confirmed-but-ambiguous situation.** He is confirmed in the XI (Entry 5 applies: discount injury by 75%). But his own statement "I'm definitely not fit" (pre-toss) contradicts his toss-time "I'm fit to play." The hamstring issue is real and limits his bowling. Per Entry 5, presence in XI implies medical clearance; discount further injury-based concerns.

## Recommendation for Synthesizer

- **Weight heavily:** Venue correction (Mullanpur, not Hyderabad), confirmed toss result (SRH bowl), confirmed playing XIs, confirmed weather data (no dew), Cricsheet venue data (214.2 avg, 75% chase wins at Mullanpur in 2026), confirmed H2H results (SRH beat RR twice in 2026).
- **Weight moderately:** Updated player stats from Sportstar (single-sourced but internally consistent and plausible), Jurel's spin weakness, Archer's PowerPlay record, SRH bowling concerns.
- **Discount:** Editorial opinions about "inexperienced bowling" and "pressure" -- these are narrative, not evidence. Parag's fitness beyond his toss confirmation -- he is in the XI, Entry 5 applies.
- **Widen band for:** Impact player selections (unknown for both teams), and the venue data gap (Mullanpur-specific venue stats are available from Cricsheet but the stats snapshot's venue data is completely wrong).
