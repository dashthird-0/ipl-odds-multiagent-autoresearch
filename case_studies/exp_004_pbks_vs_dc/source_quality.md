# Source Quality Assessment: Punjab Kings vs Delhi Capitals

## Overall Evidence Quality: Mixed

**Confidence split:** ~25% confirmed, ~45% probable, ~30% speculative/unsourced.

The News & Conditions Analyst has done solid work citing sources with URLs and dates for most claims. The evidence base is strengthened by direct quotes from identified individuals (James Hopes in The Tribune, Axar Patel via News9live) and by Cricsheet ball-by-ball data for matchup statistics. However, the analysis suffers from three structural weaknesses: (1) all predicted XIs are speculative, with DC's XI especially divergent across sources; (2) Dharamsala pitch data shows a stark internal contradiction (160 all-time vs 209 since 2023) that is never resolved; and (3) the most impactful data contamination risk is that the orchestrator's stats_snapshot.json and the Cricsheet venue splits queried by the stats analyst are keyed to the WRONG venue (Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur) — which returns 0 matches of venue-specific data. The actual venue is HPCA Stadium, Dharamsala.

**Critical data contamination risks:**

1. **stats_snapshot.json venue is WRONG.** The file lists "Maharaja Yadavindra Singh International Cricket Stadium" with 0 matches analyzed for venue splits, 0 toss data, null averages. This is Mullanpur, not Dharamsala. Any downstream agent ingesting structured venue data from this file will get nulls or, worse, may attempt to fill gaps with Mullanpur assumptions. The entire venue_splits and toss_impact blocks are inapplicable.

2. **Cricsheet venue splits cited in news_conditions.md are explicitly for Yadavindra/Mullanpur (15 matches).** The analyst correctly self-flagged this ("this data is for MULLANPUR, not Dharamsala"), but downstream agents must not treat the spin economy 7.63 vs pace economy 8.95 split as Dharamsala data. It is Mullanpur data and the two grounds have fundamentally different characteristics (Mullanpur is plains; Dharamsala is at 1,457m elevation).

3. **Head-to-head at PBKS home venues (Mohali/Yadavindra) is 7-1 PBKS from 8 matches.** This does NOT include Dharamsala, making it misleading for this specific match.

---

## Claim-by-Claim Audit

