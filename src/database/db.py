# database.py

import sqlite3

DB_NAME = "crypto_news.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS news (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        source TEXT,
        publishedAt TEXT,
        sent_time TEXT,
        asset TEXT,
        initial_price REAL,
        user_rating INTEGER
    )
    """)

    conn.commit()
    conn.close()


def insert_news(news_item, asset, price):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO news (title, source, publishedAt, sent_time, asset, initial_price)
    VALUES (?, ?, ?, datetime('now'), ?, ?)
    """, (
        news_item["title"],
        news_item["source"],
        news_item["publishedAt"],
        asset,
        price
    ))

    news_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return news_id


def save_rating(news_id, rating):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE news
    SET user_rating=?
    WHERE id=?
    """, (rating, news_id))

    conn.commit()
    conn.close()