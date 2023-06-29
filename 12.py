import pyttsx3

my_text = xml = "брб куку куку чёчё прапапа"

voice = pyttsx3.init()
voice.say(my_text)
voice.runAndWait()