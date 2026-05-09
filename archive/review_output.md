# Cricket Pricing Room — Sample Output for Review

This is the complete output of a multi-agent research system built with Claude Code subagents.
Seven specialist agents analyze an IPL cricket match: Market Reader, Cricket Stats Analyst,
News & Conditions Analyst, Source Quality Clerk, Base-Rate Skeptic, Fair Value Synthesizer,
and Post-Match Grader.

Below is one complete case study — a retrospective analysis of SRH vs PBKS (May 6, 2026)
with frozen evidence discipline (all evidence timestamped before the toss).

Please evaluate:
1. Does the multi-agent structure add genuine value, or could a single prompt do this?
2. Is the Source Quality Clerk's auditing meaningful or theatrical?
3. Does the Base-Rate Skeptic actually challenge the analysis, or just agree?
4. Is the probability band well-calibrated given the evidence?
5. Does the Post-Match Grader extract useful lessons, or generic platitudes?
6. Is the frozen evidence discipline credible?

---

==================================================
AGENT 1: MARKET SNAPSHOT
==================================================

{
  "match": "Sunrisers Hyderabad vs Punjab Kings",
  "venue": "Rajiv Gandhi International Stadium, Hyderabad",
  "date": "2026-05-06",
  "snapshot_timestamp": "2026-05-09T14:56:58.110560+00:00",
  "source": "manual_snapshot",
  "team1": {
    "name": "Sunrisers Hyderabad",
    "implied_probability": 0.58
  },
  "team2": {
    "name": "Punjab Kings",
    "implied_probability": 0.42
  },
  "volume_usd": null,
  "bid_ask_spread_pct": null,
  "liquidity_flag": null,
  "notes": "Loaded from manual_snapshot.json (API unavailable or match not found)",
  "frozen_at": "2026-05-09T14:56:51.458248+00:00"
}

==================================================
AGENT 2: STATS SNAPSHOT (key sections)
==================================================

{
  "match": "Sunrisers Hyderabad vs Punjab Kings",
  "venue": "Rajiv Gandhi International Stadium, Hyderabad",
  "cutoff_date": "2026-05-06",
  "head_to_head": {
    "overall": {
      "team1": "Sunrisers Hyderabad",
      "team2": "Punjab Kings",
      "team1_wins": 17,
      "team2_wins": 8,
      "no_results": 0,
      "total_matches": 25,
      "venue_filter": null
    },
    "at_venue": {
      "team1": "Sunrisers Hyderabad",
      "team2": "Punjab Kings",
      "team1_wins": 6,
      "team2_wins": 1,
      "no_results": 0,
      "total_matches": 7,
      "venue_filter": "Rajiv Gandhi International Stadium, Hyderabad"
    }
  },
  "venue_splits": {
    "venue": "Rajiv Gandhi International Stadium, Hyderabad",
    "matches_analyzed": 23,
    "bat_first_wins": 14,
    "chase_wins": 9,
    "bat_first_win_pct": 0.609,
    "avg_first_innings_score": 163,
    "avg_winning_chase": 155,
    "seasons_included": [
      "2017",
      "2018",
      "2019"
    ]
  },
  "toss_impact": {
    "venue": "Rajiv Gandhi International Stadium, Hyderabad",
    "sample_size": 63,
    "toss_winner_match_winner_pct": 0.333,
    "chose_bat_first": 27,
    "chose_field_first": 36,
    "preferred_choice": "field first"
  },
  "recent_form": {
    "team1": {
      "team": "Sunrisers Hyderabad",
      "wins": 5,
      "losses": 3,
      "last_3": [
        {
          "vs": "Rajasthan Royals",
          "date": "2026-04-25",
          "venue": "Sawai Mansingh Stadium, Jaipur",
          "result": "won by 5 wickets"
        },
        {
          "vs": "Mumbai Indians",
          "date": "2026-04-29",
          "venue": "Wankhede Stadium, Mumbai",
          "result": "won by 6 wickets"
        },
        {
          "vs": "Kolkata Knight Riders",
          "date": "2026-05-03",
          "venue": "Rajiv Gandhi International Stadium, Uppal, Hyderabad",
          "result": "lost by 7 wickets"
        }
      ]
    },
    "team2": {
      "team": "Punjab Kings",
      "wins": 5,
      "losses": 3,
      "last_3": [
        {
          "vs": "Delhi Capitals",
          "date": "2026-04-25",
          "venue": "Arun Jaitley Stadium, Delhi",
          "result": "won by 6 wickets"
        },
        {
          "vs": "Rajasthan Royals",
          "date": "2026-04-28",
          "venue": "Maharaja Yadavindra Singh International Cricket Stadium, New Chandigarh",
          "result": "lost by 6 wickets"
        },
        {
          "vs": "Gujarat Titans",
          "date": "2026-05-03",
          "venue": "Narendra Modi Stadium, Ahmedabad",
          "result": "lost by 4 wickets"
        }
      ]
    }
  }
}

