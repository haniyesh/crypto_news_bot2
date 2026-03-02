# callback_handler.py

import requests
from database import save_rating
from config.secrets import TELEGRAM_BOT_TOKEN

BOT_TOKEN = "YOUR_BOT_TOKEN"

def handle_updates():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

    response = requests.get(url).json()

    for update in response.get("result", []):
        if "callback_query" in update:
            data = update["callback_query"]["data"]
            chat_id = update["callback_query"]["message"]["chat"]["id"]

            if data.startswith("rate_"):
                _, news_id, rating = data.split("_")

                save_rating(int(news_id), int(rating))

                answer_url = f"https://api.telegram.org/bot{BOT_TOKEN}/answerCallbackQuery"
                requests.post(answer_url, json={
                    "callback_query_id": update["callback_query"]["id"],
                    "text": f"Rating saved: {rating} ⭐"
                })