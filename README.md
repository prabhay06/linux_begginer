# 🤖 Real-Time Haptic Awareness System

This project implements a blind spot awareness system that uses an ultrasonic sensor (HC-SR04) connected to an ESP32 microcontroller to measure distance in real-time. This data is then fed into a Python script that uses a trained machine learning model to predict and issue alerts.

This repository is an evolution of the original haptic awareness system, integrating real-world hardware for a practical application.

## 📂 Repository Structure

The project is organized into two main directories:

-   `/microcontroller`: Contains the Arduino code (`.ino`) for the ESP32 to read from the ultrasonic sensor.
-   `/python`: Contains all the Python scripts for data simulation, model training, and real-time prediction.

## 🛠️ Hardware Requirements

To build this project, you will need the following hardware:

-   **ESP32 Development Board**: Any ESP32 board will work.
-   **HC-SR04 Ultrasonic Sensor**: For distance measurement.
-   **Breadboard**: For creating the circuit.
-   **Jumper Wires**: To connect the components.
-   **Micro-USB Cable**: To connect the ESP32 to your computer.

## 🔌 Hardware Setup

Wire the HC-SR04 ultrasonic sensor to the ESP32 as follows.

### Wiring Diagram:

| HC-SR04 Pin | ESP32 Pin |
| :---------- | :-------- |
| VCC         | VIN (5V)  |
| GND         | GND       |
| Trig        | GPIO5 (D5)  |
| Echo        | GPIO18 (D18)|

**Visual Representation:**

```
      ESP32                  HC-SR04
      +------------------+     +------------------+
      | VIN (5V)         |-----| VCC              |
      | GND              |-----| GND              |
      | GPIO5 (D5)       |-----| Trig             |
      | GPIO18 (D18)     |-----| Echo             |
      +------------------+     +------------------+
```

## 💻 Software Setup & Workflow

Follow these steps to get the system up and running.

### Step 1: Set up the Microcontroller

1.  **Install Arduino IDE**: If you don't have it, [download and install the Arduino IDE](https://www.arduino.cc/en/software).
2.  **Add ESP32 Board Support**:
    *   Open Arduino IDE, go to `File > Preferences`.
    *   In "Additional Board Manager URLs", add: `https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json`
    *   Go to `Tools > Board > Boards Manager`, search for "esp32" and install the package by Espressif Systems.
3.  **Flash the Code**:
    *   Open `microcontroller/esp32_ultrasonic.ino` in the Arduino IDE.
    *   Select your ESP32 board from `Tools > Board`. (e.g., "ESP32 Dev Module").
    *   Select the correct COM port from `Tools > Port`.
    *   Click the "Upload" button to flash the code to your ESP32.
    *   You can verify it's working by opening the Serial Monitor (`Tools > Serial Monitor`) and setting the baud rate to `9600`. You should see distance readings.

### Step 2: Set up the Python Environment

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/prabhay06/linux_begginer.git
    cd linux_begginer
    ```
2.  **Create and Activate a Virtual Environment**:
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install Dependencies**:
    Navigate to the python directory and install the required packages.
    ```bash
    cd python
    pip install -r requirements.txt
    ```

### Step 3: Train the Machine Learning Model

Before running the real-time system, you need to train the model. The necessary files are generated in the `/python` directory.

1.  **Generate Data**:
    ```bash
    python data_simulator.py
    ```
    This creates `simulated_data.csv`.

2.  **Train the Model**:
    ```bash
    python train_model.py
    ```
    This creates `alert_model.joblib`.

### Step 4: Run the Real-Time Alert System

1.  **Configure Serial Port**:
    *   Open `python/predict_from_sensor.py` in a text editor.
    *   Find the `SERIAL_PORT` variable.
    *   **On Windows**, change it to your ESP32's port (e.g., `'COM3'`).
    *   **On macOS/Linux**, change it to your ESP32's port (e.g., `'/dev/tty.usbserial-XXXX'`).
2.  **Run the Script**:
    Make sure your ESP32 is plugged in and sending data.
    ```bash
    python predict_from_sensor.py
    ```
3.  **Interact with the System**:
    *   The script will display the distance measured by the sensor.
    *   It will then prompt you to **enter an estimated size** for the detected object in meters.
    *   Based on the distance and size, it will predict an alert level (`ALERT`, `beep`, or `none`) and display a corresponding message.
    *   All predictions are logged with a timestamp in `python/results.csv`.

### (Optional) Running the Original Simulation

If you wish to run the original simulation without the hardware, you can use the `main.py` script:
```bash
python main.py
```

## 📄 License
This project is open source and available for educational purposes.