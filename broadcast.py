import asyncio
from pyrogram import Client, filters
from config import Config
from database import db
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid

@Client.on_message(filters.user(Config.OWNER_ID) & filters.command("broadcast"))
async def broadcast_handler(bot, message):
    if not message.reply_to_message:
        return await message.reply_text("<b>Usage:</b> Reply to a message with <code>/broadcast</code>")
    
    all_users = await db.users.find().to_list(length=10000)
    total_users = len(all_users)
    done = 0
    blocked = 0
    deleted = 0
    failed = 0
    
    sts = await message.reply_text(f"<b>🚀 Broadcast Started...</b>\nTotal Users: {total_users}")
    
    for user in all_users:
        user_id = int(user['user_id'])
        try:
            await message.reply_to_message.copy(chat_id=user_id)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await message.reply_to_message.copy(chat_id=user_id)
            done += 1
        except UserIsBlocked:
            blocked += 1
        except InputUserDeactivated:
            deleted += 1
        except Exception:
            failed += 1
        
        if done % 20 == 0:
            await sts.edit(f"<b>📊 Status:</b>\n✅ Success: {done}\n🚫 Blocked: {blocked}\n💀 Deleted: {deleted}")
            
    await sts.edit(f"<b>✅ Broadcast Completed!</b>\n\nTotal: {total_users}\nSuccess: {done}\nBlocked: {blocked}\nFailed: {failed}")
  
