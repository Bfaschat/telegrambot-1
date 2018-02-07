# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 11:50:33 2018

@author: mayan
github: https://github.com/mjthedevil
"""

import os
import sys
import time
import telepot
from telepot.loop import MessageLoop
from PyDictionary import PyDictionary
os.chdir('C:/Users/mayan/Desktop/telegrambot')
from dictionary_dot_com import requester, definition, example_sentences, getWord, pronounciation
#from dictionary_dot_com import synonym_forms, brit_definition, brit_origin_data, origin_data, related_forms
dictionary=PyDictionary()


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if content_type == 'text':       
        print(msg['from']['first_name']+' '+msg['text'])
        split_=msg['text'].split(' ')
        if  len(split_)>2:
            return
        if len(split_)>1 and split_[0] == 'word':
            if split_[1] == 'today' or len(split_[1])!= 10:
                word_day=getWord(True,True)
            else:
                try:word_day=getWord(True,True,split_[1])
                except:word_day=getWord(True,True)               
            bot.sendMessage(chat_id,word_day)
            return
                    
        definition_1 = dictionary.meaning(msg['text'])
        block = requester(msg['text'])
        example = example_sentences(block)
        definition_2 = definition(block)
        pydi=''
        try :
            for d in definition_1:
                list_cushion=''
                for fos in definition_1[d]:
                    list_cushion = list_cushion + fos + ',\n'            
                pydi = pydi + d + ': '+ list_cushion +'\n'
        except:pass
        translation = dictionary.translate(msg['text'],'hi')
        
        if translation:
            pydi = pydi + 'In Hindi: ' + translation
    
        bot.sendMessage(chat_id,pydi)    
        bot.sendMessage(chat_id,definition_2)        
        bot.sendMessage(chat_id,example)
        pronunciation,file_name = pronounciation(block)
        bot.sendMessage(chat_id,pronunciation)
        bot.sendAudio(chat_id, open(file_name,'rb'), title=msg['text'])

TOKEN = '<Enter token from telegram here>'

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(2)
    
