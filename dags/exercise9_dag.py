from datetime import datetime, timedelta
from airflow.decorators import dag, task

default_args = {
   'owner': 'ccarrenovi',
   'retries': 1,
   'retry_delay':timedelta(minutes=2)
}

@dag(
    dag_id='exercise9',
    default_args=default_args,
    description='Ejemplo de DAG con decoradores',
    start_date=datetime(2024,1,11,2),
    schedule_interval='@daily'
)

def demo_decorators():

    @task()
    def getUsername():
        return "ccarrenovi"

    @task()
    def getRole():
        return "Administrador"

    @task()
    def printGreetings(username, role):
        print(f"Bienvenido usuario {username}, ud ingreso con el rol {role}")

    usuario= getUsername()
    rol = getRole()

    printGreetings(usuario,rol)

decorator_dag = demo_decorators()
