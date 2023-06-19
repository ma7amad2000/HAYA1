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
     if message.from_user.id == OWNER_ID:


         a = random.choice(txt1)


         await message.reply(


         f"{a}")
     else:
         a = random.choice(txt)


         await message.reply(


         f"{a}")
       

