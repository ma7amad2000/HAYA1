import asyncio

import os
import time
import requests
from config import USER_OWNER, OWNER_ID
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
                
        ],[
                    
                
                    InlineKeyboardButton(
                        "『𓏺َِ᥉َِꫝُِᎥُِƙَِꪖُِᧁَِ᥆_ŘB 』", url=f"https://t.me/T_N_T_RB"),
                ],

            ]

        ),

    )









@app.on_message(
    command(["شيكاغو تعال","عبادي","شيكاغو"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    
    usr = await client.get_chat("T_N_T_RB")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⌞𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼\nمعلومات مطور السورس2 \n↜︙Dev 𝗡𝗔𝗠𝗘 ↬:{name}\n↜︙Dev 𝐔𝐒𝐄𝐑 ↬ :@{usr.username}\n↜︙Dev 𝐈𝐃 ↬ :`{usr.id}`\n↜︙Dev 𝐁𝐈𝐎 ↬: {usr.bio} \n\n **𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼**", 
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
    command(["مبرمج السورس","مطور السورس"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("BP_BP")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⌞𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼\nمعلومات مبرمج السورس \n↜︙Dev Name ↬ :{name} \n↜︙Dev User ↬ :@{usr.username} \n↜︙Dev id ↬ :{usr.id}**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],  [
                    InlineKeyboardButton(
                        "استدعاء المبرمج", url=f"https://t.me/{usr.username}"),                        
                 ],
            ]
        ),
    )


@app.on_message(
    command(["المطور"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat(USER_OWNER)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⌞𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 \nمعلومات المطور الاساسي\n↜︙Dev Name ↬ :{name} \n↜︙Dev User ↬ :@{usr.username} \n↜︙Dev id ↬ :{usr.id}**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],   [
                    InlineKeyboardButton(
                        "استدعاء المطور", url=f"https://t.me/{usr.username}"),                        
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



    
