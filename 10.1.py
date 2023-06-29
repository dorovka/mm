import requests
from bs4 import BeautifulSoup #так как не можем использовать json из за вида кода
from datetime import datetime

today = datetime.today()
#print(today)
today = today.strftime("%d/%m/%Y")
#print(today)
payload = {"date_req":today}


response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp?", params = payload)

valute_from = "RUS"

valute_to = "R01235"

amount = int(input())




def get_curs(value_to):
    return xml.find("valute", {"id" : value_to}).value.text

if response.status_code == 200: #200 значит, что запрос выполнен успешно
    xml = BeautifulSoup(response.content, "html.parser")
    print(get_curs(valute_to))
    print(amount * get_curs(valute_to))


    """all = xml.find_all("valute")
    for i in all:
        print(i.value.text)"""