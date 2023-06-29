import random
import webbrowser
from datetime import datetime
import speech_recognition as sr
import pyttsx3
import pyaudio

r = sr.Recognizer()
voice = pyttsx3.init()
voice.say("Привет, меня зовут Мухаммед, чем я могу вам помочь?")
voice.runAndWait()
while True:
    with sr.Microphone(device_index=1) as source:
        print("Скажите что-то...")
        audio = r.listen(source)
    speech = r.recognize_google(audio, language="ru_RU").lower()

    if speech.find("привет") >= 0 or "здравствуйте" in speech: #можно "привет" in speech
        voice.say("Асалам алейкум")
        voice.runAndWait()

    elif "coinflip" in speech or "монетк" in speech:
        if random.randint(0,1):
            coin = "Орёл"
        else:
            coin = "Решка"


        voice.say("У вас", coin)
        voice.runAndWait()
    elif "пока" in speech:
        voice.say("До скорого еээзжииии")
        voice.runAndWait()
        break
    elif "ютуб" in speech or "youtube" in speech:
        webbrowser.open_new("https://www.youtube.com/watch?v=WehNoR4ZovE")
        voice.say("Открываю братэла")
        voice.runAndWait()
    elif "время" in speech:
        date = datetime.today()
        voice.say(str(date.hour) + " " + str(date.minute))
        voice.runAndWait()
    else:
        voice.say("Не вьезжаюуу, либо у меня такой команды нет, либо говори чётко, ишак!")
        voice.runAndWait()
print(speech)