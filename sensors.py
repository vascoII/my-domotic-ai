# sensors.py

import random

def get_sensor_data():
    """
    Simule la lecture de données depuis plusieurs capteurs.
    Dans la réalité, on irait chercher ces données sur un bus domotique,
    via un microcontrôleur, etc.
    """
    # Exemples de valeurs simulées
    temperature = round(random.uniform(15, 30), 2)
    humidity = round(random.uniform(30, 70), 2)
    co2_level = round(random.uniform(400, 1500), 2)
    
    return {
        "temperature": temperature,
        "humidity": humidity,
        "co2": co2_level
    }
