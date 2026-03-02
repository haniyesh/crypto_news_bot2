# src/database/feedback_repo.py

from database.db import get_connection

def save_manual_feedback(news_id, telegram_message_id, score):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO manual_feedback (news_id, telegram_message_id, score)
        VALUES (?, ?, ?)
        """,
        (news_id, telegram_message_id, score)
    )
    print("send")

    conn.commit()
    conn.close()