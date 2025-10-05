import pandas as pd
import time
import joblib

import os

def run_awareness_system(data_path='simulated_data.csv', model_path='alert_model.joblib'):
    """
    Simulates the haptic awareness system by reading sensor data
    and providing alerts using a machine learning model.
    """
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define absolute paths
    abs_data_path = os.path.join(script_dir, data_path)
    abs_model_path = os.path.join(script_dir, model_path)

    # Load the trained model
    try:
        model = joblib.load(abs_model_path)
    except FileNotFoundError:
        print(f"Error: Model file not found at {abs_model_path}")
        print("Please run 'train_model.py' first to train and save the model.")
        return

    try:
        data = pd.read_csv(abs_data_path)
    except FileNotFoundError:
        print(f"Error: Data file not found at {abs_data_path}")
        print("Please run 'data_simulator.py' first to generate the data.")
        return

    print("Starting haptic awareness system with ML model...")
    print("-----------------------------------")

    for index, row in data.iterrows():
        distance = row['distance']
        size = row['size']

        # Prepare data for prediction
        features = [[distance, size]]

        # Predict alert level
        prediction = model.predict(features)[0]

        alert = "No alert"
        if prediction == 'ALERT':
            alert = "!!! ALERT: Large object detected very close!"
        elif prediction == 'beep':
            alert = "Beep! Object detected in blind spot."

        if alert != "No alert":
            print(f"Distance: {distance:.2f}m, Size: {size:.2f}m -> {alert} (Predicted: {prediction})")

        # Simulate real-time sensor data
        time.sleep(0.1)

    print("-----------------------------------")
    print("Simulation finished.")

if __name__ == "__main__":
    run_awareness_system()