# src/ingestion/normalizer.py

def detect_asset(text: str):
    t = text.lower()

    if "bitcoin" in t or "btc" in t:
        return "BTCUSDT"
    if "ethereum" in t or "eth" in t:
        return "ETHUSDT"

    return None


def normalize(items):
    normalized = []

    for i in items:
        # Try all possible text fields
        raw_text = (
            i.get("text")
            or i.get("content")
            or i.get("description")
            or i.get("message")
            or ""
        ).strip()

        if not raw_text:
            continue  # skip empty items

        asset = detect_asset(raw_text)
        if asset is None:
            continue  # ❌ drop non-BTC/ETH news

        normalized.append({
            "title": i.get("title") or raw_text[:120],
            "text": raw_text,
            "url": i.get("url", ""),
            "source": i.get("source", "unknown"),
            "timestamp": i.get("timestamp"),
            "asset": asset,  # ✅ REQUIRED
        })

    return normalized