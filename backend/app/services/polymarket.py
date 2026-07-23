import requests

def fetch_all_active_markets_p():
    url = "https://gamma-api.polymarket.com/markets"
    params = {
        "order": "volume",
        "ascending": False,
        "active": True,
        "limit": 100,
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        markets_data = response.json()
        for market in markets_data:
            print(f"Question: {market['question']}")
            print(f"Volume: {market['volume']}")
            print(f"ID: {market['id']}")
    else:
        print(f"Error: {response.status_code}")

fetch_all_active_markets_p()