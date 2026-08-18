import json
import requests

def fetch_slug(slug: str) -> list:
    markets = []
    url = f"https://gamma-api.polymarket.com/events/slug/{slug}"
    try:
        response = requests.get(url, params = {"active": True}, timeout=10)
        event_data = response.json()
        for market in event_data['markets']:
           markets.append(market)
        return markets
    except:
        print(f"Error fetching Polymarket Slug")
        return []

def print_markets_polymarket(slug: str) -> None:
    markets = fetch_slug(slug)
    for market in markets:
        if "outcomePrices" not in market: continue
        outcomePrices = json.loads(market["outcomePrices"])
        print(f" - Market ID : {market['id']}")
        print(f"   Title: {market['question']}")
        print(f"   Outcomes: {market['outcomes']}")
        print(f"   YES ask: {outcomePrices[0]}")
        print(f"   No ask: {outcomePrices[1]}")
        print()
