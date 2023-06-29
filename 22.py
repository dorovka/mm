import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()
today = today.strftime("%d/%m/%Y")

payload = {"date_req":today}

response = requests.get(url,params=payload)
xml = BeautifulSoup(response.content,features="lxml")


def get_course(id):
    return xml.find("valute",{"id":id}).value.text

def get_name(id):
    return xml.find("valute",{"id":id}).charcode.text

"R01239"
while True:
    try:
        to = str(input()).split()
        if to == 'конец':
            break
        eur_c = get_course(to)
        eur_d = get_name(to)
        print(f'1 штука {eur_d} стоит {eur_c} руб.')
    except AttributeError:
        print('Ошибка. Такой валюты нет.')