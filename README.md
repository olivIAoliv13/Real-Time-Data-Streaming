# Real-Time-Data-Streaming

### Visualisation de la météo en temps réel.

### Etapes de lancement

- Lancer Zoopkeeper
./kafka_2.12-2.6.0/bin/zookeeper-server-start.sh ./kafka_2.12-2.6.0/config/zookeeper.properties

- Lancer Kafka
./kafka_2.12-2.6.0/bin/kafka-server-start.sh ./kafka_2.12-2.6.0/config/server.properties

- Lancer producer.py
python3.10 producer.py

- Lancer spark.py
$SPARK_HOME/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.3 spark.py


#### En cas de pb
- Verifier que les topics actuels (de base - topic-weather et final - topic-weather-final) sont ok
Sinon : Les changer grace aux commandes (modifier le nom des topics dans le code aussi)

./kafka_2.12-2.6.0/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1--partitions 1 --topic topic-weather

./kafka_2.12-2.6.0/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1--partitions 1 --topic topic-weather-final

- Verifier que spark et Kafka sont bien télechargé
Sinon : Retelecharger 

Kafka : 
$ wget https://archive.apache.org/dist/kafka/2.6.0/kafka_2.12-2.6.0.tgz
$ tar -xzf kafka_2.12-2.6.0.tgz

Spark :
$ wget https://archive.apache.org/dist/spark/spark-3.2.3/spark-3.2.3-bin-hadoop2.7.tgz
$ tar -xvf spark-3.2.3-bin-hadoop2.7.tgz
config SPark :
$ export SPARK_HOME=/workspaces/<votre-repertoire>/spark-3.2.3-bin-hadoop2.7
$ export PATH=$SPARK_HOME/bin:$PATH

- Verifier que Python est bien en version 3.10
$ python --version

Sinon :
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt update
$ sudo apt install -y python3.10 python3.10-venv python3.10-distutils

## Résultats :

![image](https://github.com/user-attachments/assets/2c5f717a-aac4-4fc0-95c8-d2aa98dc2509)
