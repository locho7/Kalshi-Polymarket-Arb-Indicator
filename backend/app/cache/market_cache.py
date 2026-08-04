import time
from typing import Any

# kalshi_cache = {
#     event_ticker: str = {
#         "fetched_at": str
#         "markets" : {
#             market_obj
#         }
#     }
# }

data_type = dict[str, dict[str, Any]]
entry_type = dict[str, Any]


class MarketCache:
    def __init__(self, ttl: float):
        self.ttl = ttl
        self._data: data_type = {}

    def get(self, key: str) -> entry_type | None:
        entry = self._data.get(key)

        if (entry is not None and 
            time.monotonic() - entry["fetched_at"] < self.ttl):
            return entry["markets"]

    def set(self, key: str, markets: entry_type) -> None:
        self._data[key] = {
            "fetched_at": time.monotonic(),
            "markets": markets
        }

    def delete(self, key: str) -> None:
        self._data.pop(key, None)

    def clear(self) -> None:
        self._data.clear()
        
        


