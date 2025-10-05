import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

import os

def train_model(data_path='simulated_data.csv', model_path='alert_model.joblib'):
    """
    Trains a machine learning model to predict alert levels.
    """
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define absolute paths for data and model
    abs_data_path = os.path.join(script_dir, data_path)
    abs_model_path = os.path.join(script_dir, model_path)

    # Load data
    try:
        data = pd.read_csv(abs_data_path)
    except FileNotFoundError:
        print(f"Error: Data file not found at {abs_data_path}")
        print("Please run data_simulator.py first to generate the data.")
        return

    # Features and target
    X = data[['distance', 'size']]
    y = data['alert_level']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the model
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")

    # Save the trained model
    joblib.dump(model, abs_model_path)
    print(f"Model trained and saved to '{abs_model_path}'")

if __name__ == "__main__":
    train_model()