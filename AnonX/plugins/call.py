import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, VoiceChatStarted, VoiceChatEnded
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX.core.call import Anon
from AnonX.utils.database import get_assistant

@app.on_message(filters.voice_chat_started)
async def stcall(client: Client, message: Message): 
      Startt = "بدت المكالمه ارقو هدرزو😻♥️..."
      await message.reply_text(Startt)

@app.on_message(filters.voice_chat_ended)
async def encall(client: Client, message: Message): 
      Enddd = "اصكرت المكالمه فاتكم الجو🥲💔"
      await message.reply_text(Enddd)

@app.on_message(filters.voice_chat_members_invited)
async def zoharyy(client: Client, message: Message): 
           text = f"- هذا دار {message.from_user.mention}\n -دعوه لـ هذا : "
           x = 0
           for user in message.voice_chat_members_invited.users:
             try:
               text += f"[{user.first_name}](tg://user?id={user.id}) "
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text} ")
           except:
             pass
