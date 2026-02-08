import os

class Config(object):
    # Koyeb থেকে ভেরিয়েবলগুলো রিড করার সঠিক পদ্ধতি
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", 0))
    API_HASH = os.environ.get("API_HASH", "")
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    OWNER_ID = int(os.environ.get("OWNER_ID", 8229228616)) # আপনার আইডি ডিফল্ট হিসেবে থাকল
    SHORTENER_API = os.environ.get("SHORTENER_API", "")
    SHORTENER_URL = os.environ.get("SHORTENER_URL", "gplinks.in")
