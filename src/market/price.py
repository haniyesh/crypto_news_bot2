# src/market/price.py

import requests

BINANCE_URL = "https://api.binance.com/api/v3/ticker/price"


def get_price(symbol: str) -> float:
    if symbol not in ("BTCUSDT", "ETHUSDT"):
        return 0.0

    r = requests.get(BINANCE_URL, params={"symbol": symbol}, timeout=5)
    return float(r.json()["price"])