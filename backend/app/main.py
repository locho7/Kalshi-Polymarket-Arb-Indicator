from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:5173", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
)

opportunities = [
    {
        "id": "btc-up-or-down",
        "title": "Btc Up or Down",
        "category": "Crypto-5M",
        "kalshiYes": 0.52,
        "kalshiNo": 0.48,
        "polymarketYes": 0.54,
        "polymarketNo": 0.46,
        "lastUpdated": "07-03-2026-20:13:52"
    }, 
    {
        "id":"mexico-england",
        "title": "Mexico vs England",
        "category": "Sports-Soccer-World-Cup",
        "kalshiYes": 0.51,
        "kalshiNo": 0.49,
        "polymarketYes": 0.53,
        "polymarketNo": 0.47,
        "lastUpdated": "07-03-2026-20:14:43"
    },
    {
        "id":"highest-temperature-in-la-today",
        "title": "Highest temperature in LA today?",
        "category": "Climate And Weather-Daily Temperature",
        "kalshiYes": 0.68,
        "kalshiNo": 0.32,
        "polymarketYes": 0.63,
        "polymarketNo": 0.37,
        "lastUpdated": "07-03-2026-20:14:34"
    }
]

@app.get("/get-opportunities")
def get_opportunities():
    return opportunities