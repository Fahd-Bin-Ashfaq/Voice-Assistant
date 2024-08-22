import pyttsx3
import speech_recognition as sr
import datetime
import os
from greet import greetMe
from Dictapp import openappweb, closeappweb
from search import searchgoogle, searchYoutube, searchWikipedia

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again, please...")
        return "None"
    return query

if __name__ == "__main__":
    greetMe()
    while True:
        query = takeCommand().lower()

        if "wake up" in query:
            greetMe()

        elif "go to sleep" in query:
            speak("Ok sir, you can call me anytime.")
            break

        elif "hello" in query:
            speak("Hello sir, how are you?")

        elif "i am fine" in query:
            speak("That's great, sir!")

        elif "how are you" in query:
            speak("Perfect, sir!")

        elif "thank you" in query:
            speak("You're welcome, sir!")

        elif "open" in query:
            openappweb(query)

        elif "close" in query:
            closeappweb(query)

        elif "google" in query:
            searchgoogle(query)

        elif "youtube" in query:
            searchYoutube(query)

        elif "wikipedia" in query:
            searchWikipedia(query)

        elif "set alarm" in query:
            speak("Set the time for the alarm")
            time = input("Please tell the time (e.g., 10:10 AM): ")
            alarm(time)

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")

        elif "finally sleep" in query:
            speak("Going to sleep, sir.")
            exit()
