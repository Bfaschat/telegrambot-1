# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 15:05:45 2018

@author: mayan
"""

import sys
import time
import telepot
from telepot.loop import MessageLoop
import os
os.chdir('C:/Users/mayan/Desktop/telegrambot')
from dictionary import requester, definition, origin_data, related_forms
from dictionary import synonym_forms, example_sentences, brit_definition, brit_origin_data

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    print(msg)
    block = requester(msg['text'])

    query_data = definition(block) + '\n' +  origin_data(block)+ '\n' +  example_sentences(block)+ '\n' +  related_forms(block)+ '\n' +  synonym_forms(block)
    if content_type == 'text':
        bot.sendMessage(chat_id,query_data )

TOKEN = '<Enter token from telegram here>'

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(2)
    
