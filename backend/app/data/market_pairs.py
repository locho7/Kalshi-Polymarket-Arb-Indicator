market_pairs = [
    # {
    #     "kalshi_event_ticker": str,
    #     "kalshi_market_ticker": str,
    #     "polymarket_slug": str,
    #     "polymarket_id": int
    # },
    {
        "kalshi_event_ticker": "KXNBA-27",
        "kalshi_market_ticker": "KXNBA-27-NYK",
        "polymarket_slug": "nba-2027-champion",
        "polymarket_id": "2243306"
    },
    {
        "kalshi_event_ticker": "KXNBA-27",
        "kalshi_market_ticker": "KXNBA-27-SAS",
        "polymarket_slug": "nba-2027-champion",
        "polymarket_id": "2243324"
    },
    {
        "kalshi_event_ticker": "KXNBA-27",
        "kalshi_market_ticker": "KXNBA-27-PHI",
        "polymarket_slug": "nba-2027-champion",
        "polymarket_id": "2243308"
    },
    {
       "kalshi_event_ticker": "KXNBA-27",
        "kalshi_market_ticker": "KXNBA-27-OKC",
        "polymarket_slug": "nba-2027-champion",
        "polymarket_id": "2243320"
    },
]


def get_kalshi_events() -> set[str]:
    events = set()
    for pair in market_pairs:
        events.add(pair["kalshi_event_ticker"].upper())
    return events

def get_polymarket_slugs() -> set[str]:
    slugs = set()
    for pair in market_pairs:
        slugs.add(pair["polymarket_slug"].lower())
    return slugs