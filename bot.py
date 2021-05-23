222#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import telebot
from datetime import datetime
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import pytz
PORT = int(os.environ.get('PORT', 80))



# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '1769553533:AAG6EI51jUJHwAVvYa12iXER7jRniQF_nNM'
#j=updater.job_queue

# Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('ECEbot at your service. Use / followed by sub name')
    
def timenow(update, context):
    """Send a message when the command /timenow is issued."""
    now = datetime.now()
    tz = pytz.timezone('Asia/Kolkata')
    your_now = now.astimezone(tz)
    current_time = your_now.strftime("%H:%M:%S")
    
    update.message.reply_text(current_time)    
    
#def morning(context:CallbackConext):
 #   message="good morning"
  #  context.bot.send_message(chad_id='888117682',text=message)
    
def math(update, context):
    """Send a message when the command /math is issued."""
    update.message.reply_text('http://imgur.com/a/VQkmm2U')

def physics(update, context):
    """Send a message when the command /physics is issued."""
    update.message.reply_text('https://drive.google.com/file/d/1ym8isX2eQBvjsGln_Yt11z5V7gxKxxSR/view?usp=sharing')    
    
def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Contact Vikram!')

def login(update, context):
   
    update.message.reply_text('Let\'s log you in..')
    
    bot.sendMessage(chat_id=update.message.chat_id,
                    text='Name')
    #name = update.message.text
    bot.sendMessage(chat_id=update.message.chat_id,
                    text='Section')
    #section = update.message.text
    
    

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
  
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)
    bot = telebot.TeleBot(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("math", math))
    dp.add_handler(CommandHandler("timenow", timenow))
    dp.add_handler(CommandHandler("physics", physics))
    dp.add_handler(CommandHandler("login", login))
   # job_daily=j.run_daily(morning,days=(0,1,2,3,4,5,6),time=datetime.time(hour=14,minute=30,second=00))


    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://tele-botvik.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()

