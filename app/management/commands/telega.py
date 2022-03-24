from typing import Dict

from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from telebot.types import Message

from app.models import Teleuser
from app.tele_handler import handle_message
import telebot
from app.tele_token import token

bot = telebot.TeleBot(token)

context: Dict[int, str] = dict()
inputs: Dict[int, Dict[str, str]] = dict()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello, my friend")


@bot.message_handler(func=lambda message: True)
def echo_all(message: Message):
    global context, inputs
    chat_id = message.chat.id
    try:
        user = Teleuser.objects.get(chat_id=chat_id).user
    except ObjectDoesNotExist:
        user = None
    if chat_id not in context:
        context[chat_id] = ""
    if message.text.lower() == "/register":
        context[chat_id] = "username"
        inputs[chat_id] = dict()
        bot.send_message(chat_id, "Please enter your username")
        return
    if context[chat_id] == "" and user is None:
        bot.send_message(chat_id, "Please register by entering '/register'")
        return
    if context[chat_id] == "username":
        inputs[chat_id]["username"] = message.text
        bot.reply_to(message, "That was your username")
        bot.send_message(message.chat.id, "Now enter your password")
        context[chat_id] = "password"
    elif context[chat_id] == "password":
        inputs[chat_id]["password"] = message.text
        bot.reply_to(message, "That was your password")
        user = authenticate(
            username=inputs[chat_id]["username"],
            password=inputs[chat_id]["password"],
        )
        if user is not None:
            Teleuser.objects.filter(chat_id=chat_id).delete()
            Teleuser.objects.create(
                user=user,
                chat_id=chat_id,
            )
            bot.send_message(message.chat.id, f"You are now registered, {user.username}")
            context[chat_id] = ""
        else:
            bot.send_message(message.chat.id, f"Incorrect username or password")
            context[chat_id] = ""
    if user is None:
        return
    handle_message(user, message.text)


class Command(BaseCommand):
    help = 'Telegram bot listener'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting Telegram bot.."))
        bot.infinity_polling()
        self.stdout.write(self.style.SUCCESS("End"))
