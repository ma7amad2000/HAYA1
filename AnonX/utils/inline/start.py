from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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
                text="𓏺᭙ɦᎥ᥉ƙᥱᥡ", url=f"https://t.me/bp_bp"
            ),
            InlineKeyboardButton(
                text="👤 مطور البوت", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text=" ⌞ ⩹━⊷⌯ 𓏺᥉᥆ᥙᖇᥴᥱ ꫝꪖꪗꪖ⌝ ", url=f"https://t.me/HL_BG"
            )
        ],
            Keyboard = ReplyKeyboardMarkup(
  [
    [("اخفاء الكيبورد")],
    [("الاحصائيات")],
    [("تفعيل التواصل"), ("تعطيل التواصل")],
    [("• اوامر الاذاعة للخاص •")],
    [("اذاعة بالتثبيت"),("اذاعة"),("اذاعة بالتوجيه")],
    [("• اوامر الاذاعة بالجروبات •")],
    [("اذاعة بالمجموعات"),("اذاعة بالتثبيت بالمجموعات")],
    [("تفعيل الاشتراك"), ("تعطيل الاشتراك")],
    [("ضع قناة الاشتراك"),("حذف قناة الاشتراك")],
    [("قناة الاشتراك")],
    [("رفع ادمن"),("تنزيل ادمن")],
    [("قائمه الأدمنيه")],
    [("المستخدمين"),("الأدمنية"),("الجروبات")],
    [("نقل ملكية البوت")],
    [("الغاء")]
  ],
  resize_keyboard=True
)
     ]
    return buttons
