import sqlite3
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

DB_PATH = "database.db"
MODEL_PATH = "sentiment_model.pkl"
VECTORIZER_PATH = "vectorizer.pkl"


def rating_to_label(r):
    if r <= 2:
        return 0
    elif r == 3:
        return 1
    else:
        return 2


def train_model():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("""
        SELECT n.text, f.rating
        FROM feedback f
        JOIN news n ON f.news_id = n.news_id
    """, conn)
    conn.close()

    if len(df) < 10:
        print("⚠ Not enough feedback to retrain.")
        return

    df["label"] = df["rating"].apply(rating_to_label)

    vectorizer = TfidfVectorizer(max_features=3000)
    X = vectorizer.fit_transform(df["text"])
    y = df["label"]

    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)

    print("✅ Model retrained with feedback.")