"""
Cricsheet IPL query tool.

Loads all IPL match JSON files into memory and provides query functions
for the Cricket Stats Analyst agent. All queries enforce a cutoff_date
parameter to prevent future data leakage in retrospective case studies.
"""

import json
import os
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass, field

DATA_DIR = Path(__file__).parent / "data"

# Team name normalization — handles franchise renames
TEAM_ALIASES = {
    "Delhi Daredevils": "Delhi Capitals",
    "Kings XI Punjab": "Punjab Kings",
    "Rising Pune Supergiant": "Rising Pune Supergiants",
    "Royal Challengers Bangalore": "Royal Challengers Bengaluru",
}

# Venue normalization — same ground, different names over the years
VENUE_ALIASES = {
    "M Chinnaswamy Stadium": "M Chinnaswamy Stadium, Bengaluru",
    "M.Chinnaswamy Stadium": "M Chinnaswamy Stadium, Bengaluru",
    "Arun Jaitley Stadium": "Arun Jaitley Stadium, Delhi",
    "Feroz Shah Kotla": "Arun Jaitley Stadium, Delhi",
    "Rajiv Gandhi International Stadium, Uppal": "Rajiv Gandhi International Stadium, Hyderabad",
    "Rajiv Gandhi International Stadium": "Rajiv Gandhi International Stadium, Hyderabad",
    "Punjab Cricket Association IS Bindra Stadium, Mohali": "PCA Stadium, Mohali",
    "Punjab Cricket Association Stadium, Mohali": "PCA Stadium, Mohali",
    "IS Bindra Stadium": "PCA Stadium, Mohali",
}


def normalize_team(name: str) -> str:
    return TEAM_ALIASES.get(name, name)


def normalize_venue(name: str) -> str:
    return VENUE_ALIASES.get(name, name)


@dataclass
class Match:
    file_id: str
    date: str
    season: str
    teams: list
    venue: str
    city: str
    toss_winner: str
    toss_decision: str
    winner: str
    win_by: dict
    batting_first: str
    innings: list = field(repr=False)

    @classmethod
    def from_file(cls, filepath: str):
        with open(filepath) as f:
            data = json.load(f)

        info = data["info"]
        teams = [normalize_team(t) for t in info["teams"]]
        toss = info.get("toss", {})
        outcome = info.get("outcome", {})

        toss_winner = normalize_team(toss.get("winner", ""))
        toss_decision = toss.get("decision", "")

        if toss_decision == "bat":
            batting_first = toss_winner
        elif toss_decision == "field":
            batting_first = [t for t in teams if t != toss_winner][0] if toss_winner else ""
        else:
            batting_first = teams[0] if data.get("innings") else ""

        winner = normalize_team(outcome.get("winner", ""))
        win_by = outcome.get("by", {})

        return cls(
            file_id=Path(filepath).stem,
            date=info["dates"][0],
            season=str(info.get("season", "")),
            teams=teams,
            venue=normalize_venue(info.get("venue", "")),
            city=info.get("city", ""),
            toss_winner=toss_winner,
            toss_decision=toss_decision,
            winner=winner,
            win_by=win_by,
            batting_first=batting_first,
            innings=data.get("innings", []),
        )


class CricsheetDB:
    def __init__(self, data_dir: str = None):
        self.data_dir = Path(data_dir) if data_dir else DATA_DIR
        self.matches: list[Match] = []
        self._load()

    def _load(self):
        json_files = sorted(self.data_dir.glob("*.json"))
        for fp in json_files:
            try:
                self.matches.append(Match.from_file(str(fp)))
            except (KeyError, json.JSONDecodeError):
                continue
        self.matches.sort(key=lambda m: m.date)

    def _filter(self, cutoff_date: str, team1: str = None, team2: str = None, venue: str = None):
        """Filter matches before cutoff, optionally by teams/venue."""
        results = []
        t1 = normalize_team(team1) if team1 else None
        t2 = normalize_team(team2) if team2 else None
        v = normalize_venue(venue) if venue else None

        for m in self.matches:
            if m.date >= cutoff_date:
                break
            if t1 and t1 not in m.teams:
                continue
            if t2 and t2 not in m.teams:
                continue
            if v and m.venue != v:
                continue
            results.append(m)
        return results

    def head_to_head(self, team1: str, team2: str, cutoff_date: str, venue: str = None):
        """Head-to-head record between two teams."""
        matches = self._filter(cutoff_date, team1, team2, venue)
        t1 = normalize_team(team1)
        t2 = normalize_team(team2)

        t1_wins = sum(1 for m in matches if m.winner == t1)
        t2_wins = sum(1 for m in matches if m.winner == t2)
        no_results = len(matches) - t1_wins - t2_wins

        return {
            "team1": t1,
            "team2": t2,
            "team1_wins": t1_wins,
            "team2_wins": t2_wins,
            "no_results": no_results,
            "total_matches": len(matches),
            "venue_filter": venue,
        }

    def venue_splits(self, venue: str, cutoff_date: str, seasons_back: int = 3):
        """Batting-first vs chasing win rates at a venue."""
        v = normalize_venue(venue)
        all_at_venue = self._filter(cutoff_date, venue=venue)

        if seasons_back:
            recent_seasons = sorted(set(m.season for m in all_at_venue))[-seasons_back:]
            matches = [m for m in all_at_venue if m.season in recent_seasons]
        else:
            matches = all_at_venue

        bat_first_wins = 0
        chase_wins = 0
        first_innings_scores = []
        winning_chases = []

        for m in matches:
            if not m.winner:
                continue
            if m.winner == m.batting_first:
                bat_first_wins += 1
            else:
                chase_wins += 1

            # Calculate first innings total
            if m.innings:
                first_inn = m.innings[0]
                total = sum(
                    d["runs"]["total"]
                    for over in first_inn.get("overs", [])
                    for d in over.get("deliveries", [])
                )
                first_innings_scores.append(total)

                if m.winner != m.batting_first and len(m.innings) > 1:
                    second_inn = m.innings[1]
                    chase_total = sum(
                        d["runs"]["total"]
                        for over in second_inn.get("overs", [])
                        for d in over.get("deliveries", [])
                    )
                    winning_chases.append(chase_total)

        total = bat_first_wins + chase_wins
        return {
            "venue": v,
            "matches_analyzed": total,
            "bat_first_wins": bat_first_wins,
            "chase_wins": chase_wins,
            "bat_first_win_pct": round(bat_first_wins / total, 3) if total else None,
            "avg_first_innings_score": round(sum(first_innings_scores) / len(first_innings_scores)) if first_innings_scores else None,
            "avg_winning_chase": round(sum(winning_chases) / len(winning_chases)) if winning_chases else None,
            "seasons_included": sorted(set(m.season for m in matches)),
        }

    def recent_form(self, team: str, cutoff_date: str, last_n: int = 8):
        """Team's recent results."""
        matches = self._filter(cutoff_date, team1=team)
        t = normalize_team(team)
        recent = matches[-last_n:]

        results = []
        for m in recent:
            opponent = [x for x in m.teams if x != t][0]
            if m.winner == t:
                margin = m.win_by
                if "runs" in margin:
                    result = f"won by {margin['runs']} runs"
                elif "wickets" in margin:
                    result = f"won by {margin['wickets']} wickets"
                else:
                    result = "won"
            elif m.winner:
                margin = m.win_by
                if "runs" in margin:
                    result = f"lost by {margin['runs']} runs"
                elif "wickets" in margin:
                    result = f"lost by {margin['wickets']} wickets"
                else:
                    result = "lost"
            else:
                result = "no result"

            results.append({
                "vs": opponent,
                "date": m.date,
                "venue": m.venue,
                "result": result,
            })

        wins = sum(1 for r in results if r["result"].startswith("won"))
        return {
            "team": t,
            "last_n": len(results),
            "wins": wins,
            "losses": len(results) - wins,
            "matches": results,
        }

    def toss_impact(self, venue: str, cutoff_date: str):
        """Toss impact at a venue."""
        matches = self._filter(cutoff_date, venue=venue)
        matches = [m for m in matches if m.winner and m.toss_winner]

        toss_winner_won = sum(1 for m in matches if m.winner == m.toss_winner)
        bat_first_choices = sum(1 for m in matches if m.toss_decision == "bat")
        field_first_choices = sum(1 for m in matches if m.toss_decision == "field")

        total = len(matches)
        return {
            "venue": normalize_venue(venue),
            "sample_size": total,
            "toss_winner_match_winner_pct": round(toss_winner_won / total, 3) if total else None,
            "chose_bat_first": bat_first_choices,
            "chose_field_first": field_first_choices,
            "preferred_choice": "bat first" if bat_first_choices > field_first_choices else "field first",
        }

    def key_players(self, team: str, cutoff_date: str, season: str = None):
        """Top batters and bowlers for a team in a season."""
        t = normalize_team(team)
        matches = self._filter(cutoff_date, team1=team)

        if season:
            matches = [m for m in matches if m.season == season]
        else:
            current_seasons = sorted(set(m.season for m in matches))
            if current_seasons:
                matches = [m for m in matches if m.season == current_seasons[-1]]

        batter_runs = defaultdict(lambda: {"runs": 0, "balls": 0, "innings": 0})
        bowler_wickets = defaultdict(lambda: {"wickets": 0, "runs": 0, "balls": 0, "innings": 0})

        for m in matches:
            for inn in m.innings:
                is_batting = normalize_team(inn.get("team", "")) == t
                for over in inn.get("overs", []):
                    for delivery in over.get("deliveries", []):
                        if is_batting:
                            batter = delivery["batter"]
                            batter_runs[batter]["runs"] += delivery["runs"]["batter"]
                            batter_runs[batter]["balls"] += 1
                        else:
                            bowler = delivery["bowler"]
                            bowler_wickets[bowler]["runs"] += delivery["runs"]["total"]
                            bowler_wickets[bowler]["balls"] += 1
                            if "wickets" in delivery:
                                for w in delivery["wickets"]:
                                    if w.get("kind") not in ("run out", "retired hurt", "retired out", "obstructing the field"):
                                        bowler_wickets[bowler]["wickets"] += 1

        # Top 3 batters by runs
        top_batters = sorted(batter_runs.items(), key=lambda x: x[1]["runs"], reverse=True)[:5]
        batters = []
        for name, stats in top_batters:
            sr = round(stats["runs"] / stats["balls"] * 100, 1) if stats["balls"] else 0
            batters.append({"name": name, "runs": stats["runs"], "balls": stats["balls"], "strike_rate": sr})

        # Top 3 bowlers by wickets
        top_bowlers = sorted(bowler_wickets.items(), key=lambda x: x[1]["wickets"], reverse=True)[:5]
        bowlers = []
        for name, stats in top_bowlers:
            overs = stats["balls"] / 6
            econ = round(stats["runs"] / overs, 2) if overs else 0
            bowlers.append({"name": name, "wickets": stats["wickets"], "economy": econ, "balls": stats["balls"]})

        season_used = matches[0].season if matches else None
        return {
            "team": t,
            "season": season_used,
            "matches_in_season": len(matches),
            "top_batters": batters,
            "top_bowlers": bowlers,
        }

    def season_standings(self, cutoff_date: str, season: str = None):
        """Points table as of cutoff date."""
        matches = [m for m in self.matches if m.date < cutoff_date and m.winner]

        if season:
            matches = [m for m in matches if m.season == season]
        else:
            seasons = sorted(set(m.season for m in matches))
            if seasons:
                matches = [m for m in matches if m.season == seasons[-1]]

        standings = defaultdict(lambda: {"played": 0, "won": 0, "lost": 0, "points": 0})

        for m in matches:
            for t in m.teams:
                standings[t]["played"] += 1
                if m.winner == t:
                    standings[t]["won"] += 1
                    standings[t]["points"] += 2
                else:
                    standings[t]["lost"] += 1

        table = sorted(standings.items(), key=lambda x: (-x[1]["points"], -x[1]["won"]))
        result = []
        for pos, (team, stats) in enumerate(table, 1):
            result.append({"position": pos, "team": team, **stats})

        season_used = matches[0].season if matches else None
        return {"season": season_used, "as_of": cutoff_date, "table": result}

    def full_stats(self, team1: str, team2: str, venue: str, cutoff_date: str):
        """Complete stats package for a match — everything the Stats Analyst needs."""
        t1 = normalize_team(team1)
        t2 = normalize_team(team2)

        # Determine current season from most recent match before cutoff
        recent = self._filter(cutoff_date)
        current_season = recent[-1].season if recent else None

        return {
            "match": f"{t1} vs {t2}",
            "venue": normalize_venue(venue),
            "cutoff_date": cutoff_date,
            "head_to_head": {
                "overall": self.head_to_head(team1, team2, cutoff_date),
                "at_venue": self.head_to_head(team1, team2, cutoff_date, venue),
            },
            "venue_splits": self.venue_splits(venue, cutoff_date),
            "recent_form": {
                "team1": self.recent_form(team1, cutoff_date),
                "team2": self.recent_form(team2, cutoff_date),
            },
            "key_players": {
                "team1": self.key_players(team1, cutoff_date, current_season),
                "team2": self.key_players(team2, cutoff_date, current_season),
            },
            "toss_impact": self.toss_impact(venue, cutoff_date),
            "season_standings": self.season_standings(cutoff_date, current_season),
        }


if __name__ == "__main__":
    import sys

    db = CricsheetDB()
    print(f"Loaded {len(db.matches)} matches")
    print(f"Date range: {db.matches[0].date} to {db.matches[-1].date}")
    print(f"Seasons: {sorted(set(m.season for m in db.matches))}")

    if len(sys.argv) > 1 and sys.argv[1] == "test":
        print("\n--- Test: RR vs GT at Sawai Mansingh, cutoff 2026-05-09 ---\n")
        stats = db.full_stats(
            "Rajasthan Royals", "Gujarat Titans",
            "Sawai Mansingh Stadium", "2026-05-09"
        )
        print(json.dumps(stats, indent=2, default=str))
