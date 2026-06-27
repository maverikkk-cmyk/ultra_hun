# main.py

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "PhoenixUltra",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

if __name__ == "__main__":
    print("🔥 Phoenix Ultra Bot is Starting...")
    app.run()
  
