#Instalacion Local de Airflow en Ubuntu 22.04.2
#==========================================================

# Instalacion de SSH
#-------------------
sudo apt install openssh-server -y
sudo systemctl status ssh
sudo systemctl enable ssh
sudo ufw allow ssh

# Instalacion de git
#-------------------
sudo apt install git

# Instalacion de python3
#----------------------
sudo apt update
sudo apt install python3
python3 --version
sudo apt install python3-pip -y

#nota: En ubuntu 22.04.2 python3 esta instalado en version 3.10

# Instalacion de paquetes de Python
#--------------------------------

pip install apache-airflow[cncf.kubernetes]
pip install pandas
pip install virtualenv
pip install connexion[swagger-ui]

 
mkdir airflow_local
cd airflow_local

sudo apt install python3.10-venv -Y

python3 -m venv py_env

source py_env/bin/activate

pip install 'apache-airflow==2.8.0'  --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.8.0/constraints-3.8.txt"


./py_env/bin/python3 -m pip install --upgrade pip

#Iniciando Airflow Server
#------------------------

export AIRFLOW_HOME=/home/daddy/Airflow_Local

airflow db init

airflow users create --username admin --firstname carlos --lastname carreno --role Admin --email ccarrenovi@gmail.com

airflow db migrate 

airflow webserver -p 8080

#Nota: Abrir el archivo de configurcion airflow.db y configurar la ruta absoluta de la base de datos.


export AIRFLOW_HOME=/home/daddy/Airflow_Local
source py_env/bin/activate
airflow scheduler

mkdir /home/daddy/Airflow_Local/dags