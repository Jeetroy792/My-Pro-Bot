@Client.on_message(filters.private & filters.command("start"))
async def start_handler(bot, message):
    if len(message.command) > 1 and message.command[1].startswith("verify_"):
        user_id = message.from_user.id
        
        # ডাটাবেসে ইউজারকে ৪ ঘণ্টার জন্য প্রিমিয়াম করে দেওয়া
        # আপনি আপনার database.py এ এই ফাংশনটি যোগ করে নেবেন
        await db.set_premium(user_id, hours=4)
        
        await message.reply_text("<b>✅ অভিনন্দন! আপনি সফলভাবে ফ্রি টাস্ক সম্পন্ন করেছেন।</b>\nআপনার প্রিমিয়াম প্ল্যান আগামী ২৪ ঘণ্টার জন্য এক্টিভেট করা হয়েছে।")
        return

    await message.reply_text("স্বাগতম! প্ল্যান দেখতে /plan লিখুন।")
  