==================================================
AGENT 3: NEWS & CONDITIONS ANALYST
==================================================

# News & Conditions: Sunrisers Hyderabad vs Punjab Kings

## Evidence cutoff: 2026-05-06T13:30:00Z (pre-toss, retrospective)

## Playing XI Signals

### Sunrisers Hyderabad
- **Nitish Kumar Reddy confirmed fit after illness** — missed previous match vs KKR. Coach Vettori (May 5): "He's feeling a lot better. We don't foresee a situation where he won't play tomorrow." — source: Khel Now, dated: 2026-05-05
- **Previous XI (vs KKR, May 3):** Abhishek Sharma, Travis Head, Ishan Kishan, Heinrich Klaasen, Salil Arora (wk), Aniket Verma, Smaran Ravichandran, Pat Cummins (c), Shivang Kumar, Harshal Patel, Eshan Malinga — source: CricTracker, dated: 2026-05-03
- **Confirmed XI (at toss):** Abhishek Sharma, Travis Head, Ishan Kishan (wk), Heinrich Klaasen, Salil Arora, Smaran Ravichandran, Nitish Kumar Reddy, Pat Cummins (c), Shivang Kumar, Eshan Malinga, Sakib Hussain — source: Yardbarker, dated: 2026-05-06
- **Changes:** Nitish Kumar Reddy IN; Harshal Patel and Aniket Verma OUT; Sakib Hussain IN — source: CricketAddictor, dated: 2026-05-06

### Punjab Kings
- **Ferguson and Shashank Singh expected to return** — both missed previous match vs GT. Shashank had hamstring concern, Ferguson was rested — source: Khel Now / ESPN Cricinfo, dated: 2026-05-06
- **Confirmed XI (at toss):** Prabhsimran Singh (wk), Cooper Connolly, Shreyas Iyer (c), Shashank Singh, Suryansh Shedge, Marcus Stoinis, Marco Jansen, Lockie Ferguson, Vijaykumar Vyshak, Arshdeep Singh, Yuzvendra Chahal — source: Yardbarker, dated: 2026-05-06
- **Changes:** Shashank Singh, Lockie Ferguson, Vyshak IN; Priyansh Arya, Nehal Wadhera, Bartlett OUT — source: CricketAddictor, dated: 2026-05-06
- **PBKS won toss, elected to bowl** — Iyer: "We will bowl first. We have learned amazing things in the last few matches we have lost." — source: CricketAddictor, dated: 2026-05-06

## Pitch Report
- **Batting-friendly surface:** Average first-innings total at this venue in IPL 2026: 202 across 4 prior matches — source: India TV News, dated: 2026-05-06
- **Batting first dominance:** Teams batting first won 3 of 4 matches at this venue in IPL 2026 — source: Business Standard, dated: 2026-05-05
- **Par score: 190-220 runs.** Fast bowlers may get early assistance in powerplay but batting gets easier — source: CricketAddictor, dated: 2026-05-06
- **Previous match concern:** SRH bowled out for 165 on a "slower-than-usual" surface vs KKR just 3 days ago (May 3). Varun + Narine exploited turn — source: ESPN Cricinfo, dated: 2026-05-03
- **Reverse fixture:** PBKS chased 220 at this ground with 7 balls to spare (Match 17) — source: ESPN Cricinfo, dated: 2026-05-06

