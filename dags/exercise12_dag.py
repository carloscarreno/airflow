import csv
import logging
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

default_args = {
   'owner': 'ccarrenovi',
   'retries': 5,
   'retry_delay':timedelta(minutes=2)
}

def postgres_to_s3():
    hook = PostgresHook(postgres_conn_id = "postgres_local_con")
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("select * from orders where date <= '20220501'")
    with open("dags/get_orders.txt","w") as f:
        csv_writer = csv.writer(f)
        # Escribe los nombres de las columnas
        csv_writer.writerow([i[0] for i in cursor.description])
        # Escribe las filas de la consulta
        csv_writer.writerows(cursor)
    cursor.close
    conn.close()
    logging.info("Se guardo las ordenes en el archivo get_orders.txt")
  

with DAG(
    dag_id='exercise12_vs_2',
    default_args=default_args,
    description='Ejemplo de DAG con PythonOperator',
    start_date=datetime(2024,2,1,2),
    schedule_interval='@daily'
) as dag:
    
    task1 = PythonOperator(
        task_id = 'Task_1',
        python_callable=postgres_to_s3
    )
  
    task1