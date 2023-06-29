from tkinter import *
from random import randint


def clear():
    widgets = window.place_slaves()
    for i in widgets:
        i.destroy()





def Next_page():
    clear()
    ent_txt = message.get()
    dog_num = 0
    d1 = 0
    d2 = 1
    for i in range(ent_txt):
        dog_num += 1
        dog_balls = randint(0, 10)
        d1 +=1
        if d1 > 14:
            d2 +=1
            d1 =1
        vuvod = ("у собаки под номером " + str(dog_num) + ", " + str(dog_balls) + " балла(ов)")
        Poluch = Label(text = vuvod, fg="black", font=("Comic Sans", 32))
        Poluch.grid(row = d1, column = d2)



def menu():
    global message
    text = Label(text="""Cколько собак учавствует
    в гонках?""", bg="black", fg="white", font=("Comic Sans", 50))
    text.place(x=360, y=200, width = 880)
    bt = Button(text = "Дальше!",bg="black", fg="white", font = ("Comic Sans", 50), command = Next_page)
    bt.place(x = 675, y = 550, width = 300)
    message = IntVar()
    x = Entry(window, width = 60, textvariable=message)
    message.set("")
    x.place(x=640, y = 450)




window = Tk()
window.geometry("1600x780")
window.title("App")

menu()
window.mainloop()