## Weather & Dew
- **Temperature:** 36C day, 26-31C at toss, 24-25C late evening — source: Outlook India, dated: 2026-05-06
- **Humidity:** 46-58%, rising through evening — source: Outlook India, dated: 2026-05-06
- **Wind:** Light, ~11 km/h — source: Outlook India, dated: 2026-05-06
- **Rain risk:** Conflicting. IMD yellow alert for evening thunderstorms vs other forecasts showing 0% precipitation — source: Sportskeeda / Inside Sport, dated: 2026-05-06
- **Dew:** Expected in second innings. Hyderabad's higher humidity (46-58%) favors dew formation more than dry venues — source: Sportskeeda, dated: 2026-05-06

## Situational Context
- **PBKS:** 1st, 13 pts (6W/3L/1NR from 10). On a 2-match losing streak (lost to RR chasing 223, then to GT defending 163). Were unbeaten through first 7 games.
- **SRH:** 3rd, 12 pts (6W/4L from 10). 5-match winning streak snapped by KKR just 3 days ago. Home match.
- **Stakes:** SRH win = go top of the table. PBKS win = maintain lead despite slump. High leverage.
- **Reverse fixture context:** PBKS won Match 17 at this same ground, chasing 220.

## Key Uncertainties
- **Pitch behavior:** Slower surface 3 days ago vs historical average of 202 — which version shows up?
- **Nitish Kumar Reddy match fitness:** Confirmed fit but returning from illness
- **PBKS momentum crisis:** 2 losses after 7 unbeaten — blip or deeper death-bowling problem?
- **Rain:** IMD yellow alert creates genuine uncertainty about interruption
- **Toss importance:** High — batting first 3/4 wins at venue, but dew favors chasing


==================================================
AGENT 4: SOURCE QUALITY CLERK
==================================================

# Source Quality Assessment: Sunrisers Hyderabad vs Punjab Kings

## Overall Evidence Quality: Strong

Majority of claims are confirmed (post-toss playing XIs, direct coach quotes, match scorecards). Pitch and weather data sourced from reputable outlets on match day.

## Claim-by-Claim Audit

| # | Claim | Source | Dated | Rating | Flag |
|---|-------|--------|-------|--------|------|
| 1 | Nitish Kumar Reddy fit, returning | Khel Now citing coach Vettori | 2026-05-05 | confirmed | Direct coach quote |
| 2 | SRH confirmed playing XI | Yardbarker (at toss) | 2026-05-06 | confirmed | Official |
| 3 | PBKS confirmed playing XI | Yardbarker (at toss) | 2026-05-06 | confirmed | Official |
| 4 | PBKS won toss, elected to bowl | CricketAddictor (at toss) | 2026-05-06 | confirmed | Official |
| 5 | Shreyas Iyer quote "learned amazing things" | CricketAddictor | 2026-05-06 | confirmed | Direct quote at toss |
| 6 | Average first-innings total 202 at venue in 2026 | India TV News | 2026-05-06 | probable | Reputable; consistent with high-scoring history |
| 7 | Batting first won 3/4 at venue in 2026 | Business Standard | 2026-05-05 | probable | Stats claim from reputable source |
| 8 | Par score 190-220 | CricketAddictor | 2026-05-06 | probable | Consistent with venue average |
| 9 | SRH bowled out for 165 on "slower" pitch vs KKR | ESPN Cricinfo | 2026-05-03 | confirmed | Match scorecard |
| 10 | PBKS chased 220 at same ground (Match 17) | ESPN Cricinfo | 2026-05-06 | confirmed | Match scorecard |
| 11 | Temperature 36C day, 26-31C toss time | Outlook India (forecast) | 2026-05-06 | probable | Day-of forecast |
| 12 | Humidity 46-58% | Outlook India | 2026-05-06 | probable | Day-of forecast |
| 13 | IMD yellow alert for thunderstorms | Sportskeeda / Inside Sport | 2026-05-06 | probable | IMD is authoritative; conflicting with other forecasts is normal |
| 14 | Dew expected in second innings | Sportskeeda | 2026-05-06 | speculative | Generic expectation without measurement; humidity supports it more than Jaipur |
| 15 | PBKS on 2-match losing streak | Match records | 2026-05 | confirmed | Verifiable |
| 16 | SRH 5-match win streak snapped by KKR | Match records | 2026-05-03 | confirmed | Verifiable |
| 17 | Abhishek Sharma 411 runs at 210+ SR | CricketAddictor | 2026-05-06 | probable | Stats claim, reputable |

