from etl_weather import weather
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv("/opt/airflow/.env")


def main():
    # Read Variables
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    database = os.getenv('DB_NAME')

    # Create the connection engine
    engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')
    weather_data = weather()
    print('Data has been successfully extracted and transformed into a dataframe')

    # Load to the database
    weather_data.to_sql('weather_staging', con=engine, if_exists='append', index=False)
    print("Data has been staged into weather_staging table successfully.")

    # SQL transformation: weather_staging → weather_data
    transform_sql = """
    BEGIN;
    
    TRUNCATE TABLE weather_data;
    
    INSERT INTO weather_data (date, precipitation, temp_max, temp_min, wind,weather,year,month,day_of_week,avg_temperature,category)
    SELECT
        date,
        precipitation,
        temp_max,
        temp_min,
        wind,
        weather,
        year,
        month,
        day_of_week,
        avg_temperature,
        category  
    FROM weather_staging;
    
    COMMIT;
    """

    # Execute the transformation SQL
    with engine.connect() as conn:
        conn.execute(text(transform_sql))
        print("Data transformed and loaded into weather_data.")
