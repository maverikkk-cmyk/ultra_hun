# plugins/admin.py

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatPermissions
from config import SUDO_USERS

# Admin Command Center with Clean UI
@Client.on_message(filters.command("admin") & filters.group)
async def admin_panel(client, message):
    # Check if sender is admin or sudo user
    member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not (member.status.value in ["administrator", "owner"] or message.from_user.id in SUDO_USERS):
        return await message.reply_text("❌ Aapke paas permissions nahi hain.")

    await message.reply_text(
        "⚡ **Phoenix Ultra - Admin Control Center**\n\nSelect an action below:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Ban User 🚫", callback_data="cb_ban"),
             InlineKeyboardButton("Mute User 🔇", callback_data="cb_mute")],
            [InlineKeyboardButton("Group Settings ⚙️", callback_data="cb_settings")]
        ])
    )

# Direct Ban Command
@Client.on_message(filters.command("ban") & filters.group)
async def ban_user(client, message):
    if not message.reply_to_message:
        return await message.reply_text("❗ Kisi user ke message par reply karke `/ban` likhein.")
    
    target_user = message.reply_to_message.from_user
    await client.ban_chat_member(message.chat.id, target_user.id)
    await message.reply_text(f"🚫 **Banned:** {target_user.mention} (`{target_user.id}`)")

# Direct Mute Command
@Client.on_message(filters.command("mute") & filters.group)
async def mute_user(client, message):
    if not message.reply_to_message:
        return await message.reply_text("❗ Kisi user ke message par reply karke `/mute` likhein.")
    
    target_user = message.reply_to_message.from_user
    await client.restrict_chat_member(
        message.chat.id, 
        target_user.id, 
        ChatPermissions(can_send_messages=False)
    )
    await message.reply_text(f"🔇 **Muted:** {target_user.mention}")
  
