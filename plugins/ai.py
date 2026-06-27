# plugins/ai.py

import urllib.parse
from pyrogram import Client, filters
import google.generativeai as genai
from config import GEMINI_KEY

# AI Config
genai.configure(api_key=GEMINI_KEY)
ai_model = genai.GenerativeModel('gemini-pro')

@Client.on_message(filters.command("ai"))
async def ai_core(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        return await message.reply_text("❗ Apna sawal likhein.\nExample: `/ai Quantum physics kya hai?`")
    
    prompt = args[1]
    thinking_msg = await message.reply_text("🧠 **Phoenix AI Thinking...**")
    
    try:
        response = ai_model.generate_content(prompt)
        await thinking_msg.edit_text(f"🤖 **Phoenix AI:**\n\n{response.text}")
    except Exception as e:
        await thinking_msg.edit_text(f"❌ **AI Error:** `{e}`")

@Client.on_message(filters.command("imagine"))
async def imagine_core(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        return await message.reply_text("❗ Prompt likhein.\nExample: `/imagine cyberpunk city, neon lights`")
        
    prompt = args[1]
    generating_msg = await message.reply_text("🎨 **Generating Art...**")
    
    try:
        encoded_prompt = urllib.parse.quote(prompt)
        # Premium no-key API for ultra image generation
        image_url = f"https://image.pollinations.ai/p/{encoded_prompt}?width=1080&height=1080&nologo=true"
        
        await message.reply_photo(photo=image_url, caption=f"✨ **Prompt:** {prompt}")
        await generating_msg.delete()
    except Exception as e:
        await generating_msg.edit_text(f"❌ **Art Error:** `{e}`")
      
