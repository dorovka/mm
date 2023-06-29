import bs4
import requests
import random
def get_interesting_fact():
    response = requests.get("https://i-fakt.ru/")
    response = response.content
    html = bs4.BeautifulSoup(response, "html.parser")
#fact = html.find(class_="p-2 clearfix")



    facts = html.find_all(class_="p-2 clearfix")
    facts = random.choice(facts)
    print(facts.text.strip())
    print(facts.a["href"])



#print(fact.text.strip()) удаляем пробельные символы
#print(fact.a["href"]) класс имеет тег а, является картинкой, находим ссылку с помощью href


def get_stand_up():
    response = requests.get("https://kudago.com/spb/entertainment/stand-up/")
    response = response.content
    html = bs4.BeautifulSoup(response, "lxml")
    stand_up = html.find(class_="post-title-link")
    print(stand_up.text)
    print(stand_up["href"])
    stand_up = html.find(class_ = "post-detail--event-place")
    print(stand_up.text)
    stand_up = html.find(class_="date-item")
    print(stand_up.text)
get_stand_up()