import telebot
import random
import requests
from bs4 import BeautifulSoup
token = "5988324226:AAFDcdHjv1sbS63-YSuP5fOS8H_H3OOGsS0"
bot = telebot.TeleBot(token)


#@bot.message_handler(command = ["audio"])
#def send_audio(message):
 #   audio = open(, "rb")
  #  bot.send_audio(message.chat.id)

print(len("jghsdjklghsjklhglshglhdslghlhdgsldhglsg"))






@bot.message_handler(commands= ['start', "help"])
def send_welcome(message):
    welcome_text = "Привет!"
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width= 1, resize_keyboard= True, one_time_keyboard=False)
    button1 = telebot.types.KeyboardButton("Факт")
    button2 = telebot.types.KeyboardButton("Котики")
    button3 = telebot.types.KeyboardButton("Поэма")
    button4 = telebot.types.KeyboardButton("Стикер")
    keyboard.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, welcome_text, reply_markup= keyboard)

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text == 'Факт':
        send_fact(message)
    elif message.text == "Котики":
        cats(message)
    elif message.text == "Поэма":
        send_poem(message)
    elif message.text == "Стикер":
        send_sticker(message)

@bot.message_handler(commands=['sticker'])
def send_sticker(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEG9FRjpJiOskpzsYXd1bOl6V5dBUmPXQACRQQAAvc0GwABmlJrRzCZ8OUsBA")

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
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_1 = telebot.types.InlineKeyboardButton("Перейти", url = "https://i-fakt.ru/")
    keyboard.add(button_1)
    bot.send_message(message.chat.id, facts, reply_markup=keyboard)

@bot.message_handler(commands= ["cat"])
def cats(message):
    cat_number = str(random.randint(1,4))
    cat_img = open("G:\\Godnota\\prochee\\" + cat_number + ".jpg", 'rb')
    bot.send_photo(message.chat.id, cat_img)

bot.polling(none_stop=True, interval=0)
