# Main folder for all API's  
import json
import requests
from startup_sequence1 import start_up_seq_weather_api

start_up_seq_weather_api()

def get_weather_data(city: str, api_key: str) -> dict:
    # Define API endpoint and parameters
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"

    # Make API request
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON data
        data = json.loads(response.text)

        # Extract weather data
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        weather_description = data['weather'][0]['description']

        # Return weather data as dictionary
        return {
            "city": city,
            "temperature": temperature,
            "humidity": humidity,
            "pressure": pressure,
            "weather_description": weather_description
        }
    else:
        # Return None if request was unsuccessful
        return None
