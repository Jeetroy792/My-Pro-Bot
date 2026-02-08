import asyncio
from bot import Bot
from flask import Flask
from threading import Thread
from config import Config

# Koyeb বা সার্ভার হেলথ চেক বজায় রাখার জন্য
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Alive & Running!"

def run_flask():
    # পোর্ট ৮০০০ এ সার্ভার চলবে
    app.run(host='0.0.0.0', port=8000)

async def main():
    # ফ্ল্যাস্ক সার্ভার আলাদা থ্রেডে চালু করা
    Thread(target=run_flask).start()
    
    # মেইন বট ক্লায়েন্ট শুরু করা
    print("🚀 Initializing SHREENATH DEVELOPER Bot...")
    forward_bot = Bot()
    
    await forward_bot.start()
    print("✅ Bot is Online and ready to serve customers!")
    
    # বটকে অনন্তকাল চালু রাখা
    await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("🛑 Bot Stopped Manually.")
      
