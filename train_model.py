# train_model.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_decision_model(data_path="data/sensor_data.csv"):
    """
    Entraîne un modèle de classification à partir de données historiques.
    Les données contiennent par exemple :
      - temperature
      - humidity
      - co2
      - action (0/1/2)
    """
    df = pd.read_csv(data_path)
    X = df[["temperature", "humidity", "co2"]]
    y = df["action"]
    
    model = RandomForestClassifier(n_estimators=50)
    model.fit(X, y)
    
    # Sauvegarde du modèle entraîné
    joblib.dump(model, "models/decision_model.pkl")
    print("Modèle entraîné et sauvegardé avec succès !")

if __name__ == "__main__":
    train_decision_model()
