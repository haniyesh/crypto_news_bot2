import logging
from ingestion.rss_fetcher import fetch_rss
from ingestion.api_fetcher import fetch_api
from ingestion.telegram_fetcher import fetch_telegram
from datetime import datetime

async def get_latest_news(limit=15):
    logging.info("👂 Checking for news...")
    all_news = []

    # RSS
    try:
        rss_news = fetch_rss()
        if isinstance(rss_news, list):
            all_news.extend(rss_news)
    except Exception as e:
        logging.error(f"❌ RSS fetch error: {e}")

    # API
    try:
        api_news = fetch_api()
        if isinstance(api_news, list):
            all_news.extend(api_news)
    except Exception as e:
        logging.error(f"❌ API fetch error: {e}")

    # Telegram (async)
    try:
        telegram_news = await fetch_telegram()
        if isinstance(telegram_news, list):
            all_news.extend(telegram_news)
    except Exception as e:
        logging.error(f"❌ Telegram fetch error: {e}")

    # Remove duplicates
    unique_news = {item["title"]: item for item in all_news}

    # Sort by publishedAt
    def parse_date(item):
        try:
            return datetime.fromisoformat(item["publishedAt"])
        except Exception:
            return datetime.min

    news_sorted = sorted(unique_news.values(), key=parse_date, reverse=True)
    safe_limit = int(limit) if isinstance(limit, int) else 15
    logging.info(f"Found {len(news_sorted)} news items.")
    return news_sorted[:safe_limit]