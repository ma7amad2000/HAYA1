######تطوير الوسكي الليبي########

#حقوق سورس حيا
#ركز وانت تعدل ياللي تسرق واذكر الحقوق خير ماتنهان وتنسب








from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, adminlist
from strings import get_command
from AnonX import app
from AnonX.utils.database import (delete_authuser, get_authuser,
                                       get_authuser_names,
                                       save_authuser)
from AnonX.utils.decorators import AdminActual
from AnonX.utils.formatters import int_to_alpha
from strings.filters import command
# Command
AUTH_COMMAND = get_command("AUTH_COMMAND")
UNAUTH_COMMAND = get_command("UNAUTH_COMMAND")
AUTHUSERS_COMMAND = get_command("AUTHUSERS_COMMAND")


@app.on_message(
    command(AUTH_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@AdminActual
async def auth(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("**»قم بالرد على المستخدم للحصول على معلوماته**")
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        user_id = message.from_user.id
        token = await int_to_alpha(user.id)
        from_user_name = message.from_user.first_name
        from_user_id = message.from_user.id
        _check = await get_authuser_names(message.chat.id)
        count = len(_check)
        if int(count) == 20:
            return await message.reply_text("**» لا يمكنك رفع اكثر من 20 ادمن في قروبك**")
        if token not in _check:
            assis = {
                "auth_user_id": user.id,
                "auth_name": user.first_name,
                "admin_id": from_user_id,
                "admin_name": from_user_name,
            }
            get = adminlist.get(message.chat.id)
            if get:
                if user.id not in get:
                    get.append(user.id)
            await save_authuser(message.chat.id, token, assis)
            await message.reply_text("عملية رفع")
            return await message.reply_text("**»تم ترقيته ادمن.**")
        else:
            await message.reply_text("**»هوا ادمن بالفعل.**")
        return
    from_user_id = message.from_user.id
    user_id = message.reply_to_message.from_user.id
    user_name = message.reply_to_message.from_user.first_name
    token = await int_to_alpha(user_id)
    from_user_name = message.from_user.first_name
    _check = await get_authuser_names(message.chat.id)
    count = 0
    for smex in _check:
        count += 1
    if int(count) == 20:
        return await message.reply_text("**»لا يمكنك رفع اكثر من 20 ادمن في قروبك**")
    if token not in _check:
        assis = {
            "auth_user_id": user_id,
            "auth_name": user_name,
            "admin_id": from_user_id,
            "admin_name": from_user_name,
        }
        get = adminlist.get(message.chat.id)
        if get:
            if user_id not in get:
                get.append(user_id)
        await save_authuser(message.chat.id, token, assis)
        await message.reply_text("عملية رفع")
        return await message.reply_text("**»تم ترقيته ادمن**")
    else:
        await message.reply_text("**»هوا ادمن بالفعل**")


@app.on_message(
    command(UNAUTH_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
#حقوق سورس حيا
#ركز وانت تعدل ياللي تسرق واذكر الحقوق خير ماتنهان وتنسب

@AdminActual
async def unauthusers(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("**»قم بالرد على المستخدم للحصول على معلوماته**")
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        token = await int_to_alpha(user.id)
        deleted = await delete_authuser(message.chat.id, token)
        get = adminlist.get(message.chat.id)
        if get:
            if user.id in get:
                get.remove(user.id)
        if deleted:
            await message.reply_text("تم ازالته")
            return await message.reply_text("**» تم تنزيله من قائمه الادمن**")
        else:
            return await message.reply_text("**» المستخدم ليس ادمن في البوت**")
    user_id = message.reply_to_message.from_user.id
    token = await int_to_alpha(user_id)
    deleted = await delete_authuser(message.chat.id, token)
    get = adminlist.get(message.chat.id)
    if get:
        if user_id in get:
            get.remove(user_id)
    if deleted:
        await message.reply_text("تم ازالته")
        return await message.reply_text("**» تم تنزيله من قائمه الادمن**")
    else:
        return await message.reply_text("**»المستخدم ليس ادمن في البوت**")


@app.on_message(
    command(AUTHUSERS_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
async def authusers(client, message: Message, _):
    _playlist = await get_authuser_names(message.chat.id)
    if not _playlist:
        return await message.reply_text(_["setting_5"])
    else:
        j = 0
        mystic = await message.reply_text(_["auth_6"])
        text = _["auth_7"]
        for note in _playlist:
            _note = await get_authuser(message.chat.id, note)
            user_id = _note["auth_user_id"]
            admin_id = _note["admin_id"]
            admin_name = _note["admin_name"]
            try:
                user = await app.get_users(user_id)
                user = user.first_name
                j += 1
            except Exception:
                continue
            text += f"{j}➤ {user}[`{user_id}`]\n"
            text += f"   {_['auth_8']} {admin_name}[`{admin_id}`]\n\n"
        await mystic.delete()
        await message.reply_text(text)
#حقوق سورس حيا
#ركز وانت تعدل ياللي تسرق واذكر الحقوق خير ماتنهان وتنسب
