import os
import sys
import webbrowser
from time import sleep
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

cnt = 0
name = ""

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')  # To change the voice in female
engine.setProperty('voice', voices[1].id)  # To change the voice in female


def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            if cnt >= 1:
                print("Tell Me what else can i Do for You..?")
                speak("Tell Me what else can i Do for You..?")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace("alexa", "")


    except:
        pass
    return command


def run_alexa():
    c1 = take_command()
    if "play" in c1:
        song = c1.replace('play', " ")
        print("playing" + song)
        speak("playing " + song)
        pywhatkit.playonyt(song)
        sys.exit()
    elif "time" in c1:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print("Current Time is " + time)
        speak("Current Time is " + time)
        sleep(1)
    elif "who is" in c1:
        person = c1.replace("who is", "")
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)
        sleep(6)
    elif "date" in c1:
        datee = datetime.date.today().strftime("%B %d, %Y")
        print("Today is " + datee)
        speak("Today is " + datee)
        sleep(5)
    elif "single" in c1:
        print("No,I am in a Relationship With Wifi")
        speak("No,I am in a Relationship With Wifi")
        sleep(6)

    elif "open powerpoint" in c1:
        print("Opening Powerpoint..")
        speak("Opening powerpoint")
        pathh = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.exe"
        os.startfile(pathh)
        sleep(7)

    elif "open command prompt" in c1:
        print("Opening Command Prompt")
        speak("Opening Command Prompt")
        os.system("start cmd")
        sleep(6)

    else:
        print("I did not understand,Can you speak Again?")
        speak("I did not understand,Can you speak Again?")


with sr.Microphone() as source:
    print("Hello dear what is your name?")
    speak("Hello dear what is your name?")
    voice = listener.listen(source)
    con = listener.recognize_google(voice)
    con = con.lower()
    name = name + con
    if 'name' in con:
        name = con.replace("my name is ", "")
    print("Hello " + name + " I am Alexa. What can i do for You?")
    speak("Hello " + name + " I am Alexa. What can i do for You?")













while True:
    run_alexa()
    cnt = 1
