import csv
import logging
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.amazon.aws.hooks.s3 import S3Hook

default_args = {
   'owner': 'ccarrenovi',
   'retries': 5,
   'retry_delay':timedelta(minutes=2)
}

def postgres_to_s3(ds_nodash, next_ds_nodash):
    hook = PostgresHook(postgres_conn_id = "postgres_local_con")
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("select * from orders where date > %s and date <= %s ",(ds_nodash, next_ds_nodash))
    with open(f"dags/get_orders.txt_{ds_nodash}","w") as f:
        csv_writer = csv.writer(f)
        # Escribe los nombres de las columnas
        csv_writer.writerow([i[0] for i in cursor.description])
        # Escribe las filas de la consulta
        csv_writer.writerows(cursor)
    cursor.close
    conn.close()
    logging.info("Se guardo las ordenes en el archivo: %s",(f"dags/get_orders.txt_{ds_nodash}"))
    # Cargamos los archivos a Amazon S3 (minio)
    s3_hook = S3Hook(aws_conn_id="minio_con")
    s3_hook.load_file(
        filename=f"dags/get_orders.txt_{ds_nodash}",
        key=f"orders/orders-{ds_nodash}.txt",
        bucket_name="airflow",
        replace=True
    )

with DAG(
    dag_id='exercise14_vs_1',
    default_args=default_args,
    description='Ejemplo de DAG con PythonOperator',
    start_date=datetime(2022,4,30,2),
    schedule_interval='@daily'
) as dag:
    
    task1 = PythonOperator(
        task_id = 'Task_1',
        python_callable=postgres_to_s3
    )
  
    task1