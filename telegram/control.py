from django.conf import settings
import telebot



BOT_TOKEN = getattr(settings, "BOT_TOKEN")
ADMIN_GROUP = getattr(settings, 'ADMIN_GROUP')
bot = telebot.TeleBot(BOT_TOKEN, threaded=False)

