import requests
import csv
from datetime import datetime

# API Key and endpoint details
API_KEY = "47848fa44a8f923de28ec28b89ff7df5"  # Replace with your actual OpenWeatherMap API key
LAT = 33.6844  # Latitude for Islamabad
LON = 73.0479  # Longitude for Islamabad
BASE_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"

# API request
response = requests.get(BASE_URL)

# Handle the response
if response.status_code == 200:
    data = response.json()

    # Extract relevant fields
    if 'main' in data and 'wind' in data and 'weather' in data:
        fields = ['Temperature', 'Humidity', 'Wind Speed', 'Weather Condition', 'Date', 'Time']
        values = [
            data['main']['temp'],  # Temperature
            data['main']['humidity'],  # Humidity
            data['wind']['speed'],  # Wind Speed
            data['weather'][0]['description'],  # Weather Condition
            datetime.now().date(),  # Date
            datetime.now().time()  # Time
        ]

        # Save the data to a CSV file
        with open('raw_data.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(fields)
            writer.writerow(values)

        print("Data saved successfully!")
    else:
        print("Error: Some expected keys are missing in the API response.")
else:
    print(f"Error: API request failed with status code {response.status_code}")
