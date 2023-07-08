import telebot
from decouple import config

BOT_TOKEN = config("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])

def wel(message):
    bot.send_message(message.chat.id,"البوت تحت التطوير")
bot.polling()    