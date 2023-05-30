import concurrent.futures
import time
import random
import requests
import RedBaronGraphics
from RedBaronGraphics import animate_graphic


def check_api_status(api_endpoint):
    try:
        response = requests.get(api_endpoint, timeout=5)
        if response.status_code == 200:
            return 'GOOD'
    except:
        pass
    return 'FAILED'
    

def start_up_seq_main_loop():
    animate_graphic()
    time.sleep(0.9)
    print(" ")
    time.sleep(1)
    connection_status = get_internet_connection_status()
    if connection_status:
        print("Connection -" + '\033[32m' + " Good" + '\033[0m')
    else:
        print("Connection -" + '\033[31m' + " Bad" + '\033[0m')
    print(" ")
    time.sleep(1)
    api_status = check_api_status("OpenAI")
    if api_status:
        print("OpenAI API - " + '\033[32m' + " Working" + '\033[0m')
    else:
        print("OpenAI API - " + '\033[31m' + " FAILURE" + '\033[0m')
    print(" ")
    time.sleep(1)
    print('\033[34m' + "main_loop Start-up Complete" + '\033[0m')
    print(" ")
    time.sleep(0.8)
    if not api_status:
        print('\033[31m' + "OpenAI API is not reachable" + '\033[0m')
    print('\033[36m' + "Speak Now: " + '\033[0m')
    print(" ")

def get_internet_connection_status():
    try:
        requests.get('https://www.google.com/', timeout=5)
        return True
    except:
        return False

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        future = executor.submit(start_up_seq_main_loop)

    # Your other program code goes here
    
    # Wait for the start_up_seq function to complete
    future.result()

def start_up_seq_web_search():
    print(" ")
    print("API - " + '\033[32m' + "Running" + '\033[0m')
    print(" ")
    time.sleep(1.2)
    try:
        requests.get('https://www.google.com/', timeout=5)
        print("Google Web Services - " + '\033[32m' + " Working" + '\033[0m')
    except:
        print("Google Web Services - " + '\033[31m' + " Failed" + '\033[0m')
    print(" ")
    time.sleep(1.8)
    print(" ")
    print('\033[34m' + "web_searchAPI Start-up Complete" + '\033[0m')
    print(" ")

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        future = executor.submit(start_up_seq_web_search)

def start_up_seq_weather_api():

    print("WeatherAPI - " + '\033[32m' + "Running" + '\033[0m')
    print(" ")
    time.sleep(1.5)
    api_key = "4ffe8a6a6920bed02ef374e1c1fa767a"  
    city = "Edmonton"   
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print("Open Weather Services -" + '\033[32m' + "online" + '\033[0m')
            print(" ")
            time.sleep(0.7)
            print("Weather Data -" + '\033[32m' + "Available" + '\033[0m')
            print(" ")
            time.sleep(1.2)
            print('\033[34m' + "weather_api Startup - " + "Complete" + '\033[0m')
            print(" ")
        else:
            print('\033[31m' + "weather_api Startup - " + "FAILED" + '\033[0m')
            print(" ")
    except requests.exceptions.RequestException as e:
        print('\033[31m' + "weather_api Startup - " + "FAILED" + '\033[0m')
        print(" ")


    # check if internet connection is working
    connection_status = get_internet_connection_status()
    if connection_status:
        print("Internet Connection -" + '\033[32m' + " Good" + '\033[0m')
        print(" ")
    else:
        print("Internet Connection -" + '\033[31m' + " FAILED" + '\033[0m')
        print(" ")

    # check if weather API is working
    




