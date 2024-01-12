from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
   'owner': 'ccarrenovi',
   'retries': 1,
   'retry_delay':timedelta(minutes=2)
}

dag1=DAG(
    dag_id='exercise0_simple_vs_1',
    default_args=default_args,
    description='Ejemplo de DAG',
    start_date=datetime(2024,1,11,2),
    schedule_interval='@daily'
)

bash_task1 = BashOperator(
    task_id='bash_task1',
    bash_command="echo Hola Mundo!, version 2, Apache Airflow",
    dag=dag1
)

bash_task1

