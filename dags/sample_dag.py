# dags/hello_world.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def say_hello():
    print("Hello from Airflow!")

with DAG(
    dag_id="hello_world",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["example"]
) as dag:
    task = PythonOperator(
        task_id="say_hello",
        python_callable=say_hello,
    )
