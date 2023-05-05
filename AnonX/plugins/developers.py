
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
    command(["مطورين سي ار","المطورين","مطورين","مطورين cr"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://c.top4top.io/p_2680dmevf1.jpg,
        caption=f"""⩹━★⊷━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝━⊶★━⩺\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين cr ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n⩹━★⊷━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝━⊶★━⩺""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝐖𝐇𝐈𝐒𝐊𝐄𝐘⌯►", url=f"https://t.me/lV_P_Nl"), 
                 ],[
                    InlineKeyboardButton(
                        "قروب المساعده", url=f"https://t.me/HL_BG"),
                ],[
                    InlineKeyboardButton(
                        "قناة السورس", url=f"https://t.me/lN_B_Fl"),
                    InlineKeyboardButton(
                        "بوتي", url=f"https://t.me/HAYA01BOT"),
                ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝⚡", url=f"https://t.me/lN_B_Fl"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["وسكي انجم","محمد","وسكي","مبرمج","whiskey ","whis" ,"المطور"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("lV_P_Nl")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"⩹━★⊷━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝━⊶★━⩺\n\n🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :{usr.id}\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n⩹━★⊷━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝━⊶★━⩺**", 
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
    command(["مساعده","قروب المساعده","ساعدني"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("HL_BG")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"⩹━★⊷━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝━⊶★━⩺\n\n🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :{usr.id}\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n⩹━★⊷━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝━⊶★━⩺**", 
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
    command(["بوت","حياه","حياتي","سورس","بوتي"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("HAYA01BOT")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"⩹━★⊷━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝━⊶★━⩺\n\n🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :{usr.id}\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n⩹━★⊷━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝━⊶★━⩺**",

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
    command(["/api"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://c.top4top.io/p_2680dmevf1.jpg",
        caption=f"""⩹⊷━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝━━⩺\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس cr\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n⩹━━⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝━━⩺""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝐖𝐇𝐈𝐒𝐊𝐄𝐘⌯‹", url=f"https://t.me/lV_P_Nl"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝⚡", url=f"https://t.me/lN_B_Fl"),
                ],

            ]

        ),

    )