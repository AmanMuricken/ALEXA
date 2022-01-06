import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listner=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)



def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    with sr.Microphone() as source:
        print("listening....")
        listner.adjust_for_ambient_noise(source)
        voice=listner.listen(source)
        global command 
        command=listner.recognize_google(voice)
        command=command.lower()
        if "alexa" in command:
            command=command.replace("alexa","")        
            print (command)
        return command

def run_alexa():
    command=take_command()
    print(command)
    if "play" in command:
        song=command.replace("play","")
        talk("playing "+song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time=datetime.datetime.now().strftime("%I:%M %P")
        talk("current time is "+time)
    elif "who the heck is" in command:
        person=command.replace("who the heck is ","")
        info=wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif "date" in command:
        talk("sorry,I have a headache")
    elif "are you single" in command:
        talk("I am in a relationship with WIFI")
    elif "joke" in command:
        talk(pyjokes.get_joke())
    else:
        talk("please say the command again")

while True:
    run_alexa()