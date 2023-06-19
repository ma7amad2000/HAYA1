
import asyncio
import requests
from pyrogram import Client
from pyrogram import filters
import random
from AnonX import app
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import USER_CHANNEL,  BOT_TOKEN

from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant





       
@app.on_message(
    command(["/start"])
    & ~filters.edited
)
async def start(client: Client, message: Message):
       m = message.chat.id
       user = message.from_user.mention
       do = requests.get(f"https://api.telegram.org/app{BOT_TOKEN}/getChatMember?chat_id=@{CHANNEL}&user_id={message.from_user.id}").text
       if do.count("left") or do.count("Bad Request: user not found"):
          await message.reply_text(f"**Join [this channel](t.me/{USER_CHANNEL}) first to be able to use the app ✨**", disable_web_page_preview=True,
          reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                        "انظم الى القناه",
                        url=f'https://t.me/{CHANNEL}'),
                        ],
                    ]
                )
            ) 
       else:
         await app.send_message(m, f"**Hello my friend ( {user} ) **",
       reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                        "𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝞝𝙔.",
                        url=f'https://t.me/BP_BP'),
                        ],[
                            InlineKeyboardButton(
                        "𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼",
                        url=f'https://t.me/hl_bg'),
                        ],
                    ]
                )
            ) 
            
            
            
            
     
