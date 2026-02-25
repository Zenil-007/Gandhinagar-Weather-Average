import requests
from datetime import datetime, timedelta
import pandas as pd
import statistics

# Gandhinagar coordinates
lat, lon = 23.2156, 72.6369
start = (datetime.today() - timedelta(days=10)).strftime("%Y-%m-%d")
end = datetime.today().strftime("%Y-%m-%d")

# Weather API (Open-Meteo Archive)
weather_url = (
    f"https://archive-api.open-meteo.com/v1/archive?"
    f"latitude={lat}&longitude={lon}&start_date={start}&end_date={end}"
    f"&daily=temperature_2m_max,temperature_2m_min&timezone=Asia/Kolkata"
)

# AQI API (Open-Meteo Air Quality → hourly data)
aqi_url = (
    f"https://air-quality-api.open-meteo.com/v1/air-quality?"
    f"latitude={lat}&longitude={lon}&start_date={start}&end_date={end}"
    f"&hourly=us_aqi&timezone=Asia/Kolkata"
)

# Fetch weather data
weather_data = requests.get(weather_url).json()
dates = weather_data["daily"]["time"]
tmax_list = weather_data["daily"]["temperature_2m_max"]
tmin_list = weather_data["daily"]["temperature_2m_min"]

# Fetch AQI data (hourly)
aqi_data = requests.get(aqi_url).json()
aqi_times = aqi_data["hourly"]["time"]
aqi_values = aqi_data["hourly"]["us_aqi"]

# Convert AQI hourly data into daily averages
df = pd.DataFrame({"time": pd.to_datetime(aqi_times), "aqi": aqi_values})
df["date"] = df["time"].dt.date
daily_aqi = df.groupby("date")["aqi"].mean().reset_index()

# ---------------- WEATHER OUTPUT ----------------
print("# 🌤 Gandhinagar Weather & AQI Report (Last 10 Days)\n")

print("## 📌 Weather Data\n")
for date, tmax, tmin in zip(dates, tmax_list, tmin_list):
    print(f"- **{date}** → Max: **{tmax}°C**, Min: **{tmin}°C**")

# Weather Statistics
avg_max = statistics.mean(tmax_list)
avg_min = statistics.mean(tmin_list)
median_max = statistics.median(tmax_list)
median_min = statistics.median(tmin_list)

print("\n### 📊 Weather Summary Statistics")
print(f"- Average Max Temp: **{avg_max:.2f}°C**")
print(f"- Average Min Temp: **{avg_min:.2f}°C**")
print(f"- Median Max Temp: **{median_max:.2f}°C**")
print(f"- Median Min Temp: **{median_min:.2f}°C**")

# ---------------- AQI OUTPUT ----------------
print("\n## 🌫 Gandhinagar AQI Data\n")
for _, row in daily_aqi.iterrows():
    print(f"- **{row['date']}** → AQI: **{row['aqi']:.2f}**")

# AQI Statistics
avg_aqi = daily_aqi["aqi"].mean()
median_aqi = daily_aqi["aqi"].median()

print("\n### 📊 AQI Summary Statistics")
print(f"- Average AQI: **{avg_aqi:.2f}**")
print(f"- Median AQI: **{median_aqi:.2f}**")
