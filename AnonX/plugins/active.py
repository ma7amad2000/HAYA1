from pyrogram import filters
from pyrogram.types import Message

from strings import get_command
from AnonX import app
from AnonX.misc import SUDOERS
from AnonX.utils.database.memorydatabase import (
    get_active_chats, get_active_video_chats)
from strings.filters import command
# Commands
ACTIVEVC_COMMAND = get_command("ACTIVEVC_COMMAND")
ACTIVEVIDEO_COMMAND = get_command("ACTIVEVIDEO_COMMAND")


@app.on_message(
    command(ACTIVEVC_COMMAND)
    & SUDOERS
)
async def activevc(_, message: Message):
    mystic = await message.reply_text(
        "الحصول على قائمة محادثات صوتية نشطة ..."
    )
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "محادثه خاصه"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("**لا توجد محادثه صوتيه نشطه**")
    else:
        await mystic.edit_text(
            f"**المحادثات الصوتيه النشطه في البوت :-**\n\n{text}",
            disable_web_page_preview=True,
        )
#حقوق سورس حيا
#ركز وانت تعدل ياللي تسرق واذكر الحقوق خير ماتنهان وتنسب


@app.on_message(
    command(ACTIVEVIDEO_COMMAND)
    & SUDOERS
)
async def activevi_(_, message: Message):
    mystic = await message.reply_text(
        "المحادثه الصوتيه نشطه حاليا..."
    )
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "محادثه خاصه"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("لا توجد محادثه نشطه في البوت...")
    else:
        await mystic.edit_text(
            f"**المحادثات النشطه في البوت :-**\n\n{text}",
            disable_web_page_preview=True,
        )
#حقوق سورس حيا
#ركز وانت تعدل ياللي تسرق واذكر الحقوق خير ماتنهان وتنسب
