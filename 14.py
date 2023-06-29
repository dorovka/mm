from tkinter import *

window = Tk()
window.title("window")
window.geometry("800x600+300+100")

lab = Label(window, text='smth', font=('Arial', 16), bg = "#d899ff", fg = "gold")
lab.place(x=100,y=100)
lab['text'] = 'Какай'
count = 10
def func():
    global count
    count +=1
    btn['text'] = count

btn = Button(window, text='Кнопка', font=('Arial', 16), bg = "#d899ff", fg = "gold", command = func)
btn.place(x=300,y=200)
window.mainloop()