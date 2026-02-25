import requests
from datetime import datetime, timedelta
import statistics

lat, lon = 23.2156, 72.6369
start = (datetime.today() - timedelta(days=10)).strftime("%Y-%m-%d")
end = datetime.today().strftime("%Y-%m-%d")

url = (
    f"https://archive-api.open-meteo.com/v1/archive?"
    f"latitude={lat}&longitude={lon}&start_date={start}&end_date={end}"
    f"&daily=temperature_2m_max,temperature_2m_min&timezone=Asia/Kolkata"
)

response = requests.get(url)
data = response.json()

dates = data["daily"]["time"]
tmax_list = data["daily"]["temperature_2m_max"]
tmin_list = data["daily"]["temperature_2m_min"]

print("## Gandhinagar Weather (Last 10 Days)\n")
for date, tmax, tmin in zip(dates, tmax_list, tmin_list):
    print(f"- {date}: Max {tmax}°C / Min {tmin}°C")

# Basic statistics
avg_max = statistics.mean(tmax_list)
avg_min = statistics.mean(tmin_list)
median_max = statistics.median(tmax_list)
median_min = statistics.median(tmin_list)

print("\n## Summary Statistics")
print(f"- Average Max Temp: {avg_max:.2f}°C")
print(f"- Average Min Temp: {avg_min:.2f}°C")
print(f"- Median Max Temp: {median_max:.2f}°C")
print(f"- Median Min Temp: {median_min:.2f}°C")
