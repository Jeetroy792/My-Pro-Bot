import asyncio
from pyrogram import Client, filters
from database import db
from config import Config

@Client.on_callback_query(filters.regex("claim_free"))
async def claim_logic(bot, query):
    user_id = query.from_user.id
    admin_short = await db.get_config("shortner")
    
    if not admin_short:
        return await query.answer("Admin hasn't set any shortner yet!", show_alert=True)
        
    original_link = f"https://t.me/{bot.me.username}?start=verify_{user_id}"
    # শর্টনারের মাধ্যমে লিংক তৈরি (আপনার ইনকাম এখানে হবে)
    short_link = f"https://{admin_short['endpoint']}/api?api={admin_short['api']}&url={original_link}"
    
    text = (
        "<b>🎁 Claim 4 Hours Free Premium</b>\n\n"
        "To unlock all features for free, click the link below and complete the captcha."
    )
    btn = [[InlineKeyboardButton("🔗 Unlock Now", url=short_link)]]
    await query.message.edit(text, reply_markup=InlineKeyboardMarkup(btn))
  
