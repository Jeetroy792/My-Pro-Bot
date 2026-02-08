import os

class Config:
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    OWNER_ID = int(os.environ.get("OWNER_ID", ""))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    SHORTENER_URL = os.environ.get("SHORTENER_URL", "shareus.io")
    SHORTENER_API = os.environ.get("SHORTENER_API", "")
  
