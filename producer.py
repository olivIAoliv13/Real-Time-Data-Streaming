#ATTENTION ! IL FAUT CREER UN NOUVEAU PRODUCER AVEC LA COMMANDE POUR QUE CA FONCTIONNE SINON DES DONNEES AVEC UN CERTAINS FORMATS RISQUE D'ETRE DEJA ENREGISTRE
#ici on a creer le tp-meteo2 : $ ./kafka_2.12-2.6.0/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic tp-meteo2

# Configuration
from kafka import KafkaProducer
import json
import time 

API_KEY = '73ed67eeb50ad642aaad2c693d6c4d44'  # Clé API
CITIES = ['Paris', 'London', 'Tokyo', 'Bangkok', 'Berlin']  # Villes cibles

KAFKA_TOPIC = 'topic-weather'

# Configuration
KAFKA_SERVER = 'localhost:9092'

# Initialisation du producteur Kafka
producer = KafkaProducer(
    bootstrap_servers=[KAFKA_SERVER],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

for city in CITIES : 
  # Envoi des données en continu
  producer.send("topic-weather",  value=city)

  import requests



# Fonction pour récupérer les données météo
def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None


# Boucle d'envoi en continu
while True:
    for city in CITIES:
        weather_data = get_weather_data(city)
        if weather_data:
            producer.send(KAFKA_TOPIC, key=city.encode('utf-8'), value=weather_data)
            # Affichage du message de confirmation
            print(f"Les données météo pour {city} ont été envoyées avec succès.")
        else:
            print(f"Impossible de récupérer les données pour {city}.")
    
    # Attendre 60 secondes avant le prochain envoi
    time.sleep(60)

# Assurer que toutes les données sont envoyées avant de fermer le producteur
producer.flush()

# Fermeture du producteur après l'envoi
producer.close()
