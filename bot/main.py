# bot/main.py

import asyncio
from pyrogram import Client
from bot.config import BOT_TOKEN, API_ID, API_HASH

# Handlers import
from bot.handlers import (
    register_start,
    register_cap,
    register_account,
    register_withdraw,
    register_support,
    register_admin
)

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
    register_start(app)
    register_cap(app)
    register_account(app)
    register_withdraw(app)
    register_support(app)
    register_admin(app)

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
