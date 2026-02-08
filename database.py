from motor.motor_asyncio import AsyncIOMotorClient
from config import Config
import time

class Database:
    def __init__(self):
        self.client = AsyncIOMotorClient(Config.DATABASE_URL)
        self.db = self.client["Forwarder_Pro"]
        self.users = self.db["users"]

    async def add_user(self, user_id):
        user = {"user_id": user_id, "plan": "Free", "expiry": 0, "channels": [], "sessions": None}
        await self.users.update_one({"user_id": user_id}, {"$set": user}, upsert=True)

    async def get_user(self, user_id):
        return await self.users.find_one({"user_id": user_id})

    async def set_premium(self, user_id, seconds):
        expiry = int(time.time()) + seconds
        await self.users.update_one({"user_id": user_id}, {"$set": {"plan": "Premium", "expiry": expiry}})

    async def is_premium(self, user_id):
        user = await self.get_user(user_id)
        if user and user.get("plan") == "Premium":
            if user.get("expiry") > time.time():
                return True
        return False

db = Database()
