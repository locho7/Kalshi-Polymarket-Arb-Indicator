from app.services.kalshi import get_market_kalshi
from app.services.polymarket import get_market_polymarket
from app.data.market_pairs import market_pairs

def build_opportunities():
    opportunities = []
    for pair in market_pairs:
        kalshi_market = get_market_kalshi(pair["kalshiEventTicker"], 
                                          pair["kalshiMarketTicker"])
        polymarket_market = get_market_polymarket(pair["polymarketSlug"],
                                                  pair["polymarketID"])
        print(f"- Kalshi: {kalshi_market}")
        print("-" * 40)
        print(f"- Polymarket: {polymarket_market}")

build_opportunities()