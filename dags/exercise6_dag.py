from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
   'owner': 'ccarrenovi',
   'retries': 5,
   'retry_delay':timedelta(minutes=2)
}

# ti es una variable built-in usanda para referenciar las instancias de tareas
def printMessage(ti):
  usuario=ti.xcom_pull(task_ids='Task_getUsuario')
  name=ti.xcom_pull(task_ids='Task_getUsuario',key='name')
  lastname=ti.xcom_pull(task_ids='Task_getUsuario',key='lastname')
  rol=ti.xcom_pull(task_ids='Task_getRol',key='rol')
  print(f"Bienvenido {name}, {lastname} a Airflow! {usuario} ud ingreso como {rol}")

def getUsuario(ti):
  ti.xcom_push(key='name', value='Juan')
  ti.xcom_push(key='lastname', value='Perez')
  return 'ccarrenovi'

def getRol(ti):
  ti.xcom_push(key='rol', value='Admin') 

with DAG(
    dag_id='exercise6_vs_1',
    default_args=default_args,
    description='Ejemplo de DAG con PythonOperator',
    start_date=datetime(2024,1,11,2),
    schedule_interval='@daily'
) as dag:
    
    task1 = PythonOperator(
        task_id = 'Task_printMessage',
        python_callable=printMessage,
    )

    task2 = PythonOperator(
        task_id = 'Task_getUsuario',
        python_callable=getUsuario
    )
  
    task3 = PythonOperator(
        task_id = 'Task_getRol',
        python_callable=getRol
    )

    [task2, task3] >> task1