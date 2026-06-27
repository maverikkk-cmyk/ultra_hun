# plugins/downloader.py

import os
import time
from pyrogram import Client, filters
from yt_dlp import YoutubeDL

@Client.on_message(filters.command("dl"))
async def high_speed_downloader(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        return await message.reply_text("❗ Link provide karein.\nExample: `/dl https://link.com`")
    
    url = args[1]
    status_msg = await message.reply_text("⚡ **Phoenix HyperDL:** Link extract ho raha hai...")
    
    file_path = f"dl_{int(time.time())}.mp4"
    ydl_opts = {
        'outtmpl': file_path,
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'quiet': True
    }
    
    try:
        await status_msg.edit_text("📥 **Downloading Media...**")
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
        await status_msg.edit_text("🚀 **Uploading to Telegram Cloud...**")
        await message.reply_video(video=file_path, caption="✅ **Phoenix Ultra Downloader**")
        
        os.remove(file_path)
        await status_msg.delete()
    except Exception as e:
        if os.path.exists(file_path):
            os.remove(file_path)
        await status_msg.edit_text(f"❌ **Error:** `{str(e)[:100]}`")
      
