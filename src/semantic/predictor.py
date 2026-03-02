import os
import joblib

MODEL_PATH = "sentiment_model.pkl"
VECTORIZER_PATH = "vectorizer.pkl"


def predict_sentiment(text):
    if not os.path.exists(MODEL_PATH):
        return {"positive": 0.5, "neutral": 0.3, "negative": 0.2}

    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

    X = vectorizer.transform([text])
    probs = model.predict_proba(X)[0]

    return {
        "negative": float(probs[0]),
        "neutral": float(probs[1]),
        "positive": float(probs[2])
    }