from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
   'owner': 'ccarrenovi',
   'retries': 5,
   'retry_delay':timedelta(minutes=2)
}

def getUsuario():
  return 'ccarrenovi'

with DAG(
    dag_id='exercise3_vs_1',
    default_args=default_args,
    description='Ejemplo de DAG con PythonOperator',
    start_date=datetime(2024,1,11,2),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id = 'Task_getUsuario',
        python_callable=getUsuario
    )
  
    task1