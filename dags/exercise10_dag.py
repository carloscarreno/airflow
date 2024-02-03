from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
   'owner': 'ccarrenovi',
   'retries': 1,
   'retry_delay':timedelta(minutes=2)
}

with DAG(
    dag_id='exercise10_vs_2',
    default_args=default_args,
    description='Ejemplo de DAG',
    start_date=datetime(2024,1,30,2),
    schedule_interval='0 0 * * *'
) as dag:
    
    task1 = PostgresOperator(
        task_id='Task_1',
        postgres_conn_id = 'postgres_local',
        sql = """
              create table if not exists auditoria(
                 dt date,
                 dag_id character varying,
                 primary key(dt, dag_id)
              )
        """
    )

    task2 = PostgresOperator(
        task_id='Task_2',
        postgres_conn_id = 'postgres_local',
        sql = """
              insert into auditoria(dt, dag_id) values('{{ds}}','{{dag.dag_id}}')
        """
    )

    task1 >> task2