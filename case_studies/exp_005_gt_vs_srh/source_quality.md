# Source Quality Assessment: Gujarat Titans vs Sunrisers Hyderabad

## Overall Evidence Quality: Mixed-to-Strong

The News & Conditions output draws primarily from two named news sources (Hindustan Times live score page, Times of India preview) and one weather API (wttr.in). The highest-value claims -- toss result, confirmed playing XIs, and both teams unchanged -- come from live match-day reporting of the toss ceremony, which is the gold standard for pre-match evidence. Pitch and tactical analysis claims rely on journalist assessment with less verifiable grounding. Weather data is from a reliable forecast API for current conditions.

## Claim-by-Claim Audit

| # | Claim | Source | Dated | Rating | Flag |
|---|-------|--------|-------|--------|------|
| 1 | SRH captain Pat Cummins won the toss and opted to bowl first | Hindustan Times live score page | 2026-05-12, 7:09 PM IST | **confirmed** | Live match reporting of toss ceremony; independently corroborated by Cricbuzz live scores page showing "SRH opt to bowl" |
| 2 | Both teams going unchanged | Hindustan Times live score page | 2026-05-12 | **confirmed** | Reported at toss; captains typically announce changes at toss. No change = confirmed by omission |
| 3 | GT confirmed Playing XI (11 players listed) | Hindustan Times live score page | 2026-05-12, ~7:00 PM IST | **confirmed** | Announced at toss |
| 4 | SRH confirmed Playing XI (11 players listed) | Hindustan Times live score page | 2026-05-12, ~7:00 PM IST | **confirmed** | Announced at toss |
| 5 | GT impact sub options: Kumar Kushagra, Anuj Rawat, Prasidh Krishna, Sai Kishore, Glenn Phillips | Hindustan Times live score page | 2026-05-12 | **confirmed** | Listed at toss |
| 6 | SRH impact sub options: Travis Head, Aniket Verma, Harsh Dubey, Harshal Patel, Liam Livingstone | Hindustan Times live score page | 2026-05-12 | **confirmed** | Listed at toss |
| 7 | Travis Head NOT in SRH's starting XI | Hindustan Times live score page | 2026-05-12 | **confirmed** | Directly observable from the confirmed XI |
| 8 | Pitch: balanced, batting-friendly surface with significant dew factor in second innings | Times of India preview | 2026-05-12, 16:55 IST | **probable** | Journalist assessment; "significant dew factor" is a subjective claim, not curator-confirmed. No direct curator quotes cited. |
| 9 | Ahmedabad track offers true bounce and consistent pace | Times of India preview | 2026-05-12, 16:55 IST | **probable** | General venue characterization consistent with known Ahmedabad conditions but not match-specific |
| 10 | Weather: 33-34C at match time, 0% rain, 11-20% humidity, 0% cloud cover | wttr.in weather API | 2026-05-12 (current) | **probable** | Weather API data; forecasts have error bars but current conditions are reliable. The 0% rain claim is robust for same-day evening. |
| 11 | Heatwave alert in Ahmedabad, 44-45C daytime | wttr.in + Times of India | 2026-05-12 | **confirmed** | Weather API shows 42C actual temperature; Times of India corroborates 44-45C |
| 12 | GT on 4-match winning streak | Stats snapshot + Hindustan Times | 2026-05-12 | **confirmed** | Cross-verified against Cricsheet data in stats_snapshot.json |
| 13 | SRH won 6 of last 7 matches | Stats snapshot + Hindustan Times | 2026-05-12 | **confirmed** | Cross-verified against Cricsheet data |
| 14 | GT won 5 of 6 completed H2H meetings vs SRH | Stats snapshot | Pre-cutoff | **confirmed** | Cricsheet ball-by-ball data |
| 15 | GT won all 3 previous meetings at Narendra Modi Stadium vs SRH | Hindustan Times article | 2026-05-12 | **probable** | Not independently verified against Cricsheet (venue_splits show 0 matches due to name mismatch); single journalistic source, but consistent with H2H record direction |
| 16 | GT last beat SRH at this venue in IPL 2025 by 38 runs (GT posted 224/6) | Hindustan Times article | 2026-05-12 | **probable** | Historical claim from reputable source; not cross-checked against Cricsheet data |
| 17 | GT bowling: 70 wickets in 11 matches; 21 powerplay wickets | Hindustan Times article | 2026-05-12 | **probable** | Journalist-compiled statistics; plausible against stats snapshot (Rabada 16, Prasidh 12, Siraj 11 = 39 from top 3 alone) |
| 18 | GT concede 9.37 RPO overall | Hindustan Times article | 2026-05-12 | **probable** | Single-source journalist statistic |
| 19 | GT's middle order has second-lowest average and fewest sixes this season | Times of India preview | 2026-05-12 | **speculative** | No data source cited; journalist claim. "Second-lowest" is specific enough to verify but unverified here |
| 20 | SRH's middle order has third-best strike rate and highest sixes | Times of India preview | 2026-05-12 | **speculative** | Same as above -- journalist claim without cited data source |
| 21 | Klaasen vs Rashid could decide the middle overs | Hindustan Times article | 2026-05-12 | **speculative** | Narrative/editorial framing, not a factual claim |
| 22 | GT's batting is "built on control, not chaos" | Hindustan Times article | 2026-05-12 | **speculative** | Editorial characterization |
| 23 | SRH improved significantly since inclusion of Sakib Hussain | Times of India preview | 2026-05-12 | **probable** | Consistent with stats (Sakib Hussain: 10 wickets, 8.48 eco) and SRH's win streak timing |

