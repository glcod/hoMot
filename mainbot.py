"""
Original file is located at
    https://colab.research.google.com/drive
"""

import thingspeak 
import urllib
import os
from telegram.ext import Updater,CommandHandler

api_key = os.getenv('thinkspeak_api')
lturl = "https://api.thingspeak.com/update?"+api_key+"&field1="
fnurl = "https://api.thingspeak.com/update?"+api_key+"&field2="

def lton(bot,update):
  chat_id = update.message.chat_id
  dt = lturl+"1"
  data = urllib.request.urlopen(dt)
  bot.send_message(chat_id = chat_id ,text = "Lights On")

def ltoff(bot,update):
  chat_id = update.message.chat_id
  dt = lturl+"0"
  data = urllib.request.urlopen(dt)
  bot.send_message(chat_id = chat_id ,text = "Lights Off")

def fnon(bot,update):
  chat_id = update.message.chat_id
  dt = fnurl+"1"
  data = urllib.request.urlopen(dt)
  bot.send_message(chat_id = chat_id ,text = "Fan On")

def fnoff(bot,update):
  chat_id = update.message.chat_id
  dt = fnurl+"0"
  data = urllib.request.urlopen(dt)
  bot.send_message(chat_id = chat_id ,text = "Fan Off")
    
up = os.getenv('telegrambot_api')
updater = Updater(up)

dp = updater.dispatcher
dp.add_handler(CommandHandler('lton',lton))
dp.add_handler(CommandHandler('ltoff',ltoff))
dp.add_handler(CommandHandler('fnon',fnon))
dp.add_handler(CommandHandler('fnoff',fnoff))
updater.start_polling()
updater.idle()
print('Done')
               
    
