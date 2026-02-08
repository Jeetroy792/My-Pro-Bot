import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database import db
from config import Config

# আপনার শর্টনার ডিটেইলস (এখান থেকে আপনার ইনকাম হবে)
SHORTENER_URL = "shareus.io" # অথবা আপনার পছন্দের শর্টনার
SHORTENER_API = "your_api_key_here"

@Client.on_message(filters.private & filters.command("plan"))
async def show_plans(bot, message):
    text = (
        "<b>💎 Choose Your Plan:</b>\n\n"
        "1. <b>Premium Plan</b> (Unlimited Forwarding)\n"
        "Price: 100 TK or <b>Free via Task</b>\n"
    )
    buttons = [
        [InlineKeyboardButton("💰 Pay Now", url="https://t.me/your_admin_id")],
        [InlineKeyboardButton("🎁 Claim Free (Click-bait)", callback_data="claim_free_task")]
    ]
    await message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons))

@Client.on_callback_query(filters.regex("claim_free_task"))
async def generate_claim_link(bot, query):
    user_id = query.from_user.id
    
    # একটি ইউনিক লিংক তৈরি করা যা শর্টনার দিয়ে যাবে
    # কাস্টমার এই লিংকে ক্লিক করলে আপনার ইনকাম হবে
    original_link = f"https://t.me/{bot.me.username}?start=verify_{user_id}"
    
    # শর্টনার দিয়ে লিংকটি ছোট করা (আগের দেওয়া get_shortlink ফাংশন ব্যবহার করবেন)
    # এখানে আমি সরাসরি ছোট লিংক দেখাচ্ছি উদাহরণের জন্য
    short_link = f"https://{SHORTENER_URL}/api?api={SHORTENER_API}&url={original_link}"
    
    text = (
        "<b>🚀 Free Plan Claim করার জন্য নিচের লিংকে ক্লিক করুন:</b>\n\n"
        "লিংকটি ওপেন করে 'Continue' করুন। সফলভাবে ভেরিফাই হলে আপনার ২৪ ঘণ্টার জন্য প্রিমিয়াম প্ল্যান এক্টিভেট হয়ে যাবে।"
    )
    buttons = [[InlineKeyboardButton("🔗 ওপেন করুন (Unlock Plan)", url=short_link)]]
    await query.message.edit(text, reply_markup=InlineKeyboardMarkup(buttons))
  
