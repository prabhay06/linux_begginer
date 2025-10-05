import serial
import joblib
import time
import pandas as pd
import os

# --- Get the directory of the current script ---
script_dir = os.path.dirname(os.path.abspath(__file__))

# --- Configuration ---
# !!! IMPORTANT: Change this to the correct serial port for your ESP32 !!!
# On Windows, it will be something like 'COM3'.
# On macOS or Linux, it will be something like '/dev/tty.usbserial-XXXX'.
SERIAL_PORT = 'COM3'  # <-- CHANGE THIS
BAUD_RATE = 9600

MODEL_PATH = os.path.join(script_dir, 'alert_model.joblib')
RESULTS_LOG_PATH = os.path.join(script_dir, 'results.csv')

def initialize_serial(port, baud_rate):
    """Initializes and returns a serial connection object."""
    try:
        ser = serial.Serial(port, baud_rate, timeout=2)
        print(f"Successfully connected to serial port {port} at {baud_rate} baud.")
        return ser
    except serial.SerialException as e:
        print(f"Error: Could not open serial port {port}. {e}")
        print("Please ensure the following:")
        print("1. The ESP32 is connected to your computer.")
        print("2. The correct SERIAL_PORT is set in this script.")
        print("3. The necessary drivers for your ESP32 are installed.")
        return None

def load_model(model_path):
    """Loads the trained machine learning model."""
    try:
        model = joblib.load(model_path)
        print("Machine learning model loaded successfully.")
        return model
    except FileNotFoundError:
        print(f"Error: Model file not found at '{model_path}'.")
        print("Please run 'train_model.py' first to train and save the model.")
        return None

def log_results(log_path, data):
    """Logs the prediction results to a CSV file."""
    # Check if the file exists to write headers
    write_header = not os.path.exists(log_path)

    # Create a DataFrame to append
    df = pd.DataFrame([data])

    # Append to the CSV file
    df.to_csv(log_path, mode='a', header=write_header, index=False)

def predict_from_sensor():
    """
    Reads real-time sensor data, predicts alerts, and logs the results.
    """
    # Initialize serial connection and load the model
    ser = initialize_serial(SERIAL_PORT, BAUD_RATE)
    model = load_model(MODEL_PATH)

    if ser is None or model is None:
        print("Exiting due to initialization failure.")
        return

    print("\n--- Real-Time Blind Spot Alert System ---")
    print("Press Ctrl+C to exit.")

    try:
        while True:
            # Read a line from the serial port
            line = ser.readline().decode('utf-8').strip()

            if line:
                try:
                    # Convert the received distance to a float
                    distance_cm = float(line)
                    distance_m = distance_cm / 100  # Convert cm to meters for the model

                    # --- Get object size (user input) ---
                    # In a real application, this might come from another sensor (e.g., a camera).
                    size_input = input(f"Distance: {distance_m:.2f}m. Enter estimated object size (in meters): ")
                    size_m = float(size_input)

                    # Prepare data for prediction
                    features = [[distance_m, size_m]]

                    # Predict alert level
                    prediction = model.predict(features)[0]

                    # Determine the alert message
                    alert_message = "No alert"
                    if prediction == 'ALERT':
                        alert_message = "!!! ALERT: Large object detected very close!"
                    elif prediction == 'beep':
                        alert_message = "Beep! Object detected in blind spot."

                    print(f"  -> Prediction: {prediction.upper()} | Alert: {alert_message}\n")

                    # Log the results
                    log_data = {
                        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
                        'distance_m': f"{distance_m:.2f}",
                        'size_m': f"{size_m:.2f}",
                        'prediction': prediction,
                        'alert_message': alert_message
                    }
                    log_results(RESULTS_LOG_PATH, log_data)

                except ValueError:
                    # Handle cases where the serial data or user input is not a valid number
                    print(f"Received invalid data: '{line}'. Please enter a valid number for size.")
                except KeyboardInterrupt:
                    print("\nExiting...")
                    break

            # A small delay to prevent overwhelming the CPU
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\n--- System stopped by user. ---")
    finally:
        if ser and ser.is_open:
            ser.close()
            print("Serial port closed.")

if __name__ == "__main__":
    predict_from_sensor()