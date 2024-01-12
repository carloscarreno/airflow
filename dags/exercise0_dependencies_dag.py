from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

def welcome():
    print("Bienvenido a Apache Airflow 2.8.0!")

default_args = {
   'owner': 'ccarrenovi',
   'retries': 1,
   'retry_delay':timedelta(minutes=2)
}

dag1=DAG(
    dag_id='exercise0_dependencies_vs_1',
    default_args=default_args,
    description='Ejemplo de DAG',
    start_date=datetime(2024,1,11,2),
    schedule_interval='@daily'
)


python_task1 = PythonOperator(
    task_id = 'python_task1',
    python_callable=welcome,
    dag=dag1
)

bash_task1 = BashOperator(
    task_id='bash_task1',
    bash_command="echo Hola Mundo!",
    dag=dag1
)

python_task1 >> bash_task1

