from control import bot
from telebot import types


@bot.message_handler(commands=['start'])
def send_welcome(msg: types.Message):
    bot.reply_to(msg, "Hello how are you doing!")