from pydantic import BaseModel
from typing import Optional

class Opportunity(BaseModel):
    id: str
    title: str

    kalshi_market_ticker: str
    polymarket_slug: str
    polymarket_id: str

    kalshi_yes_ask: Optional[float]
    kalshi_no_ask: Optional[float]
    polymarket_yes_ask: Optional[float]
    polymarket_no_ask: Optional[float]

    price_difference: Optional[float]
    best_trade: str

    last_updated: str