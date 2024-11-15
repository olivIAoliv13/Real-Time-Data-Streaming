import requests
import json
import time
from kafka import KafkaProducer

# Configuration
API_KEY = '73ed67eeb50ad642aaad2c693d6c4d44'  # Clé API OpenWeatherMap
CITIES = ['Paris', 'London', 'Tokyo']  # Villes cibles
KAFKA_SERVER = 'localhost:9092'
KAFKA_TOPIC = 'tp-meteo'

# Initialisation du producteur Kafka
producer = KafkaProducer(
    bootstrap_servers=[KAFKA_SERVER],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Fonction pour récupérer les données météo d'une ville
def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()  # Retourne les données météo au format JSON
        else:
            print(f"Erreur API pour {city}: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erreur de requête pour {city}: {e}")
        return None

# Fonction d'envoi des données météo dans Kafka
def send_weather_data_to_kafka(city):
    weather_data = get_weather_data(city)
    if weather_data:
        data = {
            'city': city,
            'temp': weather_data['main']['temp'],
            'feels_like': weather_data['main']['feels_like'],
            'temp_min': weather_data['main']['temp_min'],
            'temp_max': weather_data['main']['temp_max'],
            'pressure': weather_data['main']['pressure'],
            'humidity': weather_data['main']['humidity'],
            'sea_level': weather_data['main'].get('sea_level', None),
            'grnd_level': weather_data['main'].get('grnd_level', None)
        }
        # Envoi des données dans le topic Kafka
        producer.send(KAFKA_TOPIC, value=data)
        print(f"Envoi des données météo pour {city} dans Kafka : {data}")
    else:
        print(f"Impossible de récupérer les données pour {city}")

# Boucle pour envoyer des données toutes les minutes
while True:
    for city in CITIES:
        send_weather_data_to_kafka(city)
    print("Attente avant l'envoi des prochaines données...")
    time.sleep(60)  # Attente de 60 secondes (1 minute)
