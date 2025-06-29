from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

sys.path.append("/opt/airflow/scripts")
from load_data import main


default_args = {
    'start_date': datetime(2025, 5, 21),
}

with DAG(
    dag_id='weather_etl_pipeline',
    default_args=default_args,
    catchup=False,
    tags=['weather', 'etl'],
) as dag:

    run_etl_task = PythonOperator(
        task_id='run_weather_etl',
        python_callable=main,
    )