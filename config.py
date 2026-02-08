import os

class Config(object):
    # Koyeb থেকে ভেরিয়েবলগুলো রিড করার সঠিক পদ্ধতি
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8055237838:AAEfWPinwBScqfdV4HgT0CrEo35c...") # আপনার টোকেন
    API_ID = int(os.environ.get("API_ID", 24670806)) 
    API_HASH = os.environ.get("API_HASH", "82134723a32b2cae76b9cfb3b1570745")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://botrunner:botrunner1234@cluster...")
    OWNER_ID = int(os.environ.get("OWNER_ID", 8229228616))
    SHORTENER_API = os.environ.get("SHORTENER_API", "e07aec576df2a9ed36f1b94b8017cc53b792496f")
    SHORTENER_URL = os.environ.get("SHORTENER_URL", "gplinks.in")
    VERIFY_MODE = os.environ.get("VERIFY_MODE", "True")
