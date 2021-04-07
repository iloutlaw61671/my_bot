#!/usr/bin/env python
# coding: utf-8

# In[17]:


import telegram
import logging
from telegram.ext import CommandHandler

from telegram.ext import Updater
updater = Updater(token='1769553533:AAG6EI51jUJHwAVvYa12iXER7jRniQF_nNM', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="ECE_bot at your service")
    
    
def math(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="http://imgur.com/a/VQkmm2U")    
    

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)    
math_handler = CommandHandler('math', math)
dispatcher.add_handler(math_handler)
updater.start_polling()

