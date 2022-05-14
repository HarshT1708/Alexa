import sys
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices') #To change the voice in female
engine.setProperty('voice', voices[1].id) #To change the voice in female

def speak(text):
    engine.say(text)
    engine.runAndWait()

def talk_command():
    try:
        with sr.Microphone() as source:
            print("Tell Me what can i do for you?")
            speak("Tell Me what can i do for you?")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
               command = command.replace("alexa", "")


    except:
        pass
    return command

def run_alexa():
    c1 = talk_command()
    if 'play' in c1:
        song = c1.replace('play', " ")
        print("playing " + song)
        speak("playing "+song)
        pywhatkit.playonyt(song)
        sys.exit()
    elif 'time' in c1:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print("Current Time is " + time)
        speak("Current Time is "+time)
    elif 'who is ' in c1:
        person = c1.replace("who is", "")
        info = wikipedia.summary(person , 1)
        print(info)
        speak(info)
    elif 'date' in c1:
        datee = datetime.date.today().strftime("%B %d, %Y")
        print(datee)
        speak(datee)
    elif 'single' in c1:
        print("No,I am in a Relationship With Wifi")
        speak("No,I am in a Relationship With Wifi")
    elif 'bye' or 'exit' or 'end' in c1:
        print('Bye..See you again next Time')
        speak('Bye..See you again next Time')
        sys.exit()
    else:
        print("I did not understand,Can you speak Again?")
        speak("I did not understand,Can you speak Again?")









while True:
    run_alexa()
