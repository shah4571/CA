# bot/main.py

import asyncio
from pyrogram import Client
from bot.config import BOT_TOKEN, API_ID, API_HASH
from bot.handlers import init_handlers   # ✅ শুধু init_handlers ইমপোর্ট করো

async def main():
    # Create Pyrogram Client
    app = Client(
        "RajuNewBot",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
        parse_mode="html"  # Optional: allows HTML formatting
    )

    # Register all handlers
    init_handlers(app)   # ✅ সব হ্যান্ডলার একসাথে রেজিস্টার হবে

    print("[INFO] Bot is starting...")

    # Start bot
    async with app:
        print("[INFO] Bot is running!")
        await app.idle()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("[INFO] Bot stopped manually")