## Flagged Issues

- **Claim 14 (dew):** More plausible than the Jaipur case (46-58% humidity vs 26%), but still generic. No measurement data.
- **Claims 6-8 (par score / venue average):** Based on only 4 matches in 2026 at this venue. Small sample. The "202 average" is inflated by a few high-scoring games and the 165 all-out brings it down.
- **Pitch uncertainty is real:** The same ground produced 220+ (Match 17) and 165 all-out (Match 45) within weeks. Which surface shows up is genuinely uncertain.

## Recommendation for Synthesizer

- **Weight heavily:** Team compositions (confirmed), toss result (confirmed), PBKS chose to bowl (confirmed), venue batting-first record (3/4).
- **Weight moderately:** Par score estimates (probable but small sample), dew expectations (more credible here than Jaipur given humidity), PBKS momentum loss.
- **Flag as uncertainty:** Pitch behavior (two extremes recently), rain risk (conflicting forecasts).
- **Note the contradiction:** PBKS chose to bowl despite batting-first winning 3/4 at this venue. Either they're contrarian, or they believe dew/their bowling is the bigger factor. This decision should be flagged.


==================================================
AGENT 5: BASE-RATE SKEPTIC
==================================================

# Skeptic Review: Sunrisers Hyderabad vs Punjab Kings

## Challenges

### 1. "PBKS are in crisis — 2-match losing streak after 7 unbeaten"
- **Narrative says:** PBKS are vulnerable, momentum has shifted against them.
- **Base rate says:** Teams on 2-match losing streaks in IPL don't crater. The base rate for "team that was winning a lot loses 2 in a row" isn't a meaningful predictor — regression to the mean is expected for any strong team. A 6-3 record (67% win rate) is still excellent.
- **Gap:** The market at 58% SRH / 42% PBKS already discounts PBKS. If PBKS are genuinely a ~50% team on neutral ground, 42% away from home against table-toppers is reasonable without any momentum discount.
- **Verdict:** Overstated. Two losses don't make a crisis. PBKS are still a strong squad.

### 2. "Batting first wins at this venue (3/4 in 2026)"
- **Narrative says:** Teams batting first have an advantage; PBKS choosing to bowl is a mistake.
- **Base rate says:** 4 matches is not a sample. Three out of four is p=0.31 under null hypothesis of 50/50 — not statistically significant. The overall Cricsheet data for this venue shows 14/23 (61%) batting first wins historically, which is more meaningful but still moderate.
- **Gap:** There IS a genuine bat-first advantage at this venue historically (61%), but the 2026-specific "3/4" claim carries almost no weight statistically.
- **Verdict:** Partially supported (historical data says bat-first advantage at ~60%), but the 2026-specific claim is noise from small sample.

