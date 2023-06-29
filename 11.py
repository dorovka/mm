import requests
from bs4 import BeautifulSoup #так как не можем использовать json из за вида кода
from datetime import datetime

today = datetime.today()
print(today)
today = today.strftime("%d/%m/%Y")
print(today)
payload = {"date_req":today}


response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp?", params = payload)
xml = BeautifulSoup(response.content, "html.parser")
def get_curs(id):
    return xml.find("valute", {"id" : id}).value.text

def get_cur_ср(charcode):
    return xml.find("charcode", text = charcode).value.text
print(get_cur_ср("EUR"))
if response.status_code == 200: #200 значит, что запрос выполнен успешно
    xml = BeautifulSoup(response.content, "html.parser")
    print(get_curs("R01375"))
    print(get_curs("R01239"))
    print(get_curs("R01235"))