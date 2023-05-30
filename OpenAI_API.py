import openai



import speech_recognition as sr
import pyttsx3
import time

# initalize Openai API
openai.api_key = "sk-ZcAwsYSYvodh8cUWezWiT3BlbkFJr"
# initialize the text to speech engine
engine=pyttsx3.init()


def transcribe_audio_to_test(filename):
    recognizer=sr.Recognizer()
    with sr.AudioFile(filename)as source:
        audio=recognizer.record(source)
        
    try:
        return recognizer.recognize_google(audio)
    except:
        print("skipping unknown error")
        
def generate_response(prompt):
    response=openai.completion.create(
        engine="text-davinci-003",
        prompt=prompt
        max_tokens=4000
       n=1
       stop=None
       temperature=0.5,
    )
    return response ["Choices"][01]["text"]
def speak_text(text):
    engine.say(text)
    engine.runAndwait()
    
    def main():
        while True:
            #Waith for users say "genius"
            print("say 'genius' to begin question")
            with sr.Microphone() as source:
                recognizer=sr.Recognizer()
                audio=recognizer.listen(source)
                try:
                    transcription=recognizer.recognize_google(audio)
                    if transcription.lower()=="genius":
                        #record audio
                        filename="input"
                    

