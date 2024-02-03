from datetime import datetime, timedelta
from airflow import DAG

from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor 

default_args = {
   'owner': 'ccarrenovi',
   'retries': 10,
   'retry_delay':timedelta(minutes=2)
}

with DAG(
    dag_id='exercise11_vs_2',
    default_args=default_args,
    description='Ejemplo de DAG',
    start_date=datetime(2024,1,30,2),
    schedule_interval='0 0 * * *'
) as dag:
    
    task1 = S3KeySensor(
        task_id='Task1',
        bucket_name='airflow',
        bucket_key='sample-products.csv',
        aws_conn_id='minio_s3_con'

        
    )

    task1
