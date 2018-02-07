# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 11:03:30 2018

@author: mayan
github: https://github.com/mjthedevil
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
def requester(search_tearm):    
#    search_tearm='dream'
    url = "http://www.dictionary.com/browse/{}?s=t".format(search_tearm)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"lxml")
    central_block = soup.find('div',{'class':'center-well-container'})
    return central_block

def definition(block):
    source_luna = block.find('section',{'id':'source-luna'})
    source_data = source_luna.find('div',{'class':'source-data'})
    def_list = source_data.find('div',{'class':'def-list'})
    
    block1 = def_list.findAll('section',{'class':'def-pbk ce-spot'})
    whole_def=''
    for blk1 in block1:
        header = blk1.header.text.strip() + '\n'
        defs = blk1.findAll('div',{'class':'def-set'})
        def_print = ''
        for def_part in defs:
            no_ = def_part.find('span',{'class':'def-number'}).text.strip()
            def_ = def_part.find('div',{'class':'def-content'}).text.strip().replace('\n\r\n','\n').replace('  ','')
#            print(no_)
#            print(def_)
    #        print(no_ + ' ' + def_)
            try:
                exmpl = def_part.find('div',{'class':'def-block def-inline-example'}).text.strip()
                def_print =def_print + no_ + ' ' + def_.split('                 ')[0] + ' ' + exmpl + '\n'
            except:
                def_print =def_print + (no_ + ' ' + def_) + '\n'
        whole_def = whole_def + header  + def_print + '\n'
    return whole_def.strip()


def origin_data(block):
    source_luna = block.find('section',{'id':'source-luna'})
    header = source_luna.find('div',{'id':'source-word-origin'}).text.replace('Expand','').strip()
    origin_source = source_luna.find('div',{'class':'tail-box tail-type-origin pm-btn-spot'})
    origin =header + '\n' + origin_source.find('div',{'class':'tail-elements'}).text.strip().replace('\n\n\n','\n').replace('\n\n','\n').replace('\n\n','\n')
    return origin.strip()

def related_forms(block):
    try:
        source_luna = block.find('section',{'id':'source-luna'})
        forms_source = source_luna.find('div',{'class':'tail-box tail-type-relf pm-btn-spot'})
        header = forms_source.find('div',{'class':'tail-header'}).text.replace('Expand','').strip()
        forms = header + ':' + forms_source.find('div',{'class':'tail-content ce-spot'}).text.replace('\n\n','\n')
        return forms.strip() 
    except:print('No related_forms')
    return ''
    
def synonym_forms(block):
    try:
        source_luna = block.find('section',{'id':'source-luna'})
        synonym_source = source_luna.find('div',{'class':'tail-box tail-type-synstudy pm-btn-spot'})
        header = synonym_source.find('div',{'class':'tail-header'}).text.replace('Expand','').strip()
        synonym = header + ':' + synonym_source.find('div',{'class':'tail-content ce-spot'}).text.replace('\n\n','\n')
        return synonym.strip()
    except:print('No synonym_forms')
    return ''

def example_sentences(block):
    try:
        source_sentences = block.find('section',{'id':'source-example-sentences'})
        header = source_sentences.find('div',{'class':'source-title'}).text.replace('Expand','').strip() + ':\n'
        example_block = source_sentences.find('div',{'class':'sent-wrap ce-spot'})
        example_list = example_block.findAll('p',{'class':'partner-example-text'})
        sentences = ''
        sr_no = 0
        for exmpl in example_list:
            sr_no +=1
            sentences = sentences + str(sr_no) + '. ' + exmpl.text.strip() + '\n'
        example = header + sentences
        return example.strip()
    except:print('No example_sentences')
    return ''
    
def brit_definition(block):
    source_definition = block.find('section',{'id':'source-ced2'})
    header = source_definition.find('div',{'class':'source-title'}).text.replace('Expand','').strip()
#    print(source_definition.find('div',{'class':'source-data ce-spot'}).text)
    def_list = source_definition.find('div',{'class':'def-list'})
    
    block1 = def_list.findAll('div',{'class':'def-pbk'})
    whole_def=''
    for blk1 in block1:
        header = blk1.span.text.strip() + '\n'
        defs = blk1.findAll('div',{'class':'def-set'})
        def_print = ''
        for def_part in defs:
            no_ = def_part.find('span',{'class':'def-number'}).text.strip()
            def_ = def_part.find('div',{'class':'def-content'}).text.strip()
    #        print(no_ + ' ' + def_)
            try:
                exmpl = def_part.find('div',{'class':'def-block def-inline-example'}).text.strip()
                def_print =def_print + no_ + ' ' + def_.split('                 ')[0] + ' ' + exmpl + '\n'
            except:
                def_print =def_print + (no_ + ' ' + def_) + '\n'
        whole_def = whole_def + header  + def_print + '\n'    
    return whole_def.strip()

