#!/bin/python

#pip install python-telegram-bot

from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
  
updater = Updater("API",
                  use_context=True)
  
  
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello sir, Welcome to the Bot.Please write\
        /help to see the commands available.")
  
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /youtube - To get the youtube URL
    /twitter - To get the twitter profile URL
    /gmail - To get gmail URL
    /developer - To see developer's github""")
  
  
def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Your gmail link here (I am not\
        giving mine one for security reasons)")
  
  
def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("Youtube Link =>\
    https://www.youtube.com/channel/UCPH8W_HGyJaJuuZaMy1JDzg")
  
  
def twitter_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "twitter URL => \
        https://www.twitter.com/cirklare/")
  
  
def developer(update: Update, context: CallbackContext):
    update.message.reply_text(
        "developer URL => https://github.com/CIRKLARE/")
  
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
  
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
  
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('twitter', twitter_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('developer', developer))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))     # Filters out unknown text
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))  # Filters out unknown commands
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
  
updater.start_polling()