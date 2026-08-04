import requests

def fetch_event(event: str) -> list:
    markets = []
    url = f"https://external-api.kalshi.com/trade-api/v2/events/{event.upper()}"
    response = requests.get(url, params = {"with_nested_markets": True})
    if response.status_code == 200:
        event_data = response.json()
        for market in event_data['event']['markets']:
           markets.append(market)
    else:
        print(f"Error fetching Kalshi Event: {response.status_code}")
    return markets

def print_markets_kalshi(event) -> None:
    markets = fetch_event(event) 
    for market in markets:
        print(f" - Market Ticker: {market['ticker']}")
        print(f"   Title: {market['yes_sub_title']}")
        print(f"   YES ask: {market['yes_ask_dollars']}")
        print(f"   NO ask: {market['no_ask_dollars']}")
        print()