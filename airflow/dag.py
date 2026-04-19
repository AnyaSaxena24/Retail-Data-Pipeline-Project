<<<<<<< HEAD
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def ingest():
    print("Data Ingestion Completed")

def transform():
    print("Data Transformation Completed")

def load():
    print("Data Loaded to Database")

def analyze():
    print("Data Analysis Completed")

dag = DAG(
    'retail_data_pipeline',
    description='Retail Data Pipeline DAG',
    schedule_interval='@daily',
    start_date=datetime(2025, 1, 1),
    catchup=False
)

task1 = PythonOperator(task_id='ingestion', python_callable=ingest, dag=dag)
task2 = PythonOperator(task_id='transformation', python_callable=transform, dag=dag)
task3 = PythonOperator(task_id='loading', python_callable=load, dag=dag)
task4 = PythonOperator(task_id='analysis', python_callable=analyze, dag=dag)

=======
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def ingest():
    print("Data Ingestion Completed")

def transform():
    print("Data Transformation Completed")

def load():
    print("Data Loaded to Database")

def analyze():
    print("Data Analysis Completed")

dag = DAG(
    'retail_data_pipeline',
    description='Retail Data Pipeline DAG',
    schedule_interval='@daily',
    start_date=datetime(2025, 1, 1),
    catchup=False
)

task1 = PythonOperator(task_id='ingestion', python_callable=ingest, dag=dag)
task2 = PythonOperator(task_id='transformation', python_callable=transform, dag=dag)
task3 = PythonOperator(task_id='loading', python_callable=load, dag=dag)
task4 = PythonOperator(task_id='analysis', python_callable=analyze, dag=dag)

>>>>>>> 0ba55a4fda3736f5faf58da868efe97116708868
task1 >> task2 >> task3 >> task4