| # | Claim | Source | Dated | Rating | Flag |
|---|-------|--------|-------|--------|------|
| 1 | Venue is HPCA Dharamsala, not Mullanpur | ESPNcricinfo; CricketNews; Business Standard | May 2026; May 10 | **confirmed** | Three independent sources unanimous |
| 2 | PBKS last match XI (vs SRH, May 6) | ESPNcricinfo scorecard | May 6, 2026 | **confirmed** | Official scorecard |
| 3 | Omarzai available after rejoining squad | TV9 Hindi; India.com | May 2026; May 11 | **probable** | Two dated sources; no official team announcement |
| 4 | Hopes hints at changes / Omarzai / second spinner | ESPNcricinfo match preview | May 2026 | **probable** | Indirect quote, hedged language |
| 5 | Hopes on Dharamsala pace: bounce, sideways movement | The Tribune, direct interview | May 10, 2026 | **confirmed** | Direct quote, named source, timestamped |
| 6 | Probable PBKS XI — pace-heavy version | InsideSport; Yahoo Sports | May 11, 2026 | **speculative** | Editorial predictions, no management citation |
| 7 | Probable PBKS XI — spin-inclusive (Omarzai in) | India.com | May 11, 2026 | **speculative** | Single source editorial prediction |
| 8 | Bartlett dropped by all sources | InsideSport | May 11, 2026 | **probable** | Consensus across predictions; consistent with poor economy |
| 9 | Chahal vaping controversy; no ban expected | NewsX (May 11); WION (undated) | Partial | **probable** | Two sources; "no ban" is absence-of-evidence claim |
| 10 | Hopes on catching/fielding concerns | The Tribune | May 10, 2026 | **confirmed** | Direct quote from coaching staff |
| 11 | DC last match XI (vs KKR, May 8) | ESPNcricinfo scorecard | May 8, 2026 | **confirmed** | Official scorecard |
| 12 | Axar "next year" quotes; bench player hints | News9live; WION | May 9, 2026 | **confirmed** | Direct captain quotes, identified press conference |
| 13 | Axar criticized spinners for mistakes | News9live | May 9, 2026 | **confirmed** | Direct captain quote, dated |
| 14 | DC XI — Source A (InsideSport: Porel/Miller in) | InsideSport | May 10, 2026 | **speculative** | Single source editorial |
| 15 | DC XI — Source B (Yahoo: Nabi in) | Yahoo Sports | May 11, 2026 | **speculative** | Single source editorial |
| 16 | DC XI — Source C (NewsX: Shaw returns) | NewsX | May 11, 2026 | **speculative** | Highly speculative; Shaw last played 2024 |
| 17 | Shaw return fueled by Axar bench player comments | NewsX | May 11, 2026 | **speculative** | Inferential; no quote links Shaw to selection |
| 18 | DC won toss, elected to field | Outlook India live score | May 11, 2026 | **confirmed** | Reputable outlet; toss ~13:30 UTC, within 13:40 cutoff |
| 19 | Bat-first win rate 64% (9/14) at Dharamsala | Yahoo Sports | May 11, 2026 | **probable** | Single dated source; verifiable; small sample |
| 20 | 14 IPL matches total at HPCA | CricketNews; Business Standard | 2026; May 10 | **probable** | Two sources agree; verifiable |
| 21 | PBKS 6W-8L at Dharamsala; DC 2-2; H2H 2-2 | CricketNews; Business Standard | 2026; May 10 | **probable** | Two sources; specific breakdowns |
| 22 | Avg first-innings score all-time at Dharamsala: ~160 | Yahoo Sports | May 11, 2026 | **probable** | Single dated source; verifiable |
| 23 | Avg first-innings score since 2023: 209 | NewsX | May 11, 2026 | **speculative** | Single mid-tier source; tiny sample; likely distorted by outliers |
| 24 | H2H at PBKS home (Mohali/Yadavindra): 7-1 | Cricsheet | Database | **probable** | Reliable data but EXCLUDES Dharamsala; misleading |
| 25 | Venue splits at Yadavindra: spin 7.63, pace 8.95 | Cricsheet | Database | **probable** | Reliable data but WRONG VENUE (Mullanpur) |
| 26 | KL Rahul vs PBKS bowlers: dominant matchup | Cricsheet ball-by-ball | Database | **confirmed** | Gold standard historical data; specific and granular |
| 27 | Surface slows in second innings | Business Standard | May 10, 2026 | **probable** | Single source; no curator; generic claim |
| 28 | High altitude aids ball travel; pace assistance | NewsX | May 11, 2026 | **probable** | Physics-based claim well-established for Dharamsala |
| 29 | Temperature 19-22°C at match time | Outlook India; NewsX | May 11, 2026 | **probable** | Two dated forecast sources |
| 30 | Rain risk: showers 4-6 PM, clearing by match time | NewsX; Yahoo Sports | May 11, 2026 | **probable** | Two dated sources; broadly consistent |
| 31 | Humidity 50-52% | Outlook India | May 11, 2026 | **probable** | Single dated weather source |
| 32 | Wind 12-13 km/h from ENE | NewsX | May 11, 2026 | **probable** | Single dated source |
| 33 | Dew expected due to mountain temperature drop | Yahoo Sports | May 11, 2026 | **probable** | Plausible given altitude; not quantified |
| 34 | Highest team score at HPCA: RCB 241/7 (2024) | Yahoo Sports | May 11, 2026 | **probable** | Verifiable historical record |
| 35 | PBKS standings: P10 W6 L3 NR1, 13 pts | Outlook India points table | May 11, 2026 | **confirmed** | Corrects stats_snapshot (P9, 12 pts) |
| 36 | DC standings: P11 W4 L7, 8 pts | Outlook India points table | May 11, 2026 | **confirmed** | Updates stats_snapshot (P10) with KKR match |
| 37 | PBKS 3-match losing streak (RR, GT, SRH) | stats_snapshot + multiple sources | Yes | **confirmed** | Verifiable match results |
| 38 | Hopes: "Our tournament starts now" | Asianet Newsable | May 10, 2026 | **confirmed** | Direct quote, dated |
| 39 | DC NRR -1.154 makes playoffs near-impossible | Standings computation | N/A | **probable** | Mathematical inference; NRR figure consistent with results |
| 40 | Reverse fixture: PBKS 265/4 chasing DC 264/2 (Rahul 152) | stats_snapshot; Cricsheet | April 25 | **confirmed** | Multiple data sources for completed match |
| 41 | No curator comments found | Analyst observation | N/A | **confirmed** | Absence noted transparently |
| 42 | PBKS 5 rest days; DC 3 rest days | Schedule/scorecards | Yes | **confirmed** | Factual scheduling |
| 43 | First IPL 2026 match at Dharamsala; 3-game home block | CricketNews | 2026 | **probable** | Verifiable scheduling claim |

---

## Flagged Issues

