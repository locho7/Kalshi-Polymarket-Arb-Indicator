from app.services.kalshi import get_market_kalshi
from app.services.polymarket import get_market_polymarket
from app.data.market_pairs import market_pairs
from app.utils.find_price_difference import find_price_difference
from app.utils.find_trade import find_trade
from app.models import Opportunity
import json


def build_opportunities():
    opportunities = []
    for pair in market_pairs:
        kalshi_market = get_market_kalshi(pair["kalshi_event_ticker"], 
                                          pair["kalshi_market_ticker"])
        polymarket_market = get_market_polymarket(pair["polymarket_slug"],
                                                  pair["polymarket_id"])
        if kalshi_market is None or polymarket_market is None:
            continue
        k_yes_ask = float(kalshi_market['yes_ask_dollars'])
        k_no_ask = float(kalshi_market['no_ask_dollars'])
        p_outcome_prices = json.loads(polymarket_market['outcomePrices'])
        p_yes_ask = float(p_outcome_prices[0])
        p_no_ask = float(p_outcome_prices[1])

        opportunities.append(Opportunity(
            id=f"{kalshi_market['ticker']}:{polymarket_market['id']}",
            title=f"{polymarket_market['question']}",
            kalshi_market_ticker=kalshi_market['ticker'],
            polymarket_slug=polymarket_market['slug'],
            polymarket_id=polymarket_market['id'],
            kalshi_yes_ask=k_yes_ask,
            kalshi_no_ask=k_no_ask,
            polymarket_yes_ask=p_yes_ask,
            polymarket_no_ask=p_no_ask,
            price_difference=find_price_difference(k_yes_ask, k_no_ask,
                                                   p_yes_ask, p_no_ask),
            best_trade=find_trade(k_yes_ask, k_no_ask, 
                                  p_yes_ask, p_no_ask)
        ))
    return opportunities

print(build_opportunities())