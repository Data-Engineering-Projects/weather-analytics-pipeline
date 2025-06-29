# 🌤️ Weather Analytics ETL Pipeline with Airflow, PostgreSQL & Metabase

This project is a complete **ETL + Analytics + Visualization pipeline** designed to process and analyze weather data from Seattle. The workflow is fully containerized using Docker and orchestrated using Apache Airflow.

---

## 🛠 Tech Stack

- **Apache Airflow** – ETL Orchestration
- **PostgreSQL** – Data Warehousing (staging + production tables)
- **Docker + Docker Compose** – Environment & container management
- **Metabase** – Data visualization dashboard
- **Python + Pandas** – Data transformation logic
- **SQL Views** – Analytical queries

---

## 📈 Features & Visualizations

The dashboard is divided into **2 key tabs**:

### 🔹 1. Seasonal Trends and Stats
- **Average Wind Speed**
- **Average Temperature Change**
- **Avg Month-wise Temperature**
- **Categories vs Wind Speed**
- **Coldest Day**
- **Correlation: Wind Speed & Precipitation**
- **Highest Rainfall Month**
- **Hottest Day**
- **Maximum Precipitation**

### 🔹 2. Weather Condition Distributions
- **Distribution of Weather Conditions**
- **Extreme Weather Days**
- **Most Common Weather Conditions**

---

## 🧩 Project Structure

---

## ⚙️ ETL Workflow

1. **Extract**: Reads `seattle_weather.csv`
2. **Transform**:
   - Cleans and standardizes column names
   - Converts dates, fills missing values, categorizes weather
3. **Load**:
   - Loads data into `weather_staging` table in PostgreSQL
   - Performs data quality checks
   - Moves valid data to `weather_data` production table

⏳ Orchestrated using Apache Airflow DAGs (`weather_etl.py`)

---

## 📊 Metabase Dashboard

- The Metabase container connects to the PostgreSQL database.
- SQL views based on `weather_data` table serve as the data source.
- Dashboard includes **2 tabs**:
  - `Seasonal Trends and Stats`
  - `Weather Condition Distributions`

---

## 🐳 Getting Started

### Prerequisites

- Docker & Docker Compose installed

### Steps to Run

1. **Clone this repo**:
   ```bash
   git clone https://github.com/Data-Engineering-Projects/weather-analytics-pipeline.git
    cd weather-etl
   docker-compose up --build
2. **Access Services**:
    - Airflow: http://localhost:8080
    - Metabase: http://localhost:3000
    - PostgreSQL: port 5432
3. **Run the DAG**:
    - Trigger the weather_etl DAG in the Airflow UI.
4. **Set up Metabase**:
    - Connect to PostgreSQL
    - Point to weather_data and your analytical views
    - Build and organize the dashboard

### Data Checks
Before loading into production:
- Null checks
- Date format validation
- Range checks for temperature, wind speed, etc.
- Only after passing all checks is data inserted into weather_data.
