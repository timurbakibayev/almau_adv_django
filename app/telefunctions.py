import telebot
from django.contrib.auth.models import User

from app.tele_token import token
from app.models import Teleuser
bot = telebot.TeleBot(token)


def send_message(user: User, text: str) -> None:
    tele_users = Teleuser.objects.filter(user=user)
    for tu in tele_users:
        try:
            bot.send_message(tu.chat_id, text)
        except Exception as e:
            if "Forbidden" in str(e):
                Teleuser.objects.filter(chat_id=tu.chat_id).delete()
                print("user left the bot")
