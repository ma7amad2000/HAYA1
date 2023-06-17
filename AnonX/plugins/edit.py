
from config import API_HASH,  API_ID,  BOT_TOKEN
import asyncio
from pyrogram import Client, filters
from AnonX import app
import random
from strings.filters import command
app = Client(
    "Bot",
    api_id = API_ID
    api_hash = API_HASH
    bot_token = BOT_TOKEN
)

iddof = []

@app.on_message(command(['تفعيل التعديل'], prefixes=""))
async def iddlock(client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in ["creator", "administrator"]:
        if message.chat.id in iddof:
            return await message.reply_text("تم تفعيل التعديل مسبقًا 🔒")
        iddof.append(message.chat.id)
        return await message.reply_text("تم تفعيل التعديل بنجاح ✅🔒")
    else:
        return await message.reply_text("يجب عليك أن تكون مشرفًا لتنفيذ هذا الأمر.")

@app.on_message(command(['تعطيل التعديل'], prefixes=""))
async def iddopen(client, message):
   get = await app.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in ["creator", "administrator"]:
      if not message.chat.id in iddof:
        return await message.reply_text("التعديل معطل من قبل ✅")
      iddof.remove(message.chat.id)
      return await message.reply_text("تم فتح تعطيل بنجاح ✅🔓")
   else:
      return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")

@app.on_message(filters.edited)
async def delete_edited_message(client, message):
    if message.chat.id in iddof:
        await client.delete_messages(chat_id=message.chat.id, message_ids=message.message_id)


