import asyncio


import random
from AnonX import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import filters, Client
from config import OWNER_ID



txt = [

            "؏ـيوٍڼ حـيآهہ😻🫶",


             "ﻧ؏ـ۾ 🥺❤",
            

            "هہذآ آڛـﻤــي 🫶😻",
            
            
            "ضـوꪆ حـيـاﮪ،💗🧸!َ''))",
            
            
            "نعٓم يـﺣـبـعـﻣـري،🥺🧡🌸!َ''))",
            
            
             "ﺷِﻧڻ تـبـي🙂😒",
            
            
 
            
            

        ]

txt1 = [

            "**؏ـيوٍڼ حـيآهہ😻🫶 يا مطوريي**",


             "**ﻧ؏ـم يامطوريي**",
            

            "**امرني يا مطوري الحبيب**",
            
            
           
            
            
 
            
            

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
       

