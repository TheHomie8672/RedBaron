import concurrent.futures
import os
import pyttsx3
import startup_sequence1
import requests
import speech_recognition as sr
import time
import openai
import webbrowser
import validators
import pyaudio
import wave
import startup_sequence1
import RedBaronGraphics
import RedBaronOS
import RedBaronCommandDir
from RedBaronCommandDir import say_time
from RedBaronGraphics import animate_graphic
from startup_sequence1 import start_up_seq_main_loop, start_up_seq_weather_api, start_up_seq_web_search
from playsound import playsound
from gtts import gTTS
from WeatherAPI import get_weather_data
from WebSearchFUNC import search
from WebSearchFUNC import say
from io import BytesIO
from PIL import Image





promptA = "You are Red, an AI assistant develpoed by Marcus Sherman and powered by GPT3. Your purpose is general task managment and Programming. "
promptB = ""
promptC = ""
promptD = ""

ValidityCheckPromptA = ""
ValidityCheckPromptB = ""
ValidityCheckPromptC = ""
ValidityCheckPromptD = ""

AgentOPCheckA = ""
AgentOPCheckB = ""
AgentOPCheckC = ""
AgentOPCheckD = ""

ActivePrompt = list[promptA, promptB, promptC, promptD]


openai.api_key = "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"

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Initialize speech recognizer
r = sr.Recognizer()

goodbye_phrases = ["Say, Hey Red, if you need me","Let me know if I can help", "Give me a shout when you need me"]

def calculator():
    num1 = float(input("Enter the first number: "))
    op = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Error: Division by zero")
            return
        else:
            result = num1 / num2
    else:
        print("Error: Invalid operator")
        return

    print("Result: ", result)
    return result


def display_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()



    try:
        image_url = response["choices"][0]["text"].split("\n")[0].strip()
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img.save("generated_image.png")
        return img
    except:
        return None




