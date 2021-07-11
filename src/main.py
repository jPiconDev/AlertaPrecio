#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

import dotenv
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)
import os
import requests
import json
from bs4 import BeautifulSoup

BASE_URL = 'https://www.'
TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
TELEGRAM_API_SEND_MSG = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
i=0

################################################ Edit this lines:
# Edit each line from list to match the item on "items" with the maximum desired price.
PRICE_LIMIT = [
    50.0, 
    125.0
]

items = [
    'https://www.amazon.es/new-balance-zapatillas-para-hombre/dp/B07QMT5V84/?th=1&psc=1',
    'https://www.amazon.es/dp/B00M2OA5JI/ref=twister_B084XP4RJ7?_encoding=UTF8&psc=1'
]

################################################ End edit


for item in items:
    url = BASE_URL + item
    r = requests.get(
        url,
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
        })
    #Parsing the url to colect values and avoid code fail on empty data
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        name = soup.find(id='productTitle').get_text().strip()
        price = str(float(soup.find(id='priceblock_ourprice').get_text().replace('.', '').replace('€', '').replace(',', '.').strip())) + ' €'
        image = ''
    except:
        name = ''
        price = ''
        image = ''
    
    priceFloat = (float(price[:-2]))    #Is the actual price
    priceLimit = PRICE_LIMIT[i]     #Is the maximum desired price

    OFFER_SENDED = "OFFER_SENDED" + '_' + str(i)
    OFFER_ENV = os.getenv(OFFER_SENDED) #get the status message to prevent be repeated on each execution of code

    if (priceFloat<priceLimit):  #Check if  price was down to send message
        if (OFFER_ENV == str("False")):
            os.environ[OFFER_SENDED]="True" #set status message to true
            dotenv.set_key(dotenv_file, OFFER_SENDED, os.environ[OFFER_SENDED]) #record the file .env

            # CodeCheckLine:
            # print("Item ",i, ":",priceLimit, "€ is the desired price and ", priceFloat, "is the actual.")
            # print(OFFER_ENV)

            data = {
                'chat_id': CHAT_ID,
                'parse_mode' : 'markdown',
                'text': f'[{name}]({url})\n*{price}*'
            }
            r = requests.post(TELEGRAM_API_SEND_MSG, data=data) #send the message to telegram api

        # CodeCheckLine:
        # # elif (OFFER_ENV == str("True")):
        #     print(OFFER_ENV)
            
    else:
        os.environ[OFFER_SENDED]="False "#set status message to false
        dotenv.set_key(dotenv_file, OFFER_SENDED, os.environ[OFFER_SENDED]) #record the file .env
    i+=1











####################################### ON DEVELOP:

    # print (r.text)
    # print (r.status_code)
    # print(CHAT_ID)

    # # Modules:

    # def take_image(self):
    #     soup = BeautifulSoup(self.text, 'html.parser')
    #     img_div = soup.find(id="imgTagWrapperId")

    #     imgs_str = img_div.img.get('data-a-dynamic-image')  # a string in Json format
    #     # convert to a dictionary
    #     imgs_dict = json.loads(imgs_str)
    #     #each key in the dictionary is a link of an image, and the value shows the size (print all the dictionay to inspect)
    #     num_element = 0 
    #     first_link = list(imgs_dict.keys())[num_element]
    #     print(first_link)
    #     return first_link
    
