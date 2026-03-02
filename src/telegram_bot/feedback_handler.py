# callback_handler.py

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler
from firebase_admin import db
from datetime import datetime


# =============================
# KEYBOARD BUILDER
# =============================

def build_feedback_keyboard(news_id):
    keyboard = [
        [
            InlineKeyboardButton("1️⃣", callback_data=f"rate|{news_id}|1"),
            InlineKeyboardButton("2️⃣", callback_data=f"rate|{news_id}|2"),
            InlineKeyboardButton("3️⃣", callback_data=f"rate|{news_id}|3"),
            InlineKeyboardButton("4️⃣", callback_data=f"rate|{news_id}|4"),
            InlineKeyboardButton("5️⃣", callback_data=f"rate|{news_id}|5"),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


# =============================
# CALLBACK HANDLER
# =============================

async def handle_rating(update, context):
    query = update.callback_query
    await query.answer()

    data = query.data.split("|")

    if data[0] != "rate":
        return

    news_id = data[1]
    rating = int(data[2])
    user_id = query.from_user.id

    # مسیر ذخیره در Firebase
    rating_ref = db.reference(f"feedback/{news_id}/{user_id}")
    rating_ref.set({
        "rating": rating,
        "timestamp": datetime.utcnow().isoformat()
    })

    # محاسبه میانگین
    all_ratings_ref = db.reference(f"feedback/{news_id}")
    all_ratings = all_ratings_ref.get()

    if all_ratings:
        ratings_list = [
            v["rating"] for v in all_ratings.values()
            if isinstance(v, dict) and "rating" in v
        ]

        avg = sum(ratings_list) / len(ratings_list)

        db.reference(f"news/{news_id}/avg_rating").set(round(avg, 2))

    await query.edit_message_reply_markup(reply_markup=None)
    await query.message.reply_text(
        f"⭐️ Thank you! You rated this news: {rating}/5"
    )


def get_callback_handler():
    return CallbackQueryHandler(handle_rating)