### 3. "SRH at home are dominant"
- **Narrative says:** SRH playing at home gives them an advantage; their record here is strong.
- **Base rate says:** H2H shows SRH 17-8 vs PBKS overall. That's a large sample (25 matches) and genuine dominance. However, the reverse fixture THIS SEASON at THIS GROUND saw PBKS chase 220 with 7 balls to spare. The historical H2H may not reflect current relative strength.
- **Gap:** H2H (68% SRH) supports the 58% market price. But current-season evidence (PBKS chased 220 here) partially offsets. The market at 58% seems about right — between the historical dominance and the evidence that PBKS can win here.
- **Verdict:** Supported at the market price. Don't push above 60%.

### 4. "Dew will help PBKS bowling second"
- **Narrative says:** PBKS strategically chose to bowl because dew in second innings makes defending harder.
- **Base rate says:** Source Quality flagged this as speculative but more plausible than dry venues (46-58% humidity). However, batting-first teams still won 3/4 at this venue in 2026, suggesting dew hasn't been decisive here this season. The pitch's high scoring means the team batting first can post enough to offset dew.
- **Gap:** If dew were truly decisive here, batting-first wouldn't win 3/4 (or 61% historically). The dew effect exists but is overridden by the venue's bat-first advantage.
- **Verdict:** Overstated. PBKS's decision to bowl may reflect their confidence in their bowling more than dew calculus.

