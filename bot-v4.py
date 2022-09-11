#!/bin/python

#pip install python-telegram-bot

from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import time

updater = Updater("000000:xxxxxxxxxxxxxxxxxxxxxxxxx", use_context=True)
  
  
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello sir, Welcome to the Bot.Please write\
        /help to see the commands available.")
  
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /PDF - get pdf""")

#=========================================================
def PDF(update: Update, context: CallbackContext):
    update.message.reply_text("Wait.")
    time.sleep(0.2)
    update.message.reply_text("Wait..")
    time.sleep(0.2)
    update.message.reply_text("Wait...")
    file="file.pdf"
    context.bot.sendDocument(update.effective_chat.id, document=open(file, 'rb'))
#=========================================================


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command"  % update.message.text)
  
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
  
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('PDF', PDF))

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))     # Filters out unknown text
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))  # Filters out unknown commands
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
  
updater.start_polling()