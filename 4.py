from tkinter import *
import bs4
import requests
import random

def get_interesting_fact():
    clear()
    home_btn()
    response = requests.get("https://i-fakt.ru/")
    response = response.content
    html = bs4.BeautifulSoup(response, "html.parser")



    facts = html.find_all(class_="p-2 clearfix")
    facts = random.choice(facts)
    Message(text = facts.text.strip()).place(x=0,y=0,width=700)

def home_btn():
    b = Button(text='Домой', font =('Comic Sans', 15), command = menu)
    b.place(x=25,y=500,width=200)

def clear():
    widgets = window.place_slaves()
    for i in widgets:
        i.destroy()

def menu():
    clear()
    title = Label(text = 'Что вы выберите?', font = ('Comic Sans', 24), fg = 'white', bg = 'black')
    title.place(x=0,y=0,width=700)
    b_1 = Button(text='Пройти тест', font =('Comic Sans', 15))
    b_2 = Button(text='Создать открытку', font =('Comic Sans', 15))
    b_3 = Button(text='Случайный факт', font =('Comic Sans', 15), command = get_interesting_fact)
    b_1.place(x=25,y=50,width=200)
    b_2.place(x=225, y=50, width=200)
    b_3.place(x=425, y=50, width=200)

window = Tk()
window.geometry("700x600")
window.title('project')
menu()
window.mainloop()