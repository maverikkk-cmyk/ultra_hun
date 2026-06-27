# plugins/tools.py

import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("weather"))
async def live_weather(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        return await message.reply_text("❗ City name batayein.\nExample: `/weather Mumbai`")
        
    city = args[1]
    # Advanced weather format from wttr.in
    res = requests.get(f"https://wttr.in/{city}?format=%C+|++🌡️+%t++|++💧+%h++|++💨+%w")
    if res.status_code == 200:
        await message.reply_text(f"🌍 **Weather Report for {city.capitalize()}:**\n\n📊 `{res.text.strip()}`")
    else:
        await message.reply_text("❌ City nahi mili.")

@Client.on_message(filters.command("crypto"))
async def crypto_market(client, message):
    try:
        data = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd,inr").json()
        
        btc_usd = data['bitcoin']['usd']
        eth_usd = data['ethereum']['usd']
        sol_usd = data['solana']['usd']
        
        text = (
            "📈 **Phoenix Live Crypto Analytics**\n\n"
            f"🪙 **Bitcoin (BTC):** ${btc_usd:,}\n"
            f"🪙 **Ethereum (ETH):** ${eth_usd:,}\n"
            f"🪙 **Solana (SOL):** ${sol_usd:,}"
        )
        await message.reply_text(text)
    except Exception:
        await message.reply_text("❌ Market data temporarily unavailable.")
      
