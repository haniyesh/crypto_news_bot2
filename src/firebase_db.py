import firebase_admin
from firebase_admin import credentials, db
from firebase_admin import db
# مسیر فایل JSON
cred = credentials.Certificate("serviceAccountKey.json")

# دیتابیس URL را تغییر بده با پروژه خودت
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://cryptonews-72c0d.firebaseio.com/'
})

def save_news(news_id, news_data):
    ref = db.reference(f'news/{news_id}')
    ref.set(news_data)

def save_feedback(news_id, user_id, rating):
    ref = db.reference(f'feedback/{news_id}/{user_id}')
    ref.set({"rating": rating})

def get_feedback(news_id):
    ref = db.reference(f'feedback/{news_id}')
    return ref.get()
def get_last_sent_time():
    ref = db.reference("bot_state/last_sent_timestamp")
    return ref.get()

def save_last_sent_time(timestamp_str):
    ref = db.reference("bot_state")
    ref.update({
        "last_sent_timestamp": timestamp_str
    })