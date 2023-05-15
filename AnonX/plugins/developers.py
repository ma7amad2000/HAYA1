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

#       #             #  #####  #####      ####
#        #           #  #         #            #     #
#          #        #  #####   #            #####     
#           #    #    #          #     ##    #     #
#              #       #####   ######   #     #
                
                
@app.on_message(
    command(["مطورين حياه","المطورين","مطورين","مطورين"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://c.top4top.io/p_2680dmevf1.jpg",
        caption=f"""**⩹━★⊷━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀 ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين حياه ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀 ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓏺᭙ɦᎥ᥉ƙᥱᥡ", url=f"https://t.me/bp_bp"), 
                 ],[
                    InlineKeyboardButton(
                        "chaneall haya", url=f"https://t.me/HL_BG"),
                ],[
                    InlineKeyboardButton(
                        "channel", url=f"https://t.me/hl_bg"),
                    InlineKeyboardButton(
                        "MyBot", url=f"https://t.me/HAYA01BOT"),
                ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀 ⌝⚡", url=f"https://t.me/HL_BG"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["وسكي","ويسكي","الوسكي","مبرمج","whiskey","محمد" ,"المطور","مبرمج السورس"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("bp_bp")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀 ⌝━⊶★━⩺\n\n🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\nᴀʀʀᴀɴɢᴇᴅ :مطور السورس \n\n**⩹━★⊷━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["قروب مساعده","مساعده","الدليل"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("HL_BG")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀 ⌝━⊶★━⩺\n\n🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━★⊷━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["حياة","حياتي","حياه","بوت","بوتي"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("HAYA01BOT")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀 ⌝━⊶★━⩺\n\n🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━★⊷━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    


@app.on_message(
    command(["ذكاء حياه"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://c.top4top.io/p_2680dmevf1.jpg",
        caption=f"""**⩹⊷━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀 ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس حياه\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓏺᭙ɦᎥ᥉ƙᥱᥡ‹", url=f"https://t.me/bp_bp"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀 ⌝⚡", url=f"https://t.me/HL_BG"),
                ],

            ]

        ),

    )



    
