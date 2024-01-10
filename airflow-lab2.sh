#Instalacion de Airflow con Docker en Ubuntu 20.04.2
#====================================================


#Instalacion de Docker &  docker-compose
#---------------------------------------


sudo apt-get update
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg


echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo systemctl status docker

sudo usermod -aG docker ${USER}

#Nota: Esta ultima sentencia permite ejecutar docker como un usuario no sudoers

sudo apt  install docker-compose

docker-compose --version

#Creacion de los contenedores para Airflow
#-------------------------------------------

#Descarga el compose desde:

https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.8.0/docker-compose.yaml'

mkdir -p ./dags ./logs ./plugins ./config

echo -e "AIRFLOW_UID=$(id -u)" > .env

docker compose up airflow-init

docker compose up -d

sudo apt install net-tools