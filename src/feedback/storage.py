import sqlite3

DB_PATH = "database.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS news (
            news_id TEXT PRIMARY KEY,
            text TEXT
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            news_id TEXT,
            rating INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_news(news_id: str, text: str):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT OR IGNORE INTO news (news_id, text) VALUES (?, ?)",
        (news_id, text)
    )
    conn.commit()
    conn.close()


def save_feedback(news_id: str, rating: int):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO feedback (news_id, rating) VALUES (?, ?)",
        (news_id, rating)
    )
    conn.commit()
    conn.close()