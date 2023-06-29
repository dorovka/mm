from tkinter import *
import random
import speech_recognition as sr
import pyttsx3
import pyaudio
privet = ["Здравия желаю!", "Здраствуйте.", "Я вас категорически приветствую."]
x = 0
window = Tk()
window.geometry("800x600")
window.title("кубики")
def c():
    global x
    x=1
title = Label(text = 'Список фильмов:', font = ('Comic Sans', 24), fg = 'white', bg = 'black')
title.place(x=0,y=0,width=800)
title = Label(text = 'пианист', font = ('Comic Sans', 14), fg = 'black')
title.place(x=0,y=100,width=800)
title = Label(text = 'курьер', font = ('Comic Sans', 14), fg = 'black')
title.place(x=0,y=200,width=800)
title = Label(text = 'иди и смотри', font = ('Comic Sans', 14), fg = 'black')
title.place(x=0,y=300,width=800)
title = Label(text = 'зеркало Тарковского', font = ('Comic Sans', 14), fg = 'black')
title.place(x=0,y=400,width=800)
b_1 = Button(text='Голосовой помошник', font =('Comic Sans', 15), command = c())
b_1.place(x=300,y=50,width=500)

r = sr.Recognizer()
voice = pyttsx3.init()
voice.say("Приветствую, меня зовут Владимир Ильич, чем я могу вам помочь?")
voice.runAndWait()
if x ==1:
    with sr.Microphone(device_index=1) as source:
        print("Скажите что-то...")
        audio = r.listen(source)
    speech = r.recognize_google(audio, language="ru_RU").lower()
    if "привет" in speech:
        voice.say(random.choice(privet))
        voice.runAndWait()
    elif "пока" in speech:
        voice.say("До скорого")
        voice.runAndWait()
    else:
        voice.say("Товарищ, не совсем понял, просьба повторить!")
        voice.runAndWait()


window.mainloop()