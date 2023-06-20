import asyncio


import random
from AnonX import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import Client
from config import OWNER_ID
from pyrogram import filters

txt = [

            "؏ـيوٍڼ حـيآهہ😻🫶",


             "ﻧ؏ـ۾ 🥺❤",
            

            "هہذآ آڛـﻤــي 🫶😻",
            
            
            "ضـوꪆ حـيـاﮪ،💗🧸!َ''))",
            
            
            "نعٓم يـﺣـبـعـﻣـري،🥺🧡🌸!َ''))",
            
            
             "ﺷِﻧڻ تـبـي🙂😒",
            
            
 
            
            

        ]


        


@app.on_message(command(["حياه"]))


async def cutt(client: Client, message: Message):
     dev = (OWNER_ID)
     if message.from_user.id in dev:


         b = random.choice(txt1)


         await message.reply(


         f"{b}")
     else:
         a = random.choice(txt)


         await message.reply(


         f"{a}")
       
      txt1 = [

            f"**؏ـيوٍڼ حـيآهہ😻🫶 يا مطوريي {message.from_user.mention}**",


             f"**ﻧ؏ـم يامطوريي{message.from_user.mention}**",
            

            f"**امرني يا مطوري الحبيب{message.from_user.mention}**",
            
            
           
            
            
 
            
            

        ]


        
