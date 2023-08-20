import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "414ef42a955b665d03f6a5415a1295f1"

def get_weather(city_name):
    BASE_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

    response = requests.get(BASE_URL)
    data = response.json()

    if data.get("cod") == 200:
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        return f"Weather: {weather}\nTemperature: {temperature}°C\nHumidity: {humidity}%"
    else:
        message = data.get("message", "City not found.")
        return message

def show_weather(event=None): 
    city_name = city_entry.get()
    if city_name:
        weather_data = get_weather(city_name)
        result_label.config(text=weather_data)
    else:
        messagebox.showwarning("Warning", "Please enter a city name.")

root = tk.Tk()
root.title("Weather App")


frame = tk.Frame(root, padx=70, pady=70)  
frame.grid(row=0, column=0, padx=20, pady=20)

city_label = tk.Label(frame, text="Enter city name:", font=("Helvetica", 15))
city_label.pack(pady=20)  

city_entry = tk.Entry(frame, font=("Helvetica", 16), borderwidth=2, relief="solid", bg="#f0f0f0")
city_entry.pack(pady=10, padx=20)


get_weather_button = tk.Button(frame, text="Get Weather", command=show_weather, font=("Helvetica", 12), bg="#4CAF50", fg="white", relief="raised", padx=15, pady=8)
get_weather_button.pack(pady=20)

result_label = tk.Label(frame, text="", font=("Helvetica", 12), wraplength=600) 
result_label.pack()


city_entry.bind("<Return>", show_weather)

root.mainloop()
