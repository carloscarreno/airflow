from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
   'owner': 'ccarrenovi',
   'retries': 5,
   'retry_delay':timedelta(minutes=2)
}

def printMessage(usuario, rol):
  print(f"Bienvenido a Airflow! {usuario} ud ingreso como {rol}")

with DAG(
    dag_id='exercise2_vs_3',
    default_args=default_args,
    description='Ejemplo de DAG con PythonOperator',
    start_date=datetime(2024,1,11,2),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id = 'Task_printMessage',
        python_callable=printMessage,
        op_kwargs={'usuario': 'ccarrenovi', 'rol': 'Admin'}
    )
  
    task1