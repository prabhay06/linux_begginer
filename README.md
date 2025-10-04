# Haptic Awareness System

A beginner-friendly machine learning project for haptic awareness system using Python.

## Project Description

This project implements a haptic awareness system that uses machine learning to detect and classify haptic patterns. It's designed to be beginner-friendly and educational for those learning Python and machine learning basics.

## Project Modules

The project consists of the following modules:

- **data_simulator.py** - Simulates haptic sensor data for training and testing
- **train_model.py** - Trains the machine learning model using the simulated data
- **main.py** - Main application entry point for running the haptic awareness system

## Installation and Setup (Windows)

Follow these step-by-step instructions to set up and run the project on Windows:

### Step 1: Clone the Repository

```bash
git clone https://github.com/prabhay06/linux_begginer.git
cd linux_begginer/haptic_awareness_system
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

```bash
venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
python main.py
```

## Usage Notes

- Make sure you have Python 3.7 or higher installed on your system
- Keep the virtual environment activated while working with the project
- If you encounter any issues with dependencies, try upgrading pip: `python -m pip install --upgrade pip`
- The data simulator generates synthetic data for training purposes
- Model training may take a few minutes depending on your system specifications

## Deactivating the Virtual Environment

When you're done working on the project, deactivate the virtual environment:

```bash
deactivate
```

## License

This project is open source and available for educational purposes.
