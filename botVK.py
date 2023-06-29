import vk_api
import json
import sys
import time
import requests
from bs4 import BeautifulSoup as BS
from parserX import *
import datetime
from diam import *

with open('key.json', 'r') as key:
    token = json.load(key)
    token = token['key']
bot = vk_api.VkApi(token=token)  # Импорт экземпляра бота
bot._auth_token()  # регистрация

while True:
    messages = bot.method('messages.getConversations', {'count': 200, 'filter': 'unanswered'})
    if messages['count'] > 0:
        messages_id = messages['items'][0]['last_message']['id']
        id_1 = messages['items'][0]['last_message']['from_id']
        text = messages['items'][0]['last_message']['text']

        if text.lower() == 'показатели':
            bot.method('messages.send', {'peer_id': id_1, 'random_id': messages_id, 'message': get_course("USD")})

        elif text.lower() == 'диаметр':
            bot.method('messages.send',
                       {'peer_id': id_1, 'random_id': messages_id, 'message': Starships(url_starships)})

        elif text.lower() == 'корабли':
            bot.method('messages.send',
                       {'peer_id': id_1, 'random_id': messages_id, 'message': Starships2(url_starships2)})

        else:
            bot.method('messages.send', {'peer_id': id_1, 'random_id': messages_id, 'message': 'ошибка'})