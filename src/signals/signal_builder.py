from config.settings import CONFIDENCE_THRESHOLD

def build_signal(sentiment, confidence):
    if confidence < CONFIDENCE_THRESHOLD:
        return "⚪ Neutral (Low confidence)"
    if sentiment > 0.2:
        return "🟢 Bullish"
    if sentiment < -0.2:
        return "🔴 Bearish"
    return "🟡 Neutral"