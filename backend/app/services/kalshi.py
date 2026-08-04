import requests

def fetch_event_kalshi(event_ticker):
    event_ticker = event_ticker.upper()
    url = f"https://external-api.kalshi.com/trade-api/v2/events/{event_ticker}"
    response = requests.get(url, params = {"with_nested_markets": True})
    if response.status_code == 200:
        event_data = response.json()
        return event_data
    print(f"Error: {response.status_code}")

def print_markets_kalshi(event_ticker):
    event_data = fetch_event_kalshi(event_ticker)
    if event_data: 
        for market in event_data["event"]["markets"]:
            print(f" Ticker: {market['ticker']}")
            print(f" Title: {market['yes_sub_title']}")
            print(f" YES ask: {market['yes_ask_dollars']}")
            print(f" NO ask: {market['no_ask_dollars']}")
            print()

def get_market_kalshi(event_ticker, market_ticker):
    event_data = fetch_event_kalshi(event_ticker)
    if event_data:
        for market in event_data["event"]["markets"]:
            if market["ticker"] == market_ticker:
                return market
