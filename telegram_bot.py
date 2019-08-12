from telegram import ParseMode, Bot
from telegram.error import TelegramError
from telegram.ext.dispatcher import run_async
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler, BaseFilter

api_token = "INPUT YOUR TOKEN"

class FilterAwesome(BaseFilter):
    def __init__(self):
        self.groups = ['group1', 'chat2']
    def filter(self, message):
        if message.chat.username in self.groups:
        	new_members = message.new_chat_members
        	left_member = message.left_chat_member
            if new_members or left_member:
            	return True
        return False

def delete_message_safe(bot, msg):
    chat_id = msg._effective_message.chat.id
    message_id = msg._effective_message.message_id

    bot.delete_message(chat_id, message_id)

updater = Updater(token=api_token)
dispatcher = updater.dispatcher
filter_awesome = FilterAwesome()

echo_handler = MessageHandler(filter_awesome, delete_message_safe)
dispatcher.add_handler(echo_handler)
updater.start_polling()
