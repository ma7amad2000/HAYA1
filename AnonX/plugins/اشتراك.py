import asyncio
import os
import time
import requests
from config import USER_CHANNEL, BOT_TOKEN
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint



       
@app.on_message(
    command(["/start"])
    & ~filters.edited
)
async def start(client: Client, message: Message):
       m = message.chat.id
       user = message.from_user.mention
       do = requests.get(f"https://api.telegram.org/app{BOT_TOKEN}/getChatMember?chat_id=@{CHANNEL}&user_id={message.from_user.id}").text
       if do.count("left") or do.count("Bad Request: user not found"):
          await message.reply_text(f"**Join [this channel](t.me/{USER_CHANNEL}) first to be able to use the app ✨**", disable_web_page_preview=True,
          reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                        "انظم الى القناه",
                        url=f'https://t.me/{USER_CHANNEL}'),
                        ],
                    ]
                )
            ) 
       else:
         await app.send_message(m, f"**Hello my friend ( {message.from_user.username} ) **",
       reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                        "𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝞝𝙔.",
                        url=f'https://t.me/BP_BP'),
                        ],[
                            InlineKeyboardButton(
                        "𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼",
                        url=f'https://t.me/hl_bg'),
                        ],
                    ]
                )
            ) 
            
            
            
            
     
