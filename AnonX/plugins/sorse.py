import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

@app.on_message(
    command(["سورس مين","سورس","السورس","سورسي", "cr"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1488d38c8157537b9213f.jpg",
        caption=f"""╭═★⊷⌯⧼[⌞ 𝐒𝐎𝐔𝐑𝐂 • 𝐇𝐀𝐘𝐀⌝](https://t.me/lN_B_Fl)⧽⌯⊶★═╮\n★‹ [⌞ 𝐒𝐎𝐔𝐑𝐂 • 𝐇𝐀𝐘𝐀⌝𝐀](https://t.me/lN_B_Fl)\n★‹ [𝐇𝐀𝐘𝐀 𝐌𝐔𝐒𝐈𝐂 『 𝒃𝒐𝒕 ⏎ 』](https://t.me/HAYA01BOT?startgroup=true)\n★‹ [『𝐖𝐇𝐈𝐒𝐊𝐄𝐘 ⏎ 』](https://t.me/ssxhh)\n★‹ [𝐖𝐇𝐈𝐒𝐊𝐄𝐘 ](https://t.me/ppblb)\n╰═★⊷⌯⧼[⌞ 𝐒𝐎𝐔𝐑𝐂 • 𝐇𝐀𝐘𝐀⌝](https://t.me/lN_B_Fl)⧽⌯⊶★═╯\n ⍟ Welcome to source 𝐖𝐇𝐈𝐒𝐊𝐄𝐘 """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "『𝐖𝐇𝐈𝐒𝐊𝐄𝐘 ⏎ 』༄►", url=f"https://t.me/ssxhh"), 
                ],[
                    InlineKeyboardButton(
                        "⌞ 𝐒𝐎𝐔𝐑𝐂 • 𝐇𝐀𝐘𝐀⌝⚡️", url=f"https://t.me/lN_B_Fl"),
                ],[
                    InlineKeyboardButton(
                        "𝐀𝐃𝐃 𝐌𝐄💞", url=f"https://t.me/HAYA01BOT?startgroup=true"),
                ],

            ]

        ),

    )



@app.on_message(command(["غنيلي", "غني", "غ", "🎙 ¦ غـنيـلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغـنـية لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )