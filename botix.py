import telebot
import random
import requests
from bs4 import BeautifulSoup
token = "5988324226:AAFDcdHjv1sbS63-YSuP5fOS8H_H3OOGsS0"
bot = telebot.TeleBot(token)

@bot.message_handler(commands= ['start', "help"])
def send_welcome(message):
    welcome_text = "Привет!"
    bot.send_message(message.chat.id, welcome_text)
@bot.message_handler(commands= ["poem"])
def send_poem(message):
    poem_text = "Без тебя как без хуя, чё то не круто нихуя!"
    bot.send_message(message.chat.id, poem_text)

@bot.message_handler(commands= ["fact"])
def send_fact(message):
    response = requests.get("https://i-fakt.ru/")
    response = response.content
    html = BeautifulSoup(response, "lxml")
    facts = html.find_all(class_="p-2 clearfix")
    facts = random.choice(facts)
    facts = facts.text.strip()
    bot.send_message(message.chat.id, facts)

@bot.message_handler(commands= ["cat"])
def send_fact(message):
    cat_number = str(random.randint(1,4))
    cat_img = open("G:\\Godnota\\prochee\\" + cat_number + ".jpg", 'rb')
    bot.send_photo(message.chat.id, cat_img)

bot.polling(none_stop=True, interval=0)
bot.run()