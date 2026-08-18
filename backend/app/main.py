from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from app import models
from sqlalchemy import select
from app.database import engine, get_db
from sqlalchemy.orm import Session
from typing import List, Annotated

from app.opportunity_service import *

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
db_dependency = Annotated[Session, Depends(get_db)]


origins = [
    "http://localhost:3000",
    "http://localhost:5173", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
)

@app.get("/get-marketpairs")
def read_market_pairs(db: db_dependency):
    pairs = db.query(models.Pair).all()
    return pairs


@app.get("/get-opportunities")
def get_opportunities(db: db_dependency):
    market_pairs = db.query(models.Pair).all()
    opportunities = build_opportunities(
        market_pairs,
        get_kalshi_events,
        get_polymarket_slugs
    )
    return opportunities


@app.post("/marketpair")
async def create_market_pair (
    pair: models.MarketPairBase,
    db: db_dependency
):
   db_pair = models.Pair (
       kalshi_event_ticker = pair.kalshi_event_ticker.upper(),
       kalshi_market_ticker = pair.kalshi_market_ticker.upper(),
       polymarket_slug = pair.polymarket_slug.lower(),
       polymarket_id = pair.polymarket_id,
   )

   db.add(db_pair)
   db.commit()
   db.refresh(db_pair)

   return db_pair
