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
    command(["اصدار"])
  
)
async def bkouqw(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://b.top4top.io/p_2682mb2f41.jpg",
        caption=f"""**⩹━★⊷⌯⌞ 𓏺᥉᥆ᥙᖇᥴᥱ ꫝꪖꪗꪖ⌝⌯⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention}\n
★᚜ اسم سورس:-حياه
★᚜ نوعه:-ميوزك
★᚜ للغه برمجه:- بايثون
★᚜ اللغه:-اللغه العربيه ويدعم الانجليزيه 
★᚜ مجال تشغيل :- تشغيل بوتات الميوزك
★᚜ نظام تشغيل:-cr بوت ميوزك
★᚜ الاصدار 4.0.1 pyrogram 
★᚜ تاريخ تاسيس:-21-3-2023
★᚜ مأسس حياه:- [𓆩˹ 𓏺᭙ɦᎥ᥉ƙᥱᥡ༄►](https://t.me/bP_bP)

**⩹━★⊷⌯𓏺᥉᥆ᥙᖇᥴᥱ ꫝꪖꪗꪖ⌝⌯⊶★━⩺ ⌯⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⌞𓏺᥉᥆ᥙᖇᥴᥱ ꫝꪖꪗꪖ⌝⌯⊶★━⩺ ⌝", url=f"https://t.me/HL_BG"), 
                 ],[
                 InlineKeyboardButton(
                        "◁", callback_data="hpdtsnju"),
               ],
          ]
        ),
    )


