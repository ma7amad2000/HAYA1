import asyncio

import os
import time
import requests
from config import OWNER_ID
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين haya","المطورين","مطورين","مطورين حياه"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://b.top4top.io/p_2682mb2f41.jpg",
        caption=f"""**⩹━★⊷━⌞ 𓏺᥉᥆ᥙᖇᥴᥱ ꫝꪖꪗꪖ ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين حياه ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ 𓏺᥉᥆ᥙᖇᥴᥱ ꫝꪖꪗꪖ ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᯓ𓆩𓏺᭙ɦᎥ᥉ƙᥱᥡ ˹َّّ ", url=f"https://t.me/bp_bp"), 
                 ],[
                    
                
                    InlineKeyboardButton(
                        "𝘿𝘼𝘿✹⃝‌꙰🇨🇾𝙁𝘼𝙍𝘾𝙊𒀭", url=f"https://t.me/A_XR_0"),
                ],[
                    
                
                    InlineKeyboardButton(
                        "★⌞  𓏺᥉᥆ᥙᖇᥴᥱ ꫝꪖꪗꪖ ⌝⚡", url=f"https://t.me/HL_BG"),
                
        ],

            ]

        ),

    )








@app.on_message(
    command(["المطور","ويسكي","مبرمج السورس","وسكي","الوسكي"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("bp_bp")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞𓏺᥉᥆ᥙᖇᥴᥱ ꫝꪖꪗꪖ ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞𓏺᥉᥆ᥙᖇᥴᥱ ꫝꪖꪗꪖ ⌝━⊶★━⩺**", 
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
    command(["قناة السورس"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("HL_BG")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞  𓏺᥉᥆ᥙᖇᥴᥱ ꫝꪖꪗꪖ ⌝━⊶★━⩺\n\n¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞  𓏺᥉᥆ᥙᖇᥴᥱ ꫝꪖꪗꪖ ⌝━⊶★━⩺**", 
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
    command(["مطورك","محمد","حمادي"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("bp_bp")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞  𓏺᥉᥆ᥙᖇᥴᥱ ꫝꪖꪗꪖ ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}مطوري\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞  𓏺᥉᥆ᥙᖇᥴᥱ ꫝꪖꪗꪖ ⌝━⊶★━⩺**", 
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
    command(["مطور"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    user_OW = config.OWNER_ID
    usr = await client.get_chat("user_OW")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞  𓏺᥉᥆ᥙᖇᥴᥱ ꫝꪖꪗꪖ ⌝━⊶★━⩺\n\n ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{user_OW}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞  𓏺᥉᥆ᥙᖇᥴᥱ ꫝꪖꪗꪖ ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                text="👤 مطور البوت", user_id=OWNER
            )
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
        photo=f"https://b.top4top.io/p_2682mb2f41.jpg",
        caption=f"""**⩹⊷━⌞  𓏺᥉᥆ᥙᖇᥴᥱ ꫝꪖꪗꪖ ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس حياه\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞  𓏺᥉᥆ᥙᖇᥴᥱ ꫝꪖꪗꪖ ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᯓ𓆩𓏺᭙ɦᎥ᥉ƙᥱᥡ ˹َّّ", url=f"https://t.me/bp_bp"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞  𓏺᥉᥆ᥙᖇᥴᥱ ꫝꪖꪗꪖ ⌝⚡", url=f"https://t.me/HL_BG"),
                ],

            ]

        ),

    )



@app.on_message(
    command(["قرأن"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://b.top4top.io/p_2682mb2f41.jpg",
        caption=f"""**⩹⊷━⌞  𓏺᥉᥆ᥙᖇᥴᥱ ꫝꪖꪗꪖ ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم تشغيل القرأن الخاص بسورس حياه\nلتتمكن من استخدام اوامر القرأن اكتب \n سورة + اسم السورة بالاسفل👇\n**⩹━━⌞  𓏺᥉᥆ᥙᖇᥴᥱ ꫝꪖꪗꪖ ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᯓ𓆩𓏺᭙ɦᎥ᥉ƙᥱᥡ ˹َّّ", url=f"https://t.me/bp_bp"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞  𓏺᥉᥆ᥙᖇᥴᥱ ꫝꪖꪗꪖ ⌝⚡", url=f"https://t.me/HL_BG"),
                ],

            ]

        ),

    )



    
