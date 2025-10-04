import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def train_model(data_path='haptic_awareness_system/simulated_data.csv'):
    """
    Trains a machine learning model to predict alert levels.
    """
    # Load data
    data = pd.read_csv(data_path)

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
    joblib.dump(model, 'haptic_awareness_system/alert_model.joblib')
    print("Model trained and saved to 'haptic_awareness_system/alert_model.joblib'")

if __name__ == "__main__":
    train_model()