## Flagged Issues

1. **Venue data gap is real but partially addressed:** The stats snapshot venue_splits show 0 matches at "Narendra Modi Stadium" due to a likely venue name matching issue. The News Analyst correctly flagged this. The HT claim of GT winning all 3 home meetings vs SRH fills part of this gap but is single-source.

2. **Pitch report lacks curator quotes:** The "balanced, batting-friendly" and "significant dew factor" claims come from journalist preview writing, not from an official curator statement or press conference. This is standard for IPL pre-match coverage but should be weighted as probable, not confirmed.

3. **Middle-order comparative claims are unverified:** The TOI claims about GT having the "second-lowest average" and SRH having the "highest number of sixes" in middle-order play are specific statistical claims presented without source data. They are plausible given what we see in the stats snapshot (GT middle order is thin beyond the top 3; SRH has Klaasen/Abhishek/Ishan all with 149+ SR) but remain speculative as stated.

4. **Dew claim tension with humidity data:** The Times of India says "significant dew factor" but the weather API shows only 11-20% humidity. These are in mild tension. Dew formation depends on temperature hitting the dew point (6-10C per the API) -- with evening temperatures at 33-34C, the gap is large (~23C), which would normally suggest low dew. The News Analyst correctly flagged this uncertainty.

5. **RR match result (May 9) not yet in stats snapshot:** The stats snapshot shows GT at P10 W6, but the HT article and search results confirm GT beat RR by 77 runs on May 9 (Match 52), putting them at P11 W7 Pts14. This is a confirmed data lag, not a quality issue.

## Recommendation for Synthesizer

- **Weight heavily:** Toss result (SRH bowl first), confirmed playing XIs, both teams unchanged, weather conditions, head-to-head record, recent form. These are all confirmed or high-probable.
- **Weight moderately:** Pitch assessment (probable but not curator-confirmed), venue history at Ahmedabad (probable, single journalistic source), SRH middle-order quality (supported by stats snapshot).
- **Discount or widen bands around:** GT middle-order weakness claim (speculative -- specific ranking unverified), dew severity (tension between weather API and journalist claim), editorial tactical narratives (matchup framing is speculative by nature).
- **Key analytical note:** Travis Head's absence from the starting XI is confirmed and material. However, the impact substitute rule means he can enter the match at the innings break. The Synthesizer should model scenarios with and without Head entering.
