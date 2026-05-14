# Source Quality Assessment: Punjab Kings vs Mumbai Indians

## Overall Evidence Quality: Mixed

The evidence base is heavily reliant on Cricsheet ball-by-ball data (confirmed, high-quality) and Open-Meteo weather forecasts (probable). However, there are no team announcements, press conference quotes, curator comments, or journalist reports. All playing XI predictions are extrapolated from recent selection patterns -- a reasonable methodology but speculative by definition. The absence of any cricket press sources is a notable gap.

## Claim-by-Claim Audit

| # | Claim | Source | Dated | Rating | Flag |
|---|-------|--------|-------|--------|------|
| 1 | PBKS likely XI based on May 6 match | Cricsheet playing XI data | 2026-05-06 | probable | Reasonable extrapolation from last match, but no official confirmation. Selection patterns show rotation (Shashank/Wadhera, Ferguson/Bartlett). |
| 2 | PBKS rotated between Shashank and Wadhera | Cricsheet data, 3 matches | 2026-04-28 to 2026-05-06 | confirmed | Factual selection data from Cricsheet. |
| 3 | Ferguson returned May 6 after rest May 3 | Cricsheet data | 2026-05-06 | confirmed | Factual selection data. |
| 4 | MI last XI (May 4 vs LSG) | Cricsheet playing XI data | 2026-05-04 | confirmed | Factual selection data. |
| 5 | Rohit Sharma returned May 4 after 5-match absence | Cricsheet data | 2026-05-04 | confirmed | Verifiable from match-by-match XI data. |
| 6 | Q de Kock dropped since Apr 29 | Cricsheet data | 2026-05-04 | confirmed | Factual. |
| 7 | MI made 5 changes between May 2 and May 4 | Cricsheet data | 2026-05-04 | confirmed | Factual comparison of two XIs. |
| 8 | Hardik Pandya status uncertain | Cricsheet data | 2026-05-04 | probable | He was dropped May 4 after playing May 2. "Uncertain" is a fair characterization but the reason (injury? tactical?) is unknown. |
| 9 | Venue avg first innings 214.2 in 2026 (4 matches) | Cricsheet venue data | Season 2026 | confirmed | Factual aggregate from match data. Small sample flagged. |
| 10 | 2026 scoring jump of 26% over prior norms | Cricsheet venue data | Multi-season | confirmed | Factual calculation. |
| 11 | Chase vs bat-first: 8-7 in 15 matches | Cricsheet venue data | 2024-2026 | confirmed | Factual aggregate. |
| 12 | Temperature: 36.5C afternoon, 27-29C evening | Open-Meteo API | 2026-05-14 | probable | Weather forecast -- inherently uncertain but from a reputable free API. Forecast for today should be fairly accurate. |
| 13 | Humidity spike to 62% at 6 PM | Open-Meteo API | 2026-05-14 | probable | Weather forecast. The abrupt jump from 25% to 62% in 3 hours is a notable pattern -- could indicate a weather system or could be model artifact. |
| 14 | Dew assessment: moderate, gap ~8-10C | Derived from Open-Meteo | 2026-05-14 | probable | Calculated from temperature and dew-point data. Assessment methodology is sound but the dew-point forecast itself has error bars. |
| 15 | PBKS playoff contention, MI virtually eliminated | Cricsheet standings | 2026-05-14 | confirmed | Factual standings calculation. |
| 16 | Motivation gap between teams | Analyst inference | undated | speculative | Reasonable inference from standings but unmeasurable. "Dead rubber" teams sometimes play better (freedom) or worse (disengagement). This is a narrative claim, not a fact. |
| 17 | Reverse fixture: PBKS won by 7 wickets at Wankhede | Cricsheet data | 2026-04-16 | confirmed | Factual match result. |
| 18 | PBKS lost 3 in a row | Cricsheet data | 2026-04-28 to 2026-05-06 | confirmed | Factual. |
| 19 | MI lost 6 of 8 | Cricsheet data | Season 2026 | confirmed | Factual. |
| 20 | MI's May 4 match showed "strong form" | Analyst editorial | 2026-05-04 | probable | The raw data is confirmed (229/4 chase, Rohit 84, Rickelton 83). The characterization as "MI at their ceiling" is analyst editorializing -- the claim should be "MI scored 229/4 chasing 228" and let downstream agents interpret. |
| 21 | Neither team has fatigue concerns | Cricsheet dates | 2026-05-06/04 | confirmed | 8-day and 10-day gaps are verifiable facts. |
| 22 | Toss-winner-match-winner 66.7% at venue | Cricsheet data | 15 matches | confirmed | Factual aggregate. Sample is reasonable (n=15). |
| 23 | MI's XI is "highly unstable" | Analyst inference | undated | probable | Supported by the confirmed fact of 5 changes in one match cycle. "Highly unstable" is editorial but defensible. |
| 24 | 2026 scoring surge may reflect pitches or lineup quality | Analyst caveat | undated | speculative | Valid uncertainty flagged. n=4 is too small to attribute causation. |

## Flagged Issues

1. **No cricket press sources at all.** Zero articles from Cricbuzz, ESPNcricinfo, or any journalist. All claims derive from Cricsheet data (strong for facts, silent on team news, injuries, tactical signals) and weather API (strong for conditions). The evidence packet has no qualitative intelligence layer.

2. **Playing XI predictions are pattern extrapolation only.** Without team announcements, any XI prediction for this match is speculative. MI's recent rotation history (5 changes in one cycle) makes their XI particularly unpredictable.

3. **"Motivation gap" is an untestable narrative claim.** While standings are confirmed, the inference that MI will be less motivated is speculative. Learning log Entry 7 explicitly warns against the assumption that dead-rubber teams perform worse.

4. **Humidity spike (claim #13) should be treated cautiously.** The 25% to 62% humidity jump in 3 hours is dramatic. If accurate, it suggests meaningful dew. If a forecast artifact, the dew assessment is overstated. This is the biggest weather uncertainty.

5. **Venue scoring data is era-sensitive.** The 2026 average (214.2) is based on only 4 matches. Learning log Entry 11 warns about blending era data. The 2024-2025 average (~169) may be stale for 2026 pitch conditions.

## Recommendation for Synthesizer

- **Weight heavily:** Cricsheet-derived facts (standings, form, H2H, venue splits, playing XI history). These are confirmed and reliable.
- **Weight moderately:** Weather data (probable, with normal forecast uncertainty). Venue 2026 scoring data (confirmed but n=4).
- **Discount heavily:** Motivation/dead-rubber narrative (speculative, contradicted by Entry 7 in learning log). Specific playing XI predictions (speculative, especially for MI).
- **Widen bands because:** No press intelligence, no injury updates, no confirmed XIs. MI's XI is particularly unpredictable. The evidence quality gap means more surprises are possible on match day.
