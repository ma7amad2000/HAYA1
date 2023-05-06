from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client
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

channel1_id = "https://t.me/lN_B_Fl"
channel2_id = "https://t.me/HL_BG"

with app:
    is_subscribed_to_channel1 = app.get_chat_member(channel1_id, 'اشترك').status != 'kicked'
    is_subscribed_to_channel2 = app.get_chat_member(channel2_id, 'ااشنرك').status != 'kicked'
