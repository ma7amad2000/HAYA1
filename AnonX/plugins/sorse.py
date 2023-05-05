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

    command(["سورس مين","سورس","السورس","سورسي", "يا سورس"])

    & ~filters.edited

)

async def huhh(client: Client, message: Message):

    await message.reply_photo(

        photo=f"https://telegra.ph/file/d790b3a9cedeb8b6ca37e.jpg",

        caption=f"""╭──── • ✭ • ────╮

✭ [ѕᴏᴜʀᴄᴇ ѕᴇᴍᴏ](https://t.me/FTTUTY)

✭ [ᴅᴇᴠ ѕᴀᴍɪʀ](https://t.me/DEV_SAMIR)

╰──── • ✭ • ────╯

✭ ᴛʜᴇ ʙᴇѕᴛ ѕᴏᴜʀᴄᴇ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ """,

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        "‹ ᴅᴇᴠ ѕᴀᴍɪʀ ›", url=f"https://t.me/DEV_SAMIR"), 

                ],[

                    InlineKeyboardButton(

                        "‹ 𝚜𝚘𝚞𝚛𝚌𝚎 𝚜𝚎𝚖𝚘 ›", url=f"https://t.me/DEV_SAMIR"),

                ],[

                    InlineKeyboardButton(

                        "‹ للتنصيب راسلني ›", url=f"https://t.me/DEV_SAMIR"),

                ],

            ]

        ),

    )
@app.on_message(comman(["صوره","صور"]))
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
