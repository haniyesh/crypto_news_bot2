import asyncio
from ingestion.rss_fetcher import fetch_rss
from ingestion.api_fetcher import fetch_api
from ingestion.telegram_fetcher import fetch_telegram_news
from ingestion.normalizer import normalize

RSS_FEEDS = [
    "https://cointelegraph.com/rss"
]

TELEGRAM_CHANNELS = [
"cointelegraph",
    "coindesk",
    "bitcoinmagazine",
    "cryptoslate",
    "BitcoinMagazineTelegram"]

def fetch_all_news():
    rss = fetch_rss(RSS_FEEDS)
    api = fetch_api()
    tg = asyncio.run(fetch_telegram_news(TELEGRAM_CHANNELS))
    return normalize(rss+api+tg)