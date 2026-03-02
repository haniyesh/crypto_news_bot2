CREATE TABLE IF NOT EXISTS news_signals (
    id TEXT PRIMARY KEY,
    timestamp DATETIME,
    source TEXT,
    sentiment REAL,
    confidence REAL,
    uncertainty REAL,
    signal TEXT
);

CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    news_id TEXT,
    price_before REAL,
    price_after REAL,
    horizon_minutes INTEGER,
    outcome REAL,
    manual_label INTEGER
);
CREATE TABLE IF NOT EXISTS
manual_feedbacks(
    id integer Primary KEY AUTOINCREMENT,
    news_id TEXT NOT NULL,
    telegram_message_id INTEGER NOT NULL,
    score INTEGER CHECK (score BETWEEN 1 AND 5)
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP);
