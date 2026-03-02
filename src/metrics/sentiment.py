# src/metrics/sentiment.py

def compute_sentiment(vectors):
    """
    Simple & stable sentiment placeholder.
    Always returns a COMPLETE dict.
    """

    if not vectors:
        return {
            "label": "neutral",
            "positive": 0.0,
            "negative": 0.0
        }

    # 🔹 SIMPLE heuristic (safe)
    score = sum(v[0] for v in vectors) / len(vectors)

    if score > 0:
        return {
            "label": "positive",
            "positive": round(min(score, 1.0), 2),
            "negative": round(1 - min(score, 1.0), 2),
        }
    else:
        return {
            "label": "negative",
            "positive": round(1 - min(abs(score), 1.0), 2),
            "negative": round(min(abs(score), 1.0), 2),
        }