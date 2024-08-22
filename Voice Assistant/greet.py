import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("GOOD MORNING, sir")
    elif hour > 12 and hour <= 18:
        speak("GOOD AFTERNOON, sir")
    else:
        speak("GOOD EVENING, sir")

    speak("Please tell me, how can I help you?")
