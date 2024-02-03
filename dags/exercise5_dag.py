from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
   'owner': 'ccarrenovi',
   'retries': 5,
   'retry_delay':timedelta(minutes=2)
}

# ti es una variable built-in usanda para referenciar las instancias de tareas
def printMessage(rol, ti):
  usuario=ti.xcom_pull(task_ids='Task_setUsuario')
  name=ti.xcom_pull(task_ids='Task_setUsuario',key='name')
  lastname=ti.xcom_pull(task_ids='Task_setUsuario',key='lastname')
  print(f"Bienvenido {name}, {lastname} a Airflow! {usuario} ud ingreso como {rol}")

def setUsuario(ti):
  ti.xcom_push(key='name', value='Juan')
  ti.xcom_push(key='lastname', value='Perez')
  return 'ccarrenovi'

with DAG(
    dag_id='exercise5_vs_1',
    default_args=default_args,
    description='Ejemplo de DAG con PythonOperator',
    start_date=datetime(2024,1,11,2),
    schedule_interval='@daily'
) as dag:
    
    task1 = PythonOperator(
        task_id = 'Task_printMessage',
        python_callable=printMessage,
        op_kwargs={'rol': 'Admin'}
    )

    task2 = PythonOperator(
        task_id = 'Task_setUsuario',
        python_callable=setUsuario
    )
  
    task2 >> task1