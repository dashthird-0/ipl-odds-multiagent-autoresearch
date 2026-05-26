# Source Quality Assessment: Royal Challengers Bengaluru vs Gujarat Titans

## Overall Evidence Quality: Mixed

The News & Conditions Analyst has done excellent work identifying and correcting a critical venue error (Chinnaswamy vs Dharamsala) — this is the most important analytical contribution, supported by 5+ independent sources. However, the underlying data packet is severely compromised: ALL statistical venue splits, toss impact data, and venue-specific H2H records apply to the wrong ground. The news-sourced evidence is adequate for qualitative assessments (pitch character, weather, team news) but lacks the statistical foundation normally provided by the stats snapshot. The conflicting weather data (news vs wttr.in API) introduces additional uncertainty. Phil Salt's non-selection is confirmed post-toss, which is within the evidence cutoff window.

## Claim-by-Claim Audit

### Venue Correction

| # | Claim | Source | Dated | Rating | Flag |
|---|-------|--------|-------|--------|------|
| 1 | Venue is HPCA Stadium, Dharamsala (not Chinnaswamy) | News18, CricToday, CricketAddictor, IPL official, Google News (5+ sources) | 2026-05-26 | confirmed | Multiple independent sources unanimously agree |
| 2 | This is Qualifier 1, not a league match | CricToday, News18, Google News | 2026-05-26 | confirmed | Factual, verifiable from tournament structure |
| 3 | Winner advances to IPL 2026 Final | CricToday | 2026-05-26 | confirmed | Tournament structure fact |

### Season Standings & Form

| # | Claim | Source | Dated | Rating | Flag |
|---|-------|--------|-------|--------|------|
| 4 | RCB topped league stage with 18 points | CricToday, News18, CricketAddictor | 2026-05-26 | confirmed | Multiple sources agree |
| 5 | GT finished with 18 points, top-two | CricketAddictor, CricToday | 2026-05-26 | confirmed | Multiple sources agree |
| 6 | RCB lost final league match vs SRH | CricketAddictor | 2026-05-26 | probable | Single source but verifiable from scorecards |
| 7 | GT won final league match vs CSK | CricketAddictor | 2026-05-26 | probable | Single source but verifiable from scorecards |

### Updated Player Stats

| # | Claim | Source | Dated | Rating | Flag |
|---|-------|--------|-------|--------|------|
| 8 | Kohli 557 runs this season | CricToday | 2026-05-26 | probable | Single source; CricToday is tier-2 but stat is verifiable. Consistent with trajectory (379 in 10 matches, ~557 in 14) |
| 9 | Sudharsan 638 runs, Orange Cap holder | CricToday | 2026-05-26 | probable | Single source; extraordinary claim (253 more runs in ~4 more matches = 63 avg) but consistent with his league-stage form |
| 10 | Gill 616 runs | CricToday | 2026-05-26 | probable | Single source; 238 more runs in ~4 matches is high but plausible |
| 11 | Rashid Khan 19 wickets | CricToday | 2026-05-26 | probable | Single source; 8 more wickets in ~4 matches is high but plausible for a spinner |
| 12 | Bhuvneshwar joint-top wicket-taker | CricToday | 2026-05-26 | probable | Single source; if Rabada is also joint-top, this is consistent |
| 13 | Venkatesh Iyer 73* and 44 in last two games | CricToday | 2026-05-26 | probable | Single source; specific match performances, plausible |

### Toss Result

| # | Claim | Source | Dated | Rating | Flag |
|---|-------|--------|-------|--------|------|
| 14 | GT won toss, chose to bowl first | Google News live score title | 2026-05-26 | confirmed | Live score data; toss results are factual. Title: "RCB asked to bat first" |
| 15 | Phil Salt not in starting XI | Google News live score title "Salt still out" | 2026-05-26 | confirmed | Post-toss confirmation |

### Pitch Report

| # | Claim | Source | Dated | Rating | Flag |
|---|-------|--------|-------|--------|------|
| 16 | True bounce, excellent carry, paradise for pacers early | News18 | 2026-05-26 | probable | Consistent with multiple sources; News18 is reputable. Generic pitch character description. |
| 17 | Par score 180-195 | News18 | 2026-05-26 | speculative | Single source, no methodology cited. Conflicts with CricToday's "200+" claim. |
| 18 | Par score 200+ in IPL 2026 at Dharamsala | CricToday | 2026-05-26 | speculative | Single source; "average first innings total around 200+" is vague. No match-by-match data cited. |
| 19 | "Pace and bounce on offer, Gujarat have edge" | NDTV | 2026-05-26 | speculative | Editorial assessment, not factual. Headline opinion. |
| 20 | RCB 2W-1L at Dharamsala in IPL | CricToday | 2026-05-26 | probable | Verifiable from scorecards but not cross-checked |
| 21 | GT never played at Dharamsala in IPL | CricToday | 2026-05-26 | probable | Verifiable; negative claim hard to definitively confirm |
| 22 | High altitude helps ball travel further | CricToday | 2026-05-26 | confirmed | Established physics fact about Dharamsala |
| 23 | Dew later makes defending difficult | CricketAddictor, IPL official | 2026-05-26 | speculative | Generic venue narrative. Contradicted by wttr.in dew-point data showing -5C to -1C (dew physically impossible). See weather conflicts below. |
| 24 | 100% chasing win rate in RCB-GT H2H | News18 | 2026-05-26 | speculative | Statistically this means 8/8 matches — an extraordinary claim. More likely refers to chasing wins at this venue or a subset. Unsupported by sample-size context. |

