import asyncio
import time

from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch
from strings.filters import command
import config
from config import BANNED_USERS
from config import OWNER_ID
from strings import get_command, get_string
from AnonX import Telegram, YouTube, app
from AnonX.misc import SUDOERS, _boot_
from AnonX.plugins.playlist import del_plist_msg
from AnonX.plugins.sudoers import sudoers_list
from AnonX.utils.database import (add_served_chat,
                                       add_served_user,
                                       get_served_chats,
                                       get_served_users,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from AnonX.utils.decorators.language import LanguageStart
from AnonX.utils.formatters import get_readable_time
from AnonX.utils.inline import (help_pannel, private_panel,
                                     start_pannel)




async def participant_check(channel, user_id):
    try:
        await app(GetParticipantRequest(channel, int(user_id)))
        return True
    except UserNotParticipantError:
        return False
    except:
        return False


@app.on_message(pattern="اجباري")
async def fsub(event):
    if event.is_private:
        return
    if event.is_group:
        perm = await event.client.get_permissions(event.chat_id, event.sender_id)
        if not perm.is_admin:
            return await event.reply(
                "أنت لست مشرف في هذه المجموعة يجب ان تكون مشرف اولا"
            )
    try:
        channel = event.text.split(None, 1)[1]
    except IndexError:
        channel = None
    if not channel:
        return await edit_delete(event, "-يجب عليك وضع معرف القناة اولا")
    if not str(channel).startswith("@"):
        channel = "@" + str(channel)
    else:
        try:
            channel_entity = await event.client.get_entity(channel)
        except:
            return await event.reply(
                "<b> عليك وضع المعرف بشكل صحيح ❗️</b>", parse_mode="html"
            )
        channel = channel_entity.username
        try:
            if not channel_entity.broadcast:
                return await event.reply("هذه القناة غير صالحة .")
        except:
            return await event.reply("يجب وضع المعرف بشكل صحيح.")
        if not await participant_check(channel, app.uid):
            return await event.reply(
                f"❗️أنا لست ادمن في هذه القناة\n [القناة](https://t.me/{channel}). يجب ان اكون مشرف في القناة اولا.",
                link_preview=False,
            )
        add_fsub(event.chat_id, str(channel))
        await event.reply(
            f"- تم بنجاح تفعيل الاشتراك الاجباري   للقناة @{channel}. ✅"
        )


@app.on_message(pattern="تعطيل الاجباري")
async def removefsub(event):
    rm_fsub(event.chat_id)
    await edit_or_reply(event, "- تم بنجاح تعطيل الاشتراك الاجباري في هذه المجموعة")


@app.on(events.NewMessage())
async def fsub_n(e):
    if all_fsub() == None:
        return
    if not is_fsub(e.chat_id):
        return
    if e.is_private:
        return
    if e.chat.admin_rights:
        if not e.chat.admin_rights.ban_users:
            return
    else:
        return
    if not e.from_id:
        return
    chatdb = is_fsub(e.chat_id)
    channel = chatdb.channel
    try:
        check = await participant_check(channel, e.sender_id)
    except ChatAdminRequiredError:
        return
    if not check:
        txt = f'اهلا بك عزيزي المستخدم <a href="tg://user?id={e.sender_id}">{e.sender.first_name}</a>\nيجب عليك الاشتراك في قناة المجموعة\nللتحدث بحرية ولأزالة الكتم - <a href="t.me/{channel}">اضغط هنا</a>'
        await e.reply(txt, parse_mode="html", link_preview=False)
        await e.delete()
