# decision_engine.py

import joblib
from sensors import get_sensor_data

def load_model(path="models/decision_model.pkl"):
    model = joblib.load(path)
    return model

def decide_action(model):
    data = get_sensor_data()  # lecture capteurs
    X = [[
        data["temperature"],
        data["humidity"],
        data["co2"]
    ]]
    
    action = model.predict(X)[0]
    return action, data
