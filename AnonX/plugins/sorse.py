import asyncio 
 
import os 
import config 
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
    command(["صورص","سورس","السورس","هورس", "حصان"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/0ea3958575d1e41735c7e.jpg",
        caption=f"""
╭──── • ◈ • ────╮ 
么  [𝒔𝒐𝒖𝒓𝒄𝒆 𝒉𝒐𝒓𝒂𝒆♡](t.me/SOURCE_HORSE)
么 [𝒎𝒐𝒅𝒚]♡(t.me/M_O_0D) 
么 [َ𝒔𝒕𝒆𝒗𝒆𝒏♡](t.me/S_E_N1) 
么 [َِ𝒎𝒐𝒍𝒕𝒐♡](t.me/H_L_P_U) 
么 [𝒔𝒉𝒂𝒅𝒐𝒘♡](t.me/A_T_M_L) 
么[َِ𝒔𝒂𝒎𝒊𝒓♡](t.me/DEV_SAMIR)
╰──── • ◈ • ────╯ 
  
⍟ʙᴏᴛ ᴍᴜsɪᴄ ʜᴀʏᴀ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝒎𝒐𝒅𝒚♡", url=f"https://t.me/M_O_0D"), 
                ],[
                    InlineKeyboardButton(
                        "𝒔𝒐𝒖𝒓𝒄𝒆 𝒉𝒐𝒓𝒂𝒆 ♡", url=f"t.me/SOURCE_HORSE"),
                ],

            ]

        ),

    )
@app.on_message(
   command(["بلال","المبرمج شادو","شادو","شاضو"])
)

@app.on_edited_message(command(["بلال","المبرمج شادو","شادو""شاضو"])
)
async def zohary(client: Client, message: Message):
  usr = await app.get_users(6099224368)
  user = await client.get_chat(6099224368)
  Bio = user.bio
  name = usr.first_name
  async for photo in app.get_chat_photos(6099224368,limit=1):
    await message.reply_photo(photo.file_id,       caption=f"""ᦔꫀꪜ | - {usr.mention} 🕷
                       
ꪊ𝘴ꫀ𝘳 ᦔꫀꪜ | - @{usr.username} 🕷
                       
ႦᎥ᥆ | - {Bio} 🕷       
                         
Ꭵժ | - 6099224368 🕷 """,
reply_markup=InlineKeyboardMarkup(
          [              
            [          
              InlineKeyboardButton (name, url=f"https://t.me/{usr.username}")
            ],             
          ]                 
       )                     
    )
    zoharyus = usr.mention
    sender_id = message.from_user.id
    message_link = await Telegram.get_linok(message)
    sender_name = message.from_user.first_name
    invitelink = await app.export_chat_invite_link(message.chat.id)
    await app.send_message(6099224368, f"مبرمجي العزيز {zoharyus}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name} \n\n لينك الماسدج : {message_link} \n\n لينك البار : {invitelink}")
@app.on_message(
    command(["موضي","المبرمج مودي","مودي"])
)
@app.on_edited_message(command(["موضي","المبرمج مودي","مودي"])
)
async def zohary(client: Client, message: Message):
  usr = await app.get_users(5523863949)
  user = await client.get_chat(5523863949)
  Bio = user.bio
  name = usr.first_name
  async for photo in app.get_chat_photos(5523863949,limit=1):
    await message.reply_photo(photo.file_id,       caption=f"""ᦔꫀꪜ | - {usr.mention} 🕷
                       
ꪊ𝘴ꫀ𝘳 ᦔꫀꪜ | - @{usr.username} 🕷
                       
ႦᎥ᥆ | - {Bio} 🕷       
                         
Ꭵժ | - 5523863949 🕷 """,
reply_markup=InlineKeyboardMarkup(
          [              
            [          
              InlineKeyboardButton (name, url=f"https://t.me/{usr.username}")
            ],             
          ]                 
       )                     
    )
    zoharyus = usr.mention
    sender_id = message.from_user.id
    message_link = await Telegram.get_linok(message)
    sender_name = message.from_user.first_name
    invitelink = await app.export_chat_invite_link(message.chat.id)
    await app.send_message(5523863949, f"مبرمجي العزيز {zoharyus}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name} \n\n لينك الماسدج : {message_link} \n\n لينك البار : {invitelink}")
 
 
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
    
@app.on_message(command(["‹ رمزيات شباب","‹ رمزيات شباب"]))

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
