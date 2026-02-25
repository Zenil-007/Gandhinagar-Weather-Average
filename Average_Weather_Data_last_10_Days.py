import requests
from datetime import datetime, timedelta
import pandas as pd
import statistics

# Gandhinagar coordinates
lat, lon = 23.2156, 72.6369
start = (datetime.today() - timedelta(days=10)).strftime("%Y-%m-%d")
end = datetime.today().strftime("%Y-%m-%d")

# AQI API (Open-Meteo Air Quality → hourly data)
aqi_url = (
    f"https://air-quality-api.open-meteo.com/v1/air-quality?"
    f"latitude={lat}&longitude={lon}&start_date={start}&end_date={end}"
    f"&hourly=us_aqi&timezone=Asia/Kolkata"
)

# Fetch AQI data
aqi_data = requests.get(aqi_url).json()
aqi_times = aqi_data["hourly"]["time"]
aqi_values = aqi_data["hourly"]["us_aqi"]

# Convert AQI hourly data into daily averages
df = pd.DataFrame({"time": pd.to_datetime(aqi_times), "aqi": aqi_values})
df["date"] = df["time"].dt.date
daily_aqi = df.groupby("date")["aqi"].mean().reset_index()

# Print AQI values
print("## Gandhinagar AQI (Last 10 Days)\n")
for _, row in daily_aqi.iterrows():
    print(f"- {row['date']}: AQI {row['aqi']:.2f}")

# AQI Statistics
avg_aqi = daily_aqi["aqi"].mean()
median_aqi = daily_aqi["aqi"].median()

print("\n## AQI Summary Statistics")
print(f"- Average AQI: {avg_aqi:.2f}")
print(f"- Median AQI: {median_aqi:.2f}")
