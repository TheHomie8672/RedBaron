# Test Commands

# Get_Time Command

import datetime
import pyttsx3

def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    return current_time

def say_time():
    engine = pyttsx3.init()
    engine.say("The current time is " + get_time())
    engine.runAndWait()

#to call use say_time() 

# Command two | Timer
 
