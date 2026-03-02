# src/feedback/engine.py
from feedback.storage import get_manual_feedback


def adjust_with_feedback(news_id: str, sentiment: dict):
    """
    Adjust sentiment using past manual feedback (1–5)
    """
    ratings = get_manual_feedback(news_id)

    if not ratings:
        return sentiment

    avg_rating = sum(ratings) / len(ratings)  # 1..5
    pos = avg_rating / 5.0
    neg = 1.0 - pos

    sentiment["positive"] = round((sentiment["positive"] + pos) / 2, 3)
    sentiment["negative"] = round((sentiment["negative"] + neg) / 2, 3)

    return sentiment