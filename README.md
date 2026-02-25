# Gandhinagar Weather Analysis (Last 10 Days)

This Python script fetches **daily max and min temperatures** for Gandhinagar, Gujarat (India) using the [Open-Meteo Archive API](https://open-meteo.com/), and computes **basic statistics** (average and median).

## Features
- Fetches last 10 days of weather data (max & min temperatures).
- Prints results in Markdown-style headings.
- Computes:
  - Average Max Temperature
  - Average Min Temperature
  - Median Max Temperature
  - Median Min Temperature

## Requirements
- Python 3.7+
- Libraries:
  - `requests`
  - `statistics` (built-in)

Install dependencies:
```bash
pip install requests
