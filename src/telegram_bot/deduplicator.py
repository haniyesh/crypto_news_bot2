# deduplicator.py

from firebase_admin import db
from datetime import datetime


# =============================
# CHECK IF SENT
# =============================

def is_already_sent(news_id):
    ref = db.reference(f"sent_news/{news_id}")
    return ref.get() is not None


# =============================
# MARK AS SENT
# =============================

def mark_as_sent(news_id):
    ref = db.reference(f"sent_news/{news_id}")
    ref.set({
        "sent_at": datetime.utcnow().isoformat()
    })


# =============================
# GENERATE NEWS ID
# =============================

def generate_news_id(news_item):
    # ترکیب title + publishedAt برای یونیک بودن
    raw = news_item["title"] + news_item["publishedAt"]
    return str(abs(hash(raw)))