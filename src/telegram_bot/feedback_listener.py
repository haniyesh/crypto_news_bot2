# src/telegram_bot/feedback_listener.py

import requests
import time
from feedback.storage import save_manual_feedback
from config.secrets import TELEGRAM_BOT_TOKEN
# src/telegram_bot/feedback_listener.py



TELEGRAM_API = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"
OFFSET = None


def start_listener():
    print("🤖 Telegram feedback listener started")

    global OFFSET
    while True:
        r = requests.get(
            f"{TELEGRAM_API}/getUpdates",
            params={"timeout": 30, "offset": OFFSET},
        ).json()

        if not r.get("ok"):
            time.sleep(2)
            continue

        for update in r["result"]:
            OFFSET = update["update_id"] + 1

            msg = update.get("message", {})
            text = msg.get("text", "")

            if text.startswith("/rate_"):
                try:
                    rating = int(text.split("_")[1])
                    reply = msg.get("reply_to_message")
                    if not reply:
                        continue

                    news_id = reply["text"][:36]
                    save_manual_feedback(news_id, rating)

                    chat_id = msg["chat"]["id"]
                    requests.post(
                        f"{TELEGRAM_API}/sendMessage",
                        json={
                            "chat_id": chat_id,
                            "text": f"✅ Feedback ثبت شد: {rating}/5",
                        },
                    )

                    print(f"⭐ Feedback {rating} saved")

                except Exception as e:
                    print("❌ Listener error:", e)

        time.sleep(1)