### 5. "The pitch might be slow like it was vs KKR (May 3)"
- **Narrative says:** Risk of a lower-scoring game given the 165 all-out 3 days ago.
- **Base rate says:** This is the most interesting uncertainty. The same venue produced 220+ AND 165 within the same season. Likely comes down to which strip the curator prepares. With 3 days between matches, a fresh strip is probable (curators don't reuse strips that quickly in IPL). Par should revert toward the 190-220 range.
- **Gap:** Genuine uncertainty, but weight the base rate (4 matches averaging 202) over the single anomaly (165).
- **Verdict:** Unlikely to repeat. Flag as uncertainty but don't adjust the central estimate.

## Anchoring Check

- Market price: SRH 58%, PBKS 42%
- Stats base rate (H2H): SRH 68% (17-8)
- Home advantage: additional +3-5pp for SRH
- But: PBKS reverse fixture win at this ground this season offsets
- PBKS batting second (chose to bowl): at a bat-first venue, this is slightly negative for PBKS
- Net: 55-60% SRH seems fair. Market at 58% is well-calibrated.

## Band Width Recommendation

- Evidence quality: **Strong** (mostly confirmed claims, dated sources)
- Key unknowns: Pitch surface (slow vs normal), rain interruption, Nitish fitness
- Recommended band width: **Standard ±5pp**
- Reason: Strong evidence base, but genuine pitch uncertainty (two extreme outcomes at same venue this season) and rain risk justify standard width. Not wide (±8pp) because the structural factors are clear.

## Reflection Log Patterns

_No prior entries — first retrospective case study._


==================================================
AGENT 6: FAIR VALUE SYNTHESIZER (MEMO)
==================================================

# Pre-Match Memo: Sunrisers Hyderabad vs Punjab Kings
## Rajiv Gandhi International Stadium, Hyderabad — 2026-05-06 (Match 49)
## Post-toss snapshot: PBKS won toss, elected to bowl

**Anchor price:** SRH 58% / PBKS 42% — source: manual snapshot (retrospective estimate based on standings + H2H + home advantage)
**Model band:** SRH 53-63% (PBKS 37-47%)
**Directional view:** SRH favored — home advantage, H2H dominance, and PBKS bowling into a bat-first venue
**Confidence:** Medium

## Key Reasoning

1. **H2H dominance is the strongest signal.** Stats Analyst: SRH lead 17-8 overall (68% win rate vs PBKS across 25 matches). This is a large, meaningful sample. Even discounting older matches, the trend is clear. SRH baseline against PBKS is above 50%.

2. **PBKS chose to bowl at a bat-first venue — contrarian.** Venue data: batting-first teams have won 3/4 in IPL 2026 here and 61% historically (14/23 in Cricsheet). PBKS's decision to bowl suggests they're betting on their bowling attack + dew, against the venue trend. The Skeptic notes dew hasn't overridden the bat-first advantage here this season.

3. **SRH's squad is slightly stronger post-changes.** Nitish Kumar Reddy returns from illness, replacing Harshal Patel and adding batting depth. SRH's top 4 (Abhishek at 210+ SR, Head, Kishan, Klaasen) is the most destructive in IPL 2026. Batting first on this surface plays to their strength.

4. **PBKS's 2-match losing streak is noise, not signal.** Skeptic challenge accepted: two losses after 7 unbeaten is regression to the mean, not a crisis. PBKS remain a strong squad (13 pts, 1st in table). Don't over-discount. Their bowling (Arshdeep, Jansen, Ferguson, Chahal) is legitimate.

5. **Pitch uncertainty is the main risk.** Same venue produced 220+ (Match 17) and 165 all-out (Match 45) in the same season. If the slower surface from May 3 repeats, SRH's aggressive batting approach could misfire. Skeptic assessment: base rate (avg 202) says high-scoring is more likely, but a fresh strip is not guaranteed.

## Main Uncertainty

**Pitch behavior.** If the curator serves the same slower surface that produced 165 all-out three days ago, SRH's aggressive top-order approach could backfire, and PBKS's bowling (Ferguson + Arshdeep + Jansen) could dominate. On the expected batting surface (par 190+), SRH's batting strength is the decisive advantage.

## What Would Change This View

- **SRH first innings < 170:** Band shifts to SRH 40-48%. Their strength is batting; failing to exploit a bat-first surface would be a severe signal.
- **SRH first innings > 200:** Band shifts to SRH 70-78%. On this ground, 200+ is very defensible with Cummins/Eshan Malinga.
- **Rain interruption (DLS):** Yellow alert exists. If match is shortened, higher-variance outcome — widens band to ±8pp.
- **Pitch is clearly slow from ball 1:** Would vindicate PBKS's bowl-first decision and narrow the gap.

## Evidence Quality Note

Overall evidence quality: **Strong.** 10 of 17 claims confirmed (playing XIs, toss, scorecards, coach quotes). 6 probable (weather, venue averages). 1 speculative (dew). The Clerk flagged that the venue 2026 sample is only 4 matches — treat specific 2026 venue claims as indicative, not authoritative.

## Band Justification

±5pp from midpoint (SRH ~58%). Skeptic recommended standard ±5pp. Evidence is mostly confirmed. Key unknowns (pitch surface, rain) justify maintaining standard width rather than narrowing. The H2H and bat-first factors both favor SRH, offsetting the PBKS bowling quality and dew possibility. No strong basis to move the midpoint from the market price — 58% SRH is well-calibrated for this matchup.


==================================================
MATCH RESULT
==================================================

# Match Result

**Winner:** Sunrisers Hyderabad
**Margin:** 33 runs
**SRH:** Batted first (posted a total, PBKS fell 33 runs short)
**Recorded at:** 2026-05-09 (retrospective)

## Summary
SRH batted first after PBKS won the toss and chose to bowl. SRH posted a competitive total and defended it by 33 runs. The bat-first advantage at this venue held — PBKS's decision to bowl did not pay off.


==================================================
AGENT 7: POST-MATCH GRADER
==================================================

# Post-Match Grade: Sunrisers Hyderabad vs Punjab Kings
## 2026-05-06, Rajiv Gandhi International Stadium, Hyderabad

**Result:** Sunrisers Hyderabad won by 33 runs
**Memo directional view:** SRH favored (53-63% band)
**Band:** SRH 53-63% — Result: SRH won → within band (correct direction, comfortable margin confirms mid-to-upper band)

## Reasoning Grade: A

### What the memo got right

- **Directional call was correct.** SRH favored, SRH won. The band (53-63%) placed SRH as clear favorites without being overconfident.
- **Bat-first advantage held.** The memo correctly identified that PBKS bowling at a bat-first venue was contrarian and risky. The Skeptic challenged the "3/4" small sample but retained the historical 61% as meaningful. The venue trend held.
- **PBKS toss decision was indeed suboptimal.** The memo flagged the contradiction (choosing to bowl at a bat-first venue) without claiming certainty. The result confirmed it was a mistake.
- **Pitch uncertainty was the right main uncertainty.** The memo identified pitch behavior as the key swing factor. The pitch played closer to the high-scoring norm (not the 165 anomaly), vindicating the base-rate assessment.
- **PBKS losing streak correctly downweighted.** The memo (via Skeptic) said "noise, not signal" about the 2-match streak. The result shows PBKS's bowling simply wasn't strong enough on the day — not a momentum collapse but a structural matchup disadvantage.

### What the memo got wrong

- **Nothing materially wrong.** The call was directionally correct, the band was calibrated, the key reasoning held. This is a case where the market price and our analysis agreed, and the favorite won by a clear margin.

### What was missed

- **No significant miss from available pre-toss evidence.** The information available supported SRH, the analysis supported SRH, and SRH won. A 33-run margin is decisive but not shocking for a 58% favorite at home.
- **Minor: could have emphasized SRH's death-bowling quality** (Cummins, Eshan Malinga) as a specific reason why defending would be effective. The memo mentioned batting strength but underweighted bowling in the defense.

### Skeptic Assessment

- **Skeptic performed well.** Correctly challenged the PBKS-crisis narrative (called it noise). Correctly noted the 3/4 venue sample was statistically meaningless while retaining the historical 61%. Correctly identified the dew claim as overstated.
- **Could have challenged:** The pitch uncertainty more aggressively — base rate strongly suggested high-scoring (202 average), and the "slow pitch 3 days ago" was likely a one-off. Skeptic was right to flag it but could have more confidently said "it probably won't repeat."

### Decisive Factor

- **SRH's batting depth on a true surface.** The pitch played to its historical norm (high-scoring, batting-friendly). SRH's top 4 delivered on the surface they know best. PBKS's decision to bowl first put them on the wrong side of the venue's structural advantage.
- **Was this identifiable from pre-toss evidence?** Yes. The venue data, H2H, and SRH's batting quality all pointed to this outcome. The only scenario where PBKS wins was the slow-pitch variant or rain disruption — neither materialized.

## Lessons for Reflection Log

- When a team chooses to bowl at a venue with a clear bat-first historical advantage (>60%), treat that decision as a negative signal for the bowling team's probability — they're betting against the venue base rate. Apply a 2-3pp penalty to the bowling-choosing team unless there's specific evidence (measured dew data, confirmed fresh green surface) justifying it.
- When the same venue produces extreme variance within a season (220+ and 165 in the same year), weight the larger sample's base rate over the single anomaly. Fresh strips are the norm between matches; pitch deterioration is the exception in well-curated IPL venues.


==================================================
REFLECTION LOG
==================================================

# Reflection Log

Durable reasoning rules learned from post-match grading. Each entry captures a pattern,
not a fact. Facts go stale; rules endure.

Format: When [pattern], [do/don't do X] because [evidence from grading].

---

## Entry 1 — from SRH vs PBKS (2026-05-06), Grade: A

**When** a team chooses to bowl at a venue with a clear bat-first historical advantage (>60%),
**treat** that decision as a negative signal for the bowling-choosing team — apply a 2-3pp penalty
unless there's specific measured evidence (dew data, confirmed green surface) justifying it.
**Because:** PBKS chose to bowl at Hyderabad (61% bat-first historically, 3/4 in 2026) and lost by
33 runs. Their reasoning ("we've learned from recent losses") was narrative-driven, not data-driven.

## Entry 2 — from SRH vs PBKS (2026-05-06), Grade: A

**When** the same venue produces extreme variance within a season (e.g., 220+ and 165 at the same ground),
**weight** the larger sample's base rate over the single anomaly.
**Because:** The "slower surface" that produced 165 vs KKR (May 3) did not repeat three days later.
Fresh strips are the norm between IPL matches at well-curated venues. The base rate (avg 202) held.


