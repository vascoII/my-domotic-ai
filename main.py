# main.py

import time
from decision_engine import load_model, decide_action
from actuators import open_windows, close_windows, do_nothing

def main_loop(interval=5):
    """
    Boucle principale qui, toutes les X secondes, lit les capteurs,
    prédit l'action et agit en conséquence.
    """
    print("Chargement du modèle...")
    model = load_model()
    print("Modèle chargé. Démarrage de l'agent IA domotique.\n")
    
    while True:
        action, sensor_data = decide_action(model)
        print(f"Capteurs => {sensor_data}")
        
        if action == 0:
            do_nothing()
        elif action == 1:
            open_windows()
        elif action == 2:
            close_windows()
        else:
            print("Action inconnue !")
        
        # Temporisation
        time.sleep(interval)

if __name__ == "__main__":
    main_loop(interval=5)
