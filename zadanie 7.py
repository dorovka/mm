from tkinter import *
import random
import time
from emoji import *

window = Tk()
window.geometry('700x500')
window.title('Кликер')

points2 = 0
points = 0


def check2():
    global points2
    k.place(x=random.randint(1, 550), y=random.randint(1, 350))
    points2 += 1
    label['text'] = points + points2
    label['bg'] = 'red'
    if points + points2 >= 20:
        b['fg'] = 'green'
        k['fg'] = 'green'
    if points + points2 == 20:
        time.sleep(2)
    if points2 > 10 and points == 0:
        b['text'] = emojize("Ну пожалуйста :anguished_face:", variant="emoji_type")
    else:
        b['text'] = 'нажми меня'

def check():
    global points
    b.place(x=random.randint(1,550),y=random.randint(1,350))
    points +=1
    label['text'] = points + points2
    label['bg'] ='red'
    if points + points2 >= 20:
        b['fg'] = 'green'
        k['fg'] = 'green'
    if points + points2 == 20:
        time.sleep(2)
    if points > 10 and points2 == 0:
        k['text'] = emojize("Ну пожалуйста :anguished_face:", variant="emoji_type")
    else:
        k['text'] = 'нажми меня'



b = Button(text='нажми меня', font=('Arial', 20), fg='black', command=check)
b.place(x=400,y=130)


k = Button(text='нажми меня', font=('Sans', 20), fg='black', command=check2)
k.place(x=200,y=130)


label = Label(text = points, font=('Arial',15), fg='black')
label.place(x=10,y=10)






window.mainloop()
