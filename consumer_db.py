from kafka import KafkaConsumer
import psycopg2
import json
from datetime import datetime

# Configuration de Kafka
KAFKA_TOPIC = 'tp-meteo2'
KAFKA_SERVER = 'localhost:9092'
PASSWORD_DB = "wdZ0NnLIUce4"

# Configuration de la base de données Neon PostgreSQL
db_connection = psycopg2.connect(
    f"postgresql://meteo_owner:wdZ0NnLIUce4@ep-square-surf-a5zzakek.us-east-2.aws.neon.tech/meteo?sslmode=require"
)
cursor = db_connection.cursor()

# Initialisation du consumer Kafka
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=[KAFKA_SERVER],
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("En attente de messages...")

# Consommer les messages et insérer dans la base de données
for message in consumer:
    data = message.value

    # Extraire les informations nécessaires
    ville = data['name']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    temperature = data['main']['temp']
    humidite = data['main']['humidity']
    vent = data['wind']['speed']
    
    # Récupérer la date et l'heure actuelles
    date = datetime.now()

    # Insérer les données dans la table `meteo`
    try:
        cursor.execute(
            """
            INSERT INTO meteo (ville, latitude, longitude, temperature, humidite, vent, date)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (ville, latitude, longitude, temperature, humidite, vent, date)
        )
        db_connection.commit()
        print(f"Données insérées pour {ville}: Temp={temperature}°C, Humidité={humidite}%, Vent={vent} m/s, Date={date}")
    except Exception as e:
        print(f"Erreur lors de l'insertion pour {ville}: {e}")
        db_connection.rollback()

# Fermer la connexion à la base de données à la fin du traitement
cursor.close()
db_connection.close()
