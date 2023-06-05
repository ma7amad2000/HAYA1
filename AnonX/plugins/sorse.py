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
    command(["صورص","سورس","السورس","سورس حياه", "haya"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://b.top4top.io/p_2682mb2f41.jpg",
        caption=f"""
  ╭═★⊷⌯[⧼⌞𝑆𝑂𝑈𝑅𝐶𝐸 𝐻𝐴𝑌𝐴⧽](https://t.me/HL_BG)⌯⊶★═╮
   
   么  [𝑆𝑂𝑈𝑅𝐶𝐸 𝐻𝐴𝑌𝐴⋆♡](https://t.me/HL_BG) 𝐶𝐻𝐴𝑁𝑁𝐸𝐿

   么  [𝑊𝐻𝐼𝑆𝐾𝐸𝑌⋆♡](https://t.me/bP_bP) 𝐷𝐸𝑉𝐸L𝑂𝑃𝐸𝑅    

   么  [َِ𝑀𝑌𝐺𝑅𝑂𝑈𝑃⋆♡](t.me/HL_BG) 𝐺𝑅𝑂𝑈𝑃 𝐻𝐸L𝑃 

   么  [𝑀𝑌𝐵𝑂𝑇⋆♡](t.me/HAYA01BOT) 𝑀𝑈𝑆𝐼𝐶 𝐵𝑂𝑇

  ╰───么[𝐻𝐴𝑌𝐴](https://t.me/HL_BG)  • ◈ •[𝐻𝐴𝑌𝐴](https://t.me/HL_BG)  么───╯ 
  
 ⍟𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᯓ𓆩𓏺᭙ɦᎥ᥉ƙᥱᥡ ˹ ♡", url=f"https://t.me/bP_bP"), 
                ],[
                    InlineKeyboardButton(
                        "⩹━⊷⌯ 𓏺᥉᥆ᥙᖇᥴᥱ ꫝꪖꪗꪖ♡", url=f"t.me/HL_BG"),
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

    
 
