from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import *
import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🗒 الاوامر",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="المساعدة", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons
     

def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🗒 الاوامر", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="✨️ 『𝐂𝐑𝐘𝐒𝐓𝐀𝐋 ⏎ 』 ✨️]ِ", url=f"https://t.me/ssxhh"
            ),
            InlineKeyboardButton(
                text="👤 مطور البوت", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text=" ⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 🦋𝐂𝐑𝐘𝐒𝐓𝐀𝐋  ⌝ ", url=f"https://t.me/no1bros"
            )
        ],
     ]
    return buttons

@bot.message_handler(commands=["start"])
def start(message):
                ch = "قناتك بدون @"
                idu = message.chat.id
                join = requests.get(f"https://api.telegram.org/bot{token}/getChatMember?chat_id=@{ch}&user_id={idu}").text
                if '"status":"left"' in join:
                    bot.send_message(message.chat.id,f"""
🚸| عذرا عزيزي
🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه
{ch} 

‼️| اشترك ثم ارسل /start
                    """)
                else:
                 bot.send_photo(message.chat.id,url, """• 𝚆𝙴𝙻𝙲𝙾𝙼𝙴  •''''''')
