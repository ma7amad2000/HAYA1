import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app

import re
import sys
from os import getenv

from dotenv import load_dotenv



@app.on_message(
    command(["اصدار","حول"])
  
)
async def bkouqw(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://c.top4top.io/p_2680dmevf1.jpg",
        caption=f"""**⩹━★⊷⌯⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝⌯⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention}\n
★᚜ اسم سورس:-حياه
★᚜ نوعه:-ميوزك
★᚜ للغه برمجه:- بايثون
★᚜ اللغه:-اللغه العربيه ويدعم الانجليزيه 
★᚜ مجال تشغيل :- تشغيل بوتات الميوزك
★᚜ نظام تشغيل:-حياه بوت ميوزك
★᚜ الاصدار 4.0.1 pyrogram 
★᚜ تاريخ تاسيس:-21-3-2023
★᚜ مأسس حياه:- [𝐖𝐇𝐈𝐒𝐊𝐄𝐘༄►](https://t.me/lV_P_Nl)

**⩹━★⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌯⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝", url=f"https://t.me/lN_B_Fl"), 
                 ],[
                 InlineKeyboardButton(
                        "◁", callback_data="hpdtsnju"),
               ],
          ]
        ),
    )


