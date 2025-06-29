# Importing libraries
import numpy as np
import pandas as pd
from datetime import datetime
import os

# Extraction
def weather():
    # Extraction
    filepath = "/opt/airflow"
    data_path = os.path.join(filepath, "data", "seattle-weather.csv")
    weather_data = pd.read_csv(data_path, delimiter=',', encoding='utf-8')
    # Transformation
    weather_data['date'] = pd.to_datetime(weather_data['date'])
    weather_data['year'] = weather_data['date'].dt.year
    weather_data['month'] = weather_data['date'].dt.month
    weather_data['day_of_week'] = weather_data['date'].dt.day_name()
    weather_data['avg_temperature'] = round(weather_data['temp_max'] + weather_data['temp_min'] / 2, 2)
    weather_data['category'] = weather_data['weather'].apply(lambda x: 'Wet' if x == 'drizzle' or x == 'rain' or x == 'snow' else 'Dry')
    return weather_data