def play_audio(audio_file):
    CHUNK = 1024
    wf = wave.open(audio_file, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(CHUNK)
    while data:
        stream.write(data)
        data = wf.readframes(CHUNK)
    stream.stop_stream()
    stream.close()
    p.terminate()

def on_phrase(self, recognizer, audio):
    try:
        recognized_text = recognizer.recognize_google(audio)
        print("You said:", recognized_text)
        if "search" in recognized_text:
            query = recognized_text.split("search", 1)[1].strip()
            search(query)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def search(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def callback(recognizer_instance, audio, mute_flag=False):
    try:
        if not mute_flag:
            recognizer_instance.stop()
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

import webbrowser

def say_output(output_text):
    print(f"Red: {output_text}")
    if "http" in output_text:
        webbrowser.open(output_text)
    else:
        engine = pyttsx3.init()
        engine.say(output_text)
        engine.runAndWait()



def get_input(prompt, is_keyword=False, mute=False):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if not mute:
            print(prompt)
        if is_keyword:
            r.energy_threshold = 5500
            r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return ""

def user_input():
    return input("You: ")


start_up_seq_main_loop()
def main_loop():
    
    startup_sequence1
    waiting_for_keyword = False
    flag_state = False
    flag_time = None
    input_text = ""
    mute_flag = False

    while True:
        if waiting_for_keyword:
           
            input_text = get_input("Say 'Hey Baron' to start a conversation.", True)

            if input_text is not None and any(keyword in input_text.lower() for keyword in ["Hey Baron"]):
                waiting_for_keyword = False
                say_output("How can I help you?")
        else:
            # Get the user's input
            
            user_input = get_input("", False, mute_flag)

            # Check if the user has stopped speaking
            if not user_input:
                if flag_state and time.time() - flag_time >= 5:
                    waiting_for_keyword = True
                    flag_state = False
                    say_output("Holler if you need me")
                continue

            # Process the user's input
            print(f"User input: {user_input}")
            if "exit" in user_input.lower() or "goodbye" in user_input.lower() or "bye" in user_input.lower():
                say_output("Goodbye!")
                return

            elif "weather" in user_input.lower():
                city = user_input.split()[-1]
                print(f"Getting weather data for {city}...")
                weather_data = get_weather_data(city, os.environ.get("OPENWEATHER_API_KEY"))
                
                if weather_data:
                    temperature = weather_data["temperature"]
                    weather_description = weather_data["weather_description"]
                    response_text = f"The temperature in {city} is {temperature:.1f} degrees Celsius with {weather_description}."
                    say_output(response_text)
                    print(response_text)
                else:
                    response_text = f"Sorry, could not retrieve weather data for {city}."
                    say_output(response_text)
                    print(response_text)
                    
                    
                    # Hard-Coded Commands!
            
            elif "mute" in user_input.lower(): # not working | Show-Stopper | 
               waiting_for_keyword = True
               say_output("Aight, peace")

            elif "unmute" in user_input.lower(): # not working | Show-Stopper | 
                waiting_for_keyword = False
                say_output("Sup")

            elif "meaning of life" in user_input: # | Non-Essencial | 
                say("the meaning of life is 42")
            
            elif "What are you" in user_input: # | Non-Essencial | 
                say("I am an assistant being developed by Marcus Sherman. I am designed to respond inteligently to any questions and requests you may have.") 
                main_loop()

            elif "who is marcus sherman" in user_input: # Sorry abojut my Vanity | Non-Essencial | 
                say("Marcus Alexander Sherman, born October Ninth, Two Thousand and three, is a freelance software developer and my creator!")
                main_loop()

            elif "are you recording me" in user_input: # | Non-Essencial | 
                say("Maybe, maybe not")
                main_loop()
            
            elif "status check mainloop" in user_input: # Just check to make sure that the Main-Loop isnt being Cheeky
                say("begining main loop diagnostics")
                start_up_seq_main_loop()
                main_loop()

            elif "status check weather api" in user_input: # as the Name would Suggest, It check the connection status of the Web-Check Function
                say("begining weather api diagnostics")
                start_up_seq_weather_api()
                main_loop()

            elif "status check web search" in user_input: # I think the name is rather self Explanatory
                say("begining web search diagnostics") 
                start_up_seq_web_search()
                main_loop()

            elif "reset" in user_input: # Use if encountering a Falure State
                say("restarting. . .")
                main_loop()
            
            elif "play opening graphic" in user_input: # Plays the Opening Graphic 
                animate_graphic()
                main_loop()
        
            elif "whats the time" in user_input: # | Non-Critical |
                say_time()
                main_loop()

            elif "what is 2 + 2" in user_input:
                say("2 + 2 = 5")
                time.sleep(0.5)
                say("Just kidding, the answer is 4")
                main_loop()
                
            elif "pull up your calculator" in user_input: # so far untested
                say("absolutely, here you go") 
                calculator()
                main_loop()

            elif "command list" in user_input:
                say("absolutely, here you go") # replace with a dict when able
                print("mute, unmute, status check mainloop, status check weather api")
                print("status check web search, reset, what time is it, pull up your calculator")
                time.sleep(0.6)
                main_loop()

           

            # os integration in progress | Not Working | needs proper PATHS!
            
            elif "open chrome" in user_input.lower():
                say("understood, opening chrome")
                os.startfile("chrome.exe")
                main_loop()
            
            elif "open notepad" in user_input.lower():
                say("understood, opening notepad")
                os.startfile("notepad.exe")
                main_loop()
            
            elif "open calculator" in user_input.lower():
                say("understod, opening calculator")
                os.startfile("calc.exe")
                main_loop()
            
            elif "open file explorer" in user_input.lower():
                say("understood, opening file explorer")
                os.startfile("explorer.exe") 
                main_loop()

            else:
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    future = executor.submit(openai.Completion.create, 
                    engine="text-davinci-003",  
                    prompt= ActivePrompt + "  |  " +  user_input, max_tokens=4000, n=1, stop=None, temperature=0.4)
        

            response_text = future.result().choices[0].text.strip()
            print(response_text)

        if "search" in user_input.lower(): # websearch needs work 
            query = user_input.replace("search", "").strip()
            say_output(f"Searching for {query}...")
            search(query)

        # Check if response text is a valid URL
        elif validators.url(response_text):
            webbrowser.open(response_text)

        else:
            say_output(response_text)
            flag_state = True
            flag_time = time.time()

if __name__ == "__main__":
    main_loop()
    
    