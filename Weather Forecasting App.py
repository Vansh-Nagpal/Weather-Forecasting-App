import requests

API_KEY = 'your_openweathermap_api_key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/'

def get_weather_data(city):
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def get_forecast_data(city):
    url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def display_weather(data):
    if data.get("cod") != 200:
        print("City not found.")
        return
    
    print(f"Current Weather in {data['name']} ({data['sys']['country']}):")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description'].capitalize()}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s\n")

def display_forecast(data):
    if data.get("cod") != "200":
        print("City not found.")
        return
    
    print(f"5-Day Weather Forecast for {data['city']['name']} ({data['city']['country']}):")
    for item in data['list']:
        date = item['dt_txt']
        temp = item['main']['temp']
        description = item['weather'][0]['description'].capitalize()
        print(f"{date} - Temp: {temp}°C - {description}")

def main():
    print("Weather Forecasting App")
    city = input("Enter city name: ")

    weather_data = get_weather_data(city)
    display_weather(weather_data)

    forecast_data = get_forecast_data(city)
    display_forecast(forecast_data)

if __name__ == "__main__":
    main()



import tkinter as tk
from tkinter import messagebox

def fetch_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    weather_data = get_weather_data(city)
    if weather_data.get("cod") != 200:
        messagebox.showerror("Error", "City not found.")
        return

    weather_info = f"""
    City: {weather_data['name']}
    Country: {weather_data['sys']['country']}
    Temperature: {weather_data['main']['temp']}°C
    Weather: {weather_data['weather'][0]['description'].capitalize()}
    Humidity: {weather_data['main']['humidity']}%
    Wind Speed: {weather_data['wind']['speed']} m/s
    """
    result_label.config(text=weather_info)

root = tk.Tk()
root.title("Weather Forecasting App")

city_label = tk.Label(root, text="Enter city name:")
city_label.pack(pady=10)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

fetch_button = tk.Button(root, text="Fetch Weather", command=fetch_weather)
fetch_button.pack(pady=10)

result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=10)

root.mainloop()