### Weather

| # | Claim | Source | Dated | Rating | Flag |
|---|-------|--------|-------|--------|------|
| 25 | Temperature 18-21C at match time | News18 | 2026-05-26 | probable | Weather forecast. wttr.in shows 25C at 1800hrs IST, 19C at 2100hrs — broadly consistent for late evening. |
| 26 | 25% chance of moderate rain | News18 | 2026-05-26 | speculative | Conflicts with wttr.in showing 0% during 1500-1800hrs. May refer to later evening. Different forecast models can vary. |
| 27 | "80 Per Cent Rain Threat" | Google News title (publication unknown) | 2026-05-26 | speculative | Dramatic headline without cited forecast model. Conflicts sharply with News18's 25% and wttr.in's 0%. |
| 28 | Humidity 55-65% | News18 | 2026-05-26 | speculative | **SHARPLY CONFLICTS** with wttr.in showing 11-18% during match hours. Gap too large for normal forecast error. One source is wrong. |
| 29 | Dew point -5C to -1C during evening | wttr.in API | 2026-05-26 | probable | Real-time weather API with hourly data. At these dew points, dew formation is physically impossible — surface temperature would need to drop well below these dew points for condensation. |
| 30 | Mountain breeze, cloud cover assists swing | News18 | 2026-05-26 | probable | Consistent with Dharamsala's known conditions. Cloud cover varies by forecast. |

## Flagged Issues

1. **CRITICAL: Wrong venue in evidence packet** — All statistical data (venue splits, toss impact, venue H2H) from stats_snapshot.json applies to M Chinnaswamy Stadium, Bengaluru. The match is at HPCA Stadium, Dharamsala. This is the tenth occurrence of Entry 13's venue verification failure. Every venue-specific number in the stats snapshot must be discarded.

2. **Stale stats snapshot** — Covers 10 of 14 league matches. Player stats have changed materially (GT's bowlers especially: Rashid +8 wickets, Siraj +6 wickets). Updated stats from CricToday are single-sourced.

3. **Irreconcilable weather data** — News18 (55-65% humidity) vs wttr.in (11-18% humidity) is a 40-50 percentage point discrepancy. This cannot be normal forecast variation. The dew narrative in preview articles (CricToday, CricketAddictor, IPL official) may be generic venue lore rather than same-day analysis. wttr.in's dew point data (-5C to -1C) suggests dew is physically impossible tonight, which would invalidate the "dew advantage for chasing team" narrative that multiple sources cite.

4. **Par score conflict** — 180-195 (News18) vs 200+ (CricToday). This is a meaningful gap that affects how we assess batting-first difficulty. Neither source provides match-by-match evidence.

5. **"100% chasing win rate" claim** — News18's claim that chasing teams have a 100% win rate in RCB-GT H2H is likely misattributed or refers to a subset. The stats snapshot shows the overall H2H as 4-4, and the analyst notes all 8 matches — it is unlikely every single one was won by the chasing team. This claim should be treated with high skepticism.

6. **Toss known post-evidence-cutoff ambiguity** — The toss occurred at approximately 13:30 UTC and the evidence cutoff is 13:40 UTC. The toss result is within the cutoff window and can be used. GT chose to bowl, which is the standard Dharamsala choice per multiple sources.

## Recommendation for Synthesizer

- **Weight heavily**: Venue correction (confirmed), toss result (confirmed), Phil Salt out (confirmed), match stakes as Qualifier 1 (confirmed), updated standings (confirmed)
- **Use with caution**: Updated player stats from CricToday (single-sourced but plausible), pitch character descriptions (consistent across multiple sources), GT's bowling strength narrative
- **Discount heavily**: Specific par scores (conflicting), dew narrative (contradicted by wttr.in API data), "80% rain threat" headline, "100% chasing win rate" claim, humidity figures (irreconcilable conflict)
- **Widen band for**: Wrong-venue data gap (no reliable Dharamsala statistical splits), weather uncertainty, par score uncertainty, GT's zero Dharamsala experience
