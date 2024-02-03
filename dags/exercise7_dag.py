from datetime import datetime, timedelta
from airflow import DAG

from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor


default_args = {
   'owner': 'ccarrenovi',
   'retries': 3,
   'retry_delay':timedelta(minutes=2)
}

with DAG(
    dag_id='exercise7_vs_1',
    default_args=default_args,
    description='Ejemplo de DAG con S3 Sensor',
    start_date=datetime(2024,2,1,2),
    schedule_interval='@daily'
) as dag:
    
    task1 = S3KeySensor(
        task_id = 'Task1',
        bucket_name='aikrflow',
        bucket_key = 'sample-products.csv',
        aws_conn_id = 'minio_s3_con'
    )

    task1