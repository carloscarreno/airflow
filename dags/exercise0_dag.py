from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
   'owner': 'ccarrenovi',
   'retries': 1,
   'retry_delay':timedelta(minutes=2)
}

with DAG(
    dag_id='exercise0_vs_1',
    default_args=default_args,
    description='Ejemplo de DAG',
    start_date=datetime(2024,1,11,2),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='Task_1',
        bash_command="echo Hola Mundo!, version Apache Airflow"
    )

    task1