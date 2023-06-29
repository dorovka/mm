import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()
today = today.strftime("%d/%m/%Y")

payload = {"date_req":today}

response = requests.get(url,params=payload)
xml = BeautifulSoup(response.content,features="lxml")  # pip inastall lxml

usd = "R01235"
eur = "R01239"

# нахожэдение курса по id
def get_course(id):
    return xml.find("valute",{"id":id}).value.text

# Нахождение курса по charcode
def get_course_chr(chr):
    chr = xml.find("charcode",text = chr)
    valute = chr.parent
    return valute.value.text


usd_c = get_course(usd)
eur_c = get_course_chr("EUR")


usd_c = usd_c.replace(",",".")
eur_c = eur_c.replace(",",".")

if __name__ == '__main__':
    print(f"Курс доллара: {usd_c} рублей.")
    print(f"Курс евро: {eur_c} рублей.")
    print(f"Еурс доллара к евро: {(float(usd_c)/float(eur_c)):.4} евро")

# f = open("course.txt", "w") # w - запись, r - чтение, a - дописать
# f.write(f"date: {today} \nusd: {usd_c} rur.\neur: {eur_c} rur.\n")
# f.close()

"""
# словарь
Dict = {"ключ":"значение",
        "python":"programming language"}
Dict["java"] = "language"
Dict["java"] = "pl"
Dict1 = {"programming language": ["java","js","fortran","cpp","C#","rubby","wihitespace"]}

Dict.update(Dict1) # объединение словарей
print(Dict)
print(type(Dict))
print(Dict.get("java"))
# print(Dict["java"])
"""
