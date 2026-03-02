# src/telegram_bot/formatter.py

def format_message(title, url, asset, price, sentiment, analysis):
    positive = sentiment.get("positive", 0.0)
    negative = sentiment.get("negative", 0.0)
    label = sentiment.get("label", "neutral")

    return f"""
📰 *{title}*

📊 *Signal*: {label.upper()}
🟢 Positive: {positive:.2f}
🔴 Negative: {negative:.2f}

💰 *Asset*: {asset} @ {price}

🧠 *AI Insight*
{analysis}

🔗 {url}

⭐️ *Feedback*: reply with /rate_1 to /rate_5
""".strip()