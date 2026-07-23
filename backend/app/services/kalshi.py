import requests

base_url = "https://external-api.kalshi.com/trade-api/v2"


def fetch_all_active_markets_k(order="volume", ascending=False, active=True, limit=100):
    url = f"{base_url}/markets"
    params = {
        "limit": limit,
    }

    if active:
        params["status"] = "open"

    response = requests.get(url, params=params)

    if response.status_code == 200:
        markets_data = response.json()
        markets = markets_data["markets"]

        if order == "volume":
            markets.sort(
                key=lambda market: float(market.get("volume_fp", 0)),
                reverse=not ascending
            )

        for market in markets:
            print(f"Title: {market['title']}")
            print(f"Volume: {market['volume_fp']}")
            print(f"Ticker: {market['ticker']}")
            print()

        return markets
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None


def get_markets():
    url = "https://external-api.kalshi.com/trade-api/v2/markets"
    params = {
        "limit": 10,
        "status": "open"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        markets_data = response.json()
        print(markets_data)
    else:
        print(f"Error: {response.status_code}")

def fetch_markets(series):
    url = f"{base_url}/markets?series_ticker={series}&status=open"
    response = requests.get(url)
    if response.status_code == 200:
        markets_data = response.json()
        for market in markets_data['markets']:
            print(f"- {market['title']}")
            print(f"  Ticker: {market['event_ticker']}")
            print(f"  Yes Price: ${market['yes_bid_dollars']} | No Price: {market['no_bid_dollars']}")
            print(f"  Last Price Dollars: ${market['last_price_dollars']}")
            print()
            return market
    return None

fetch_all_active_markets_k()
