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
    command(["سورس من","سورس","السورس","سورسي", "سورس حياه"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://c.top4top.io/p_2680dmevf1.jpg",
        caption=f"""╭═★⊷⌯⧼[⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝](https://t.me/lN_B_Fl)⧽⌯⊶★═╮\n★‹ [⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝𝐀](https://t.me/lN_B_Fl)\n★‹ [𝐇𝐀𝐘𝐀 𝐌𝐔𝐒𝐈𝐂 『 𝒃𝒐𝒕 ⏎ 』](https://t.me/HAYA01BOT?startgroup=true)\n★‹ [『𝐖𝐇𝐈𝐒𝐊𝐄𝐘 ⏎ 』](https://t.me/lV_P_Nl)\n★‹ [𝐖𝐇𝐈𝐒𝐊𝐄𝐘 ](https://t.me/ppblb)\n╰═★⊷⌯⧼[⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝](https://t.me/lN_B_Fl)⧽⌯⊶★═╯\n ⍟𝑊𝐸𝐿𝐶𝑂𝑀𝐸 𝑇𝑂 𝑆𝑂𝑈𝑅𝐶𝐸 𝐻𝐴𝑌𝐴 𖠅 """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "『𝐖𝐇𝐈𝐒𝐊𝐄𝐘 ⏎ 』༄►", url=f"https://t.me/lV_P_Nl"), 
                ],[
                    InlineKeyboardButton(
                        "⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝⚡️", url=f"https://t.me/lN_B_Fl"),
                ],[
                    InlineKeyboardButton(
                        "𝐀𝐃𝐃 𝐌𝐄💞", url=f"https://t.me/HAYA01BOT?startgroup=true"),
                ],

            ]

        ),

    )



@app.on_message(command(["غنيلي", "غني", "غ", "حياه غنيلي"]))
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
    
@app.on_message(command(["صورة","صور"]))
async def ihd(client: Client, message: Message):
    rs = random.randint(39,148)
    url = f"https://t.me/GTTUTY/{rs}"
    await client.send_photo(message.chat.id,url,caption="💕 ¦ تـم اختيـار الصوره لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
