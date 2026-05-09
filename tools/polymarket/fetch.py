"""
Polymarket IPL market data adapter.

Fetches current implied probabilities from Polymarket's public Gamma API
and CLOB API for IPL match-winner markets. Falls back to manual_snapshot.json
if the API is unreachable or the match isn't found.
"""

import json
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

GAMMA_API = "https://gamma-api.polymarket.com"
CLOB_API = "https://clob.polymarket.com"
IPL_TAG_ID = "101988"


def fetch_ipl_events(active_only: bool = True) -> list[dict]:
    """Fetch all IPL events from Gamma API."""
    url = f"{GAMMA_API}/events?tag_id={IPL_TAG_ID}"
    if active_only:
        url += "&active=true&closed=false"

    req = urllib.request.Request(url, headers={"User-Agent": "CricketPricingRoom/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except (urllib.error.URLError, TimeoutError) as e:
        print(f"API error: {e}")
        return []


def find_match_market(events: list[dict], team1: str, team2: str) -> dict | None:
    """Find the match-winner market for a specific matchup."""
    t1_lower = team1.lower()
    t2_lower = team2.lower()

    for event in events:
        title = event.get("title", "").lower()
        # Match events like "Indian Premier League: Rajasthan Royals vs Gujarat Titans"
        if t1_lower in title and t2_lower in title:
            # Skip toss, sixes, batter prop markets
            if any(x in title for x in ["toss", "sixes", "batter", "double"]):
                continue
            # Find the match-winner market (not toss/completion sub-markets)
            for market in event.get("markets", []):
                q = market.get("question", "").lower()
                if t1_lower in q and t2_lower in q and "toss" not in q and "completed" not in q:
                    return market
    return None


def parse_market(market: dict, team1: str, team2: str) -> dict:
    """Parse a Gamma API market object into our snapshot format."""
    outcomes = market.get("outcomes", "")
    if isinstance(outcomes, str):
        outcomes = json.loads(outcomes) if outcomes else []

    prices = market.get("outcomePrices", "")
    if isinstance(prices, str):
        prices = json.loads(prices) if prices else []

    # Map outcomes to teams
    team1_prob = None
    team2_prob = None
    t1_lower = team1.lower()
    t2_lower = team2.lower()

    for i, outcome in enumerate(outcomes):
        if i < len(prices):
            price = float(prices[i])
            outcome_lower = outcome.lower()
            if t1_lower in outcome_lower or any(w in outcome_lower for w in t1_lower.split()):
                team1_prob = price
            elif t2_lower in outcome_lower or any(w in outcome_lower for w in t2_lower.split()):
                team2_prob = price

    # Fallback: first price = first team in outcomes order
    if team1_prob is None and team2_prob is None and len(prices) >= 2:
        team1_prob = float(prices[0])
        team2_prob = float(prices[1])

    volume = float(market.get("volume", 0) or 0)

    # Liquidity flag
    if volume < 10_000:
        liquidity = "thin"
    elif volume < 50_000:
        liquidity = "moderate"
    else:
        liquidity = "deep"

    return {
        "source": "polymarket",
        "market_id": market.get("id", ""),
        "condition_id": market.get("conditionId", ""),
        "team1": {"name": team1, "implied_probability": team1_prob},
        "team2": {"name": team2, "implied_probability": team2_prob},
        "volume_usd": round(volume, 2),
        "liquidity_flag": liquidity,
    }


def fetch_last_trade_prices(token_ids: list[str]) -> tuple[float | None, float | None]:
    """Fetch last trade price for each token from CLOB API."""
    prices = []
    for tid in token_ids[:2]:
        url = f"{CLOB_API}/book?token_id={tid}"
        req = urllib.request.Request(url, headers={"User-Agent": "CricketPricingRoom/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                book = json.loads(resp.read())
                prices.append(float(book.get("last_trade_price", 0)))
        except (urllib.error.URLError, TimeoutError, ValueError):
            prices.append(None)
    return tuple(prices) if len(prices) == 2 else (None, None)


def load_manual_snapshot(case_study_dir: str) -> dict | None:
    """Load manual_snapshot.json fallback."""
    path = Path(case_study_dir) / "manual_snapshot.json"
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return None


def get_market_snapshot(team1: str, team2: str, venue: str = "", date: str = "", case_study_dir: str = None) -> dict:
    """
    Main entry point. Fetch market snapshot for a match.
    Falls back to manual_snapshot.json if API fails or match not found.
    """
    snapshot = {
        "match": f"{team1} vs {team2}",
        "venue": venue,
        "date": date,
        "snapshot_timestamp": datetime.now(timezone.utc).isoformat(),
    }

    # Try live API first
    events = fetch_ipl_events()
    market = find_match_market(events, team1, team2) if events else None

    if market:
        parsed = parse_market(market, team1, team2)
        snapshot.update(parsed)

        # Get last trade prices from CLOB for a more granular view
        token_ids = market.get("clobTokenIds", "")
        if isinstance(token_ids, str):
            token_ids = json.loads(token_ids) if token_ids else []
        if token_ids:
            ltp1, ltp2 = fetch_last_trade_prices(token_ids)
            snapshot["last_trade_prices"] = [ltp1, ltp2]
            # Overround from Gamma prices (sum - 1.0). Polymarket normalizes to 1.0,
            # so this is typically 0. Kept for consistency with the agent spec.
            t1p = snapshot["team1"]["implied_probability"] or 0
            t2p = snapshot["team2"]["implied_probability"] or 0
            snapshot["bid_ask_spread_pct"] = round((t1p + t2p - 1.0) * 100, 2)
        else:
            snapshot["last_trade_prices"] = None
            snapshot["bid_ask_spread_pct"] = None

        snapshot["notes"] = "Live API fetch successful"
        return snapshot

    # Fallback to manual snapshot
    if case_study_dir:
        manual = load_manual_snapshot(case_study_dir)
        if manual:
            snapshot.update(manual)
            snapshot["source"] = "manual_snapshot"
            snapshot["notes"] = "Loaded from manual_snapshot.json (API unavailable or match not found)"
            return snapshot

    # No data available
    snapshot["source"] = "none"
    snapshot["team1"] = {"name": team1, "implied_probability": None}
    snapshot["team2"] = {"name": team2, "implied_probability": None}
    snapshot["volume_usd"] = None
    snapshot["bid_ask_spread_pct"] = None
    snapshot["liquidity_flag"] = None
    snapshot["notes"] = "No market data available — match not found on Polymarket and no manual snapshot provided"
    return snapshot


if __name__ == "__main__":
    import sys

    print("Fetching IPL market data from Polymarket...\n")

    # List all available IPL match markets
    events = fetch_ipl_events()
    print(f"Found {len(events)} IPL events\n")

    for event in events:
        title = event.get("title", "")
        if "vs" in title and "Toss" not in title and "Sixes" not in title and "Batter" not in title and "Double" not in title:
            print(f"  {title}")
            for m in event.get("markets", []):
                q = m.get("question", "")
                prices = m.get("outcomePrices", "[]")
                vol = m.get("volume", 0)
                if "toss" not in q.lower() and "completed" not in q.lower():
                    print(f"    Prices: {prices}, Volume: ${float(vol or 0):,.0f}")

    if len(sys.argv) > 1 and sys.argv[1] == "test":
        print("\n--- Test: RR vs GT snapshot ---\n")
        snapshot = get_market_snapshot("Rajasthan Royals", "Gujarat Titans", "Sawai Mansingh Stadium", "2026-05-10")
        print(json.dumps(snapshot, indent=2))