1. **CRITICAL: stats_snapshot.json and Cricsheet venue splits are for the WRONG VENUE.** The orchestrator's structured data is keyed to Maharaja Yadavindra Singh International Cricket Stadium (Mullanpur), returning 0 matches for venue splits and toss impact. The Cricsheet data queried by the stats analyst (spin eco 7.63, pace eco 8.95 from 15 matches) is also for Mullanpur, NOT Dharamsala. These two grounds are fundamentally different — Mullanpur is a plains venue; Dharamsala is at 1,457m elevation with distinct pace-friendly characteristics. The News Analyst's manually sourced Dharamsala data is the ONLY applicable venue information.

2. **Conflicting first-innings averages at Dharamsala are unresolved.** Yahoo Sports says ~160 all-time; NewsX says 209 since 2023. The 49-run difference is enormous. The 209 figure likely rests on 2-3 recent matches and may be heavily skewed by outliers like RCB's 241/7. Neither figure alone should be used as par.

3. **DC predicted XI is maximally uncertain.** Three sources give three radically different XIs. The only constant across all three is Nissanka, Rahul, Rizvi, Stubbs, Axar, Ashutosh, and Starc. Positions 8-11 are genuinely unknown.

4. **PBKS predicted XI has a binary fork.** Ferguson/Vyshak (pace) vs Omarzai/Brar (all-round/spin) is unresolved. Both scenarios are editorially constructed.

5. **Bat-first win rate 64% (9/14) at Dharamsala is a small sample.** The margin of error is wide. DC's decision to bowl first may or may not be an error.

6. **H2H "at PBKS home" (7-1) excludes Dharamsala.** PBKS vs DC at Dharamsala specifically is 2-2. The 7-1 figure is misleading for this match.

7. **Toss result timestamp is tight against cutoff.** Toss at ~13:30 UTC, cutoff at 13:40 UTC. Within bounds but only by ~10 minutes. Confirmed via Outlook India.

8. **Chahal vaping: WION source is undated.** Low impact on match analysis but noted.

9. **"209 since 2023" figure from NewsX** is presented without sample size. If based on 2-3 matches, a single outlier massively distorts it. Heavily discount.

10. **No pitch curator comments found.** All surface assessments rely on journalists, coaching staff, or generic venue profiles.

---

## Recommendation for Synthesizer

### High-confidence inputs (weight heavily):
- Venue correction to Dharamsala (three independent sources, critical)
- Toss result: DC won, elected to field (Outlook India, confirmed within cutoff)
- Axar Patel's "next year" quotes and bench player rotation hints (direct captain quotes, confirmed)
- James Hopes' direct quotes on Dharamsala pace conditions and catching concerns (The Tribune, confirmed)
- KL Rahul vs PBKS bowlers matchup data (Cricsheet ball-by-ball, gold standard)
- Match results, standings, and recent form (confirmed from scorecards and points tables)
- Last match XIs for both teams (ESPNcricinfo scorecards, confirmed)
- Weather: 19-22°C, rain clearing by match time, dew likely (two dated sources)
- PBKS 3-match losing streak (confirmed match results)

### Moderate-confidence inputs (weight with caution):
- Bartlett dropped (consensus editorial, consistent with poor numbers)
- Omarzai available for selection (two sources, probable, actual selection unconfirmed)
- Dharamsala all-time avg first-innings ~160 (single source, verifiable, small sample)
- Bat-first wins 9/14 (64%) at Dharamsala (verifiable but small sample, wide CI)
- Surface slows in second innings (single source, no curator, generic)
- Dew factor in second innings (plausible given altitude, not quantified)
- PBKS 6W-8L at Dharamsala; DC 2-2; H2H 2-2 at Dharamsala (two sources)

### Discount or disregard:
- All predicted XIs — speculative; DC's XI maximally uncertain
- Prithvi Shaw return — wild speculation, single mid-tier source
- "209 since 2023" first-innings average — tiny sample, single source, distorted
- Venue splits from Cricsheet for Yadavindra/Mullanpur — WRONG VENUE
- H2H at PBKS home 7-1 — excludes Dharamsala; use 2-2 at Dharamsala instead
- stats_snapshot.json venue_splits, toss_impact, at_venue H2H — ALL null/zero, wrong venue
- David Miller in DC XI (InsideSport) — single source, no corroboration

### Widen uncertainty for:
- First-innings par at Dharamsala: 160 vs 209 conflict unresolved, no curator
- DC team composition: captain's "next year" comments + 3 divergent predicted XIs
- PBKS team composition: Omarzai-or-Ferguson fork changes team balance materially
- Dew magnitude and its impact on DC's bowling-first decision
- DC effort/motivation level: unusual strong signal from captain, inherently uncertain impact
- **CRITICAL: The orchestrator's structured venue data is entirely inapplicable.** All venue-specific inferences must come from manually sourced Dharamsala data (14-match sample, no curator, conflicting averages).
