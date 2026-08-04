from app.math import (find_price_difference, 
                      find_trade)
from app.market_service import (get_polymarket_market, 
                                get_kalshi_market)
from app.data.market_pairs import market_pairs
from app.models import Opportunity
from operator import attrgetter
from datetime import datetime
import json

def get_opportunities() -> list[Opportunity]:
    opportunities = []

    for pair in market_pairs:
        kalshi_market = get_kalshi_market(pair["kalshi_event_ticker"], 
                                                  pair["kalshi_market_ticker"])
        polymarket_market = get_polymarket_market(pair["polymarket_slug"],
                                                          pair["polymarket_id"])
        
        if kalshi_market is None or polymarket_market is None:
            continue

        k_yes = float(kalshi_market['yes_ask_dollars'])
        k_no = float(kalshi_market['no_ask_dollars'])

        outcome_prices = json.loads(polymarket_market['outcomePrices'])
        p_yes = float(outcome_prices[0])
        p_no = float(outcome_prices[1])

        difference = find_price_difference(k_yes, k_no, p_yes, p_no)
        if difference is None: #or difference < 0.01:
            continue

        trade = find_trade(k_yes, k_no, p_yes, p_no)

        opportunities.append(Opportunity(
            id=f"{kalshi_market['ticker']}:{polymarket_market['id']}",
            title=f"{polymarket_market['question']}",
            kalshi_market_ticker=kalshi_market['ticker'],
            polymarket_slug=polymarket_market['slug'],
            polymarket_id=polymarket_market['id'],
            kalshi_yes_ask=k_yes,
            kalshi_no_ask=k_no,
            polymarket_yes_ask=p_yes,
            polymarket_no_ask=p_no,
            price_difference=difference,
            best_trade=trade,
            last_updated=datetime.now().strftime("%H:%M:%S")
        ))

    return opportunities

def build_opportunities() -> list[Opportunity]:
    opportunities = get_opportunities()
    opportunities.sort(key=attrgetter('price_difference'), reverse=True)
    return opportunities
