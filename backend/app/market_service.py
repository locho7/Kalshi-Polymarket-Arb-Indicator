from app.api_clients.kalshi import fetch_event
from app.api_clients.polymarket import fetch_slug
from app.data.market_pairs import get_kalshi_events, get_polymarket_slugs
from app.cache.market_cache import MarketCache

ttl_seconds = 30
kalshi_cache = MarketCache(ttl_seconds)
polymarket_cache = MarketCache(ttl_seconds)


def refresh_kalshi_cache() -> None:
    kalshi_cache.clear()
    for event in get_kalshi_events():
        markets_dict = {}
        markets_list = fetch_event(event)
        for market in markets_list:
            markets_dict[market['ticker']] = market
        kalshi_cache.set(event, markets_dict)

def refresh_polymarket_cache() -> None:
    polymarket_cache.clear()
    for slug in get_polymarket_slugs():
        markets_dict = {}
        markets_list = fetch_slug(slug)
        for market in markets_list:
            markets_dict[market['id']] = market
        polymarket_cache.set(slug, markets_dict)

def get_kalshi_market(event_ticker: str, market_ticker: str) -> dict | None:
    event_ticker = event_ticker.upper()
    market_ticker = market_ticker.upper()

    if event_ticker not in get_kalshi_events():
        return None
    
    markets = kalshi_cache.get(event_ticker)

    if markets is None:
        refresh_kalshi_cache()
        markets = kalshi_cache.get(event_ticker)

    if markets is None:
        return None

    return markets.get(market_ticker)

def get_polymarket_market(slug: str, id: str) -> dict | None:
    slug = slug.lower()

    if slug not in get_polymarket_slugs():
        return None

    markets = polymarket_cache.get(slug)

    if markets is None:
        refresh_polymarket_cache()
        markets = polymarket_cache.get(slug)

    if markets is None:
        return None
    
    return markets.get(id)

    

