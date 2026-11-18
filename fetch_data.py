import requests
import csv

url = "https://api.open-meteo.com/v1/forecast?latitude=-20.25&longitude=57.42&hourly=temperature_2m&forecast_days=7"

response = requests.get(url)
data = response.json()

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["time", "temperature"])
    times = data["hourly"]["time"]
    temps = data["hourly"]["temperature_2m"]
    for t, temp in zip(times, temps):
        writer.writerow([t, temp])

print("Saved data.csv!")