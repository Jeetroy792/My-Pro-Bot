from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database import db
from config import Config
import time

@Client.on_message(filters.private & filters.command("start"))
async def start(bot, message):
    await db.add_user(message.from_user.id)
    # ক্লেইম ভেরিফিকেশন চেক
    if len(message.command) > 1 and message.command[1].startswith("verify_"):
        await db.set_premium(message.from_user.id, 86400) # ২৪ ঘণ্টা
        return await message.reply("<b>✅ Success! Premium activated for 4 hours.</b>")

    text = "<b>👋 Welcome to Pro Forwarder v2.0</b>\n\nThe most powerful automation tool for your business."
    buttons = [
        [InlineKeyboardButton("🚀 Start Forward", callback_data="fwd_start"),
         InlineKeyboardButton("⚙️ Settings", callback_data="set_menu")],
        [InlineKeyboardButton("💎 Buy Premium", callback_data="plan_buy"),
         InlineKeyboardButton("🎁 Free Claim", callback_data="claim_free")],
        [InlineKeyboardButton("📊 My Stats", callback_data="user_stats"),
         InlineKeyboardButton("❓ Help", callback_data="help_guide")]
    ]
    await message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons))

# --- ADMIN ONLY SHORTENER COMMAND ---
@Client.on_message(filters.user(Config.OWNER_ID) & filters.command("set_shortner"))
async def set_admin_shortner(bot, message):
    if len(message.command) < 3:
        return await message.reply("<b>Usage:</b> `/set_shortner gplinks.com e07aec576df2a9ed36f1b94b8017cc53b792496f`")
    
    endpoint = message.command[1]
    api_key = message.command[2]
    await db.update_config("shortner", {"endpoint": endpoint, "api": api_key})
    await message.reply(f"<b>✅ Admin Shortener updated to: {endpoint}</b>")

# অন্যান্য কমান্ডগুলো (বাকি ১৯টি কমান্ডের লিস্ট আমি মডিউল আকারে দেব)
