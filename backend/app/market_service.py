from app.api_clients.kalshi import fetch_event
from app.api_clients.polymarket import fetch_slug
from app.market_cache import MarketCache

ttl_seconds = 30
kalshi_cache = MarketCache(ttl_seconds)
polymarket_cache = MarketCache(ttl_seconds)


def refresh_kalshi_cache(events) -> None:
    kalshi_cache.clear()
    for event in events:
        markets_dict = {}
        markets_list = fetch_event(event)
        for market in markets_list:
            markets_dict[market['ticker']] = market
        kalshi_cache.set(event, markets_dict)


def refresh_polymarket_cache(slugs) -> None:
    polymarket_cache.clear()
    for slug in slugs:
        markets_dict = {}
        markets_list = fetch_slug(slug)
        for market in markets_list:
            markets_dict[market['id']] = market
        polymarket_cache.set(slug, markets_dict)


def get_kalshi_market(events, event, market) -> dict | None:
    event = event.upper()
    market = market.upper()
    markets = kalshi_cache.get(event)
    
    if markets is None:
        refresh_kalshi_cache(events)
        markets = kalshi_cache.get(event)

    if markets is None:
        return None

    return markets.get(market)


def get_polymarket_market(slugs, slug, id) -> dict | None:
    slug = slug.lower()
    id = str(id)
    markets = polymarket_cache.get(slug)

    if markets is None:
        refresh_polymarket_cache(slugs)
        markets = polymarket_cache.get(slug)

    if markets is None:
        return None
    
    return markets.get(id)

    

