# telegram_sender.py

import requests
from config.secrets import TELEGRAM_BOT_TOKEN,TELEGRAM_CHAT_ID
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send_news_with_rating(news_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    keyboard = {
        "inline_keyboard": [
            [
                {"text": "⭐1", "callback_data": f"rate_{news_id}_1"},
                {"text": "⭐2", "callback_data": f"rate_{news_id}_2"},
                {"text": "⭐3", "callback_data": f"rate_{news_id}_3"},
                {"text": "⭐4", "callback_data": f"rate_{news_id}_4"},
                {"text": "⭐5", "callback_data": f"rate_{news_id}_5"},
            ]
        ]
    }

    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown",
        "reply_markup": keyboard
    }

    requests.post(url, json=payload)