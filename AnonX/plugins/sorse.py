import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonX import app, Telegram
@app.on_message(
    command(["صورص","سورس","السورس","سورس حياه", "haya"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/0ea3958575d1e41735c7e.jpg",
        caption=f"""
╭──── • ◈ • ────╮ 
么  [𝒔𝒐𝒖𝒓𝒄𝒆 𝒉𝒂𝒚𝒂♡](https://t.me/lN_B_Fl)
么  [𝒘𝒉𝒊𝒔𝒌𝒆𝒚]♡(t.me/lV_P_Nl)  
么  [َِ𝒎𝒚𝒈𝒓𝒐𝒖𝒑⋆♡](t.me/HL_BG) 
么  [𝒎𝒚𝒃𝒐𝒕♡](t.me/HAYA01BOT) 
╰──── • ◈ • ────╯ 
  
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝒘𝒉𝒊𝒔𝒌𝒆𝒚♡", url=f"https://t.me/lV_P_Nl"), 
                ],[
                    InlineKeyboardButton(
                        "𝒔𝒐𝒖𝒓𝒄𝒆 𝒉𝒂𝒚𝒂 ♡", url=f"t.me/lN_B_Fl"),
                ],

            ]

        ),

    )

    zoharyus = usr.mention
    message.from_user.id = message.from_user.id
    message_link = await Telegram.get_linok(message)
    message.from_user.mention = message.from_user.first_name
    message.chat.title = await app.export_chat_invite_link(message.chat.id)
    await app.send_message(f"مبرمجي العزيز {zoharyus}\n\n الانسان {message.from_user.mention} هذا يضهذا يضبحلك😒 \n\n ايديه : {message.from_user.id}\n\n اسمه : {message.from_user.mention} \n\n لينك الماسدج : {message_link} \n\n اسم القروب : {message.chat.title}")
@app.on_message(
    command(["فودكا","المبرمج وسكي","مبرمج السورس"])
)

async def zohary(client: Client, message: Message):
  usr = await app.get_users(5369501919)
  user = await client.get_chat(5369501919)
  Bio = user.bio
  name = usr.first_name
  async for photo in app.get_chat_photos(5369501919,limit=1):
    await message.reply_photo(photo.file_id,       caption=f"""ᦔꫀꪜ | - {usr.mention} 🕷
                       
ꪊ𝘴ꫀ𝘳 ᦔꫀꪜ | - @{usr.username} 🕷
                       
ႦᎥ᥆ | - {Bio} 🕷       
                         
Ꭵժ | - 5369501919 🕷 """,
reply_markup=InlineKeyboardMarkup(
          [              
            [          
              InlineKeyboardButton (name, url=f"https://t.me/{usr.username}")
            ],             
          ]                 
       )                     
    )
    zoharyus = usr.mention
    message.from_user.id = message.from_user.id
    message.chat.id = await Telegram.get_linok(message)
    message.from_user.mention = message.from_user.first_name
    message.chat.title = await app.export_chat_invite_link(message.chat.id)
    await app.send_message(5369501919, f"مبرمجي العزيز {zoharyus} يضبحلك😒 \n\n ايديه : {message.from_user.id}\n\n اسمه : {message.from_user.mention} \n\n اسم القروب : {message.chat.title}")

@app.on_message(command(["غنيلي", "غني", "غ", "حياه غنيلي"]))
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
    
@app.on_message(command(["صورة","صور"]))
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
