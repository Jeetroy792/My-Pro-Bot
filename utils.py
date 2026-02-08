import asyncio
from pyrogram import Client
from config import Config

class STS:
    def __init__(self, forward_id):
        self.id = forward_id
        self.data = {}

    async def store(self, from_chat, to_chat, limit, last_id):
        self.data[self.id] = [from_chat, to_chat, limit, last_id]

    async def get(self):
        return self.data.get(self.id)

async def get_user_bot(session_string):
    """ইউজার সেশন থেকে অটোমেটিক ক্লায়েন্ট তৈরি করা"""
    try:
        ubot = Client(
            name="UserBot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            session_string=session_string
        )
        return ubot
    except Exception as e:
        print(f"UserBot Error: {e}")
        return None
      
