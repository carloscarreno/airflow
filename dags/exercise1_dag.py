from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
   'owner': 'ccarrenovi',
   'retries': 3,
   'retry_delay':timedelta(minutes=2)
}

with DAG(
    dag_id='exercise1_vs_6',
    default_args=default_args,
    description='Ejemplo de DAG con BashOperator',
    start_date=datetime(2024,1,11,2),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='Task_1',
        bash_command="echo Hola Mundo version airflow!"
    )

    task2 = BashOperator(
        task_id='Task_2',
        bash_command="echo Otra vez hola, desde Task2!"
    )

    task3 = BashOperator(
        task_id='Task_3',
        bash_command="echo Otra vez hola, desde Task3!"
    )

    # task1.set_downstream(task2)

    # task1.set_downstream(task3)

    #task1 >> task2
    #task1 >> task3

    task1 >> [task2, task3]

