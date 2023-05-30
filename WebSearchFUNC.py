import webbrowser
import pyttsx3
import startup_sequence1
from startup_sequence1 import start_up_seq_web_search

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

start_up_seq_web_search()

def say(text):
    engine.say(text)
    engine.runAndWait()

def search(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    