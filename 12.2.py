import random
import speech_recognition as sr
import pyttsx3
import pyaudio
privet = ["Здравия желаю!", "Здраствуйте.", "Я вас категорически приветствую."]
film = ['пианист', "курьер", "иди и смотри", "зеркало Тарковского"]
r = sr.Recognizer()
voice = pyttsx3.init()
voice.say("Приветствую, меня зовут Владимир Ильич, чем я могу вам помочь?")
voice.runAndWait()
while True:
    with sr.Microphone(device_index=1) as source:
        print("Скажите что-то...")
        audio = r.listen(source)
    speech = r.recognize_google(audio, language="ru_RU").lower()
    if "привет" in speech:
        voice.say(random.choice(privet))
        voice.runAndWait()
    elif "фильм" in speech:
        voice.say(random.choice(film))
        voice.runAndWait()
    elif "пока" in speech:
        voice.say("До скорого")
        voice.runAndWait()
        break
    else:
        voice.say("Товарищ, не совсем понял, просьба повторить!")
        voice.runAndWait()