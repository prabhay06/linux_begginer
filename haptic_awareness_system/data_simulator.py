import pandas as pd
import numpy as np

def generate_data(num_samples=1000):
    """Generates simulated data for blind spot detection."""
    # Seed for reproducibility
    np.random.seed(42)

    # Generate random data for distance (in meters) and size (in meters)
    distance = np.random.uniform(0.5, 10, num_samples)
    size = np.random.uniform(0.1, 3, num_samples)

    # Determine alert level based on rules
    alert_level = []
    for d, s in zip(distance, size):
        if d < 2 and s > 1.5:
            alert_level.append('ALERT')
        elif d < 5 and s > 0.5:
            alert_level.append('beep')
        else:
            alert_level.append('none')

    # Create a DataFrame
    df = pd.DataFrame({
        'distance': distance,
        'size': size,
        'alert_level': alert_level
    })

    return df

if __name__ == "__main__":
    data = generate_data()
    data.to_csv('haptic_awareness_system/simulated_data.csv', index=False)
    print("Simulated data generated and saved to 'haptic_awareness_system/simulated_data.csv'")