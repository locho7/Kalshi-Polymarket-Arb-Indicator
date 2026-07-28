import json
import requests

def fetch_event_polymarket(slug):
    url = f"https://gamma-api.polymarket.com/events/slug/{slug}"
    response = requests.get(url, params = {"active": True})
    if response.status_code == 200:
        event_data = response.json()
        # for market in event_data["markets"]:
        #     if "outcomePrices" not in market: continue
        #     outcomePrices = json.loads(market["outcomePrices"])
        #     print(f" - Market Ticker/ID : {market['id']}")
        #     print(f"   Title: {market['question']}")
        #     print(f"   Outcomes: {market['outcomes']}")
        #     print(f"   YES ask: {outcomePrices[0]}")
        #     print(f"   No ask: {outcomePrices[1]}")
        #     print()
        return event_data
    print(f"Error: {response.status_code}")

def print_markets_polymarket(slug):
    event_data = fetch_event_polymarket(slug)
    if event_data:
        for market in event_data["markets"]:
            if "outcomePrices" not in market: continue
            outcomePrices = json.loads(market["outcomePrices"])
            print(f" - Market Ticker/ID : {market['id']}")
            print(f"   Title: {market['question']}")
            print(f"   Outcomes: {market['outcomes']}")
            print(f"   YES ask: {outcomePrices[0]}")
            print(f"   No ask: {outcomePrices[1]}")
            print()

def get_market_polymarket(slug, id):
    event_data = fetch_event_polymarket(slug)
    if event_data:
        for market in event_data["markets"]:
            if market["id"] == id:
                return market