def brit_origin_data(block):
    source_etymon2 = block.find('section',{'id':'source-etymon2'})
    header = source_etymon2.find('div',{'class':'source-title'}).text.replace('Expand','').strip()
    source_box = source_etymon2.findAll('div',{'class':'source-box'})
    origin_source = ''
    for srb in source_box:
        def_list = srb.find('div',{'class':'def-list'}).text.strip() + '\n'
        origin_source = origin_source + def_list
    origin =header + '\n' + origin_source
    return origin.strip()


def getWord(origin = False, citation = False, date='/'.join(str(datetime.now().date()).split('-'))):
#    date='2017/01/05'
    plain_text = requests.get('http://dictionary.reference.com/wordoftheday/{}'.format(date)).text
    soup = BeautifulSoup(plain_text,"lxml")
    wordDay = 'Word: ' + soup.find("div", {"class": "definition-header"}).text.split()[2]
    try:
        definition ='\n\nDefinition: ' + soup.find("ol", {"class": "definition-list definition-wide-desktop-third definition-desktop-third definition-tablet-third"}).text.strip()
    except:
        definition ='\n\nDefinition: ' + soup.find("ol", {"class": "definition-list definition-wide-desktop-third definition-desktop-third definition-tablet-first"}).text.strip()
    header = soup.find("div", {"class": "citation-header"}).text.strip()
    if citation== True:
        header = soup.find("div", {"class": "citation-header"}).text.strip()
        citation_1 =':\n'+ soup.find("div", {"class": "citation-context"}).span.text.strip()
        citation_2 ='\n\n' + header +citation_1 +'\n'+ soup.find("blockquote", {"class": "citation-bottom-block"}).span.text.strip()
#        print(citation_2)
    else:
        citation_2=''   
    return wordDay + definition + citation_2

def get_pronunciation(def_head,_PRONUNCIATION_CLASS):
    try:
        pronunciation = def_head.find(class_=_PRONUNCIATION_CLASS) \
                                .get_text().strip()
    except:
        return None
    return pronunciation


def get_pronunciation_url(block,_PRONUNCIATION_AUDIO_TYPE_CLASS):
    try:
        p_url = block.find('source',{'type':_PRONUNCIATION_AUDIO_TYPE_CLASS}).get('src')
    except:
        return None
    return p_url


def save_to_mp3(url,word):   
    """
    Saves mp3 pronunciation sound file.
    Keyword Arguments:
    file_name -- name of the file, must include .mp3 suffix (default self.word + '.mp3')
    """
    file_name = word + '.mp3'
    try:
        with open(file_name, 'wb') as mp3_file:
            file_url = url
            mp3_file.write(requests.get(file_url).content)
            print("writing to: {0}".format(file_name))
            return file_name
    except (FileNotFoundError, PermissionError) as e:
        print("Failed to save mp3 file: {error}".format(error=e))

def pronounciation(block):
    _MAIN_CONTAINER_CLASS = 'source-box'
    _PRONUNCIATION_CLASS = 'spellpron'
    _PRONUNCIATION_AUDIO_TYPE_CLASS = 'audio/mpeg' 
    _WORD_CLASS = 'head-entry'
    main = block.find(class_=_MAIN_CONTAINER_CLASS)
    word = block.find(class_=_WORD_CLASS).text.strip()
    pronunciation = get_pronunciation(main,_PRONUNCIATION_CLASS)
    pronunciation_url = get_pronunciation_url(main,_PRONUNCIATION_AUDIO_TYPE_CLASS)
    print(pronunciation)
#    print(pronunciation_url)
    file_name = save_to_mp3(pronunciation_url,word)
    return pronunciation,file_name
    

#block= requester('Otorhinolaryngologist')
#pronunciation,file_name = pronounciation(block)



#print(definition(block))
#print(origin_data(block))
#print(related_forms(block))
#print(synonym_forms(block))
#print(example_sentences(block))
#print(brit_definition(block))
#print(brit_origin_data(block))
#print(getWord())
#remaining idioms and phrases
#    source-ahsmd
#    source-das
#    source-ahdi2
#    