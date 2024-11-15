# Real-Time-Data-Streaming
# Real-Time-Data-Streaming

Créer un dossier dans la racine de votre projet nommé “kafka”
$ mkdir kafka

Créer un autre dossier dans la racine de votre projet nommé “spark”
$ mkdir spark

Créer dans le dossier kafka un fichier appélé “producer.py”
$ cd kafka
$ touch producer.py

renommer le fichier procuder.py en consomer.py
$ mv producer.py consomer.py

Afficher le contenu de votre repertoire racine
$ cd -
$ ls

Afficher le contenu de votre repertoire kafka
$ cd kafka
$ ls

Placer vous à l’aide de “cp” dans votre repertoire kafka
?

Installer java
$ sudo apt-get update
$ sudo apt-get install openjdk-11-jdk-headless

Installer kafka
$ wget https://archive.apache.org/dist/kafka/2.6.0/kafka_2.12-2.6.0.tgz
$ tar -xzf kafka_2.12-2.6.0.tgz

Démarrer un serveur zookeeper
$ ./kafka_2.12-2.6.0/bin/zookeeper-server-start.sh ./kafka_2.12-2.6.0/config/zookeeper.properties

Démarrer un server kafka
$  ./kafka_2.12-2.6.0/bin/kafka-server-start.sh ./kafka_2.12-2.6.0/config/server.properties

Créer un topic nommé “exo1”
$ ./kafka_2.12-2.6.0/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic exo1

Créer un autre topic nommé “exo2”
$ ./kafka_2.12-2.6.0/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic exo2

Afficher la liste de tous les topics disponibles
$ ./kafka_2.12-2.6.0/bin/kafka-topics.sh --list --bootstrap-server localhost:9092

Supprimer le topic “exo2”
$ ./kafka_2.12-2.6.0/bin/kafka-topics.sh --delete --bootstrap-server localhost:9092 --topic exo2

Produire des messages dans le topic “exo1”
$  ./kafka_2.12-2.6.0/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic exo1

Consommer des messages stockés dans le topic “exo1”
$  ./kafka_2.12-2.6.0/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic exo1 -- from-beginning

Ouvrir l'environnement virtuel
$ source kafka_env/bin/activate
