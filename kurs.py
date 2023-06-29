from tkinter import *
import requests
from bs4 import BeautifulSoup as BS
import datetime
today = datetime.datetime.today().strftime('%d/%m/%Y')

url = "http://www.cbr.ru/scripts/XML_daily.asp?"
response = requests.get(url, params = {"date_req":today})
xml = BS(response.content, 'lxml')

response2 = requests.get("https://coinspot.io/").content
xml2 = BS(response2, 'lxml')
bit = xml2.find("a", href ="/currencies/view/BTC/").span.text
print(bit)

def get_course(chr):
    chr = xml.find('charcode', text = chr)
    chr = chr.parent #возвращаемся вверх, к id
    chr = chr.value #спускаемся опять вниз, но уже к value
    return chr.text


window = Tk()
window.geometry('400x350+300+300')
window.title("Курс валют")
window.resizable(width=False, height=False)

canvas = Canvas(width=250, height=250)
canvas.pack(anchor=CENTER, expand=1)
canvas.create_rectangle(10, 10, 210, 200, outline="#EA4643")
canvas.create_rectangle(5, 5, 215, 205, outline="#EA4643")
canvas.create_rectangle(5, 0, 220, 210, outline="#EA4643")
canvas.create_rectangle(5, 0, 230, 220, outline="#EA4643")
canvas.create_rectangle(5, 0, 240, 230, outline="#EA4643")
canvas.create_rectangle(5, 0, 250, 240, outline="#EA4643")
canvas.create_line(5, 0, 250, 240, fill = "#EA4643")
canvas.create_line(210, 10, 250, 240, fill = "#EA4643")
canvas.create_line(10, 200, 250, 240, fill = "#EA4643")

lab = Label(window, text='Курс валют \n имбабанк', font = ("Comic", 24), fg='#EA4643')
lab.place(y=25, x=150)

img = PhotoImage(file='knight.png')
logo = Label(window, image = img)
logo.place(y=0, x=0)

info_course = Label(window, text="Курс валют на: " + today.replace("/", "."), font=("comic", 16), fg = "black")
info_course.place(y=140, x=90)

euro_course = Label(window, text='€ ' +get_course("EUR"), font = ("Comic", 16), fg='black')
euro_course.place(y=180, x=100)

dollor_course = Label(window, text='$ ' +get_course("USD"), font = ("Comic", 16), fg='black')
dollor_course.place(y=210, x=100)

bit_course = Label(window, text='BTC ' +bit[:9], font = ("Comic", 16), fg='black')
bit_course.place(y=240, x=100)

yuan_course = Label(window, text='¥ ' +get_course("CNY"), font = ("Comic", 16), fg='black')
yuan_course.place(y=270, x=100)

window.mainloop()
