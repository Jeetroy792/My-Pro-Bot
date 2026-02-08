from pyrogram import Client, filters
@Client.on_callback_query(filters.regex("set_menu"))
async def settings_menu(bot, query):
    buttons = [
        [InlineKeyboardButton("🕒 Set Delay", callback_data="set_delay"),
         InlineKeyboardButton("🔄 Uniquify", callback_data="toggle_unique")],
        [InlineKeyboardButton("📡 Channels", callback_data="my_chans"),
         InlineKeyboardButton("🔑 Session", callback_data="my_session")],
        [InlineKeyboardButton("🔙 Back", callback_data="start_back")]
    ]
    await query.message.edit("<b>🛠 Configuration Menu</b>\nCustomize your bot experience below:", reply_markup=InlineKeyboardMarkup(buttons))
  
