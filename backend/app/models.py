from pydantic import BaseModel
from typing import Optional

from sqlalchemy import Column, String, Integer
from app.database import Base

class OpportunityBase(BaseModel):
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

class MarketPairBase(BaseModel):
    kalshi_event_ticker: str
    kalshi_market_ticker: str
    polymarket_slug: str
    polymarket_id: str

class Pair(Base):
    __tablename__ = 'pair'

    id = Column(Integer, primary_key=True)
    kalshi_event_ticker = Column(String, index=True)
    kalshi_market_ticker = Column(String, index=True, unique=True)
    polymarket_slug = Column(String, index=True)
    polymarket_id = Column(String, index=True, unique=True)