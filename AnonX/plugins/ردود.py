import asyncio


import random
from AnonX import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import filters, Client
import config



txt = [

            "دوٌمُ ٱڷضٍـحڪهْهْ ♥️😻",


             "ضٍـحڪڹٱ مُعُٱٱڪ🙄🙄",
            

            "ضٍـحڪڹٱ مُعُٱٱڪ🙄🙄",
            
            
            "۾ـآ ڣي ڜي يڞحـڪ يبـآڕد 😒😒",
            
            
            "ࢪبـي يـدوٍ۾ آلڞـحـڪـهہ يآﭰلبـي🥺🔥",
            
            
             "ضحكه بدون نيهه🙂😒",
            
            
 
            
            

        ]


        


@app.on_message(command(["ههه","😂😂","😂😂😂😂😂","😂🤣","ههههههههههههههههههه","😂😂😂😂😂😂"]))


async def cutt(client: Client, message: Message):


      a = random.choice(txt)


      await message.reply(


        f"{a}")
