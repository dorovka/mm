from tkinter import *
import webbrowser

window = Tk()
window.geometry("1500x700")
window.title("Dangerous")
window.resizable(width=False, height=False)
text = Label(text="ВЫ ВЫЙГРАЛИ В ЛОТЕРЕЕ!", bg="grey", fg="lime", font=("Comic Sans", 64))
text.place(relheight=1, relwidth =1)

count_text = Label(text = "4", bg="black", fg="lime", font= ("Comic Sans", 64))

def on_close():
    if int(count_text["text"]) > 0:
        count_text.place(relheigh= 1, relwidth = 1)
        count_text['text'] = int(count_text["text"]) - 1
        window.after(800, on_close)
    else:
        webbrowser.open("https://drive.google.com/file/d/1oav0A--bJlbQFPN0C6nQxAbjKsFfDbJj/view?usp=share_link")
        window.overrideredirect(1) #убираем рамки
        window.state("zoomed")
        photo = PhotoImage(file = "DSC.png")
        ph_label = Label(image = photo, bg = "black")
        ph_label.photo = photo
        ph_label.place(relheight = 1, relwidth = 1)

window.protocol("WM_DELETE_WINDOW", on_close)
window.mainloop()