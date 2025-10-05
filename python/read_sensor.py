import serial
import time

# --- IMPORTANT: Change this to your ESP32's port name ---
SERIAL_PORT = 'COM3' 
BAUD_RATE = 115200

try:
    # Open the serial connection
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"Connected to {SERIAL_PORT} at {BAUD_RATE} baud.")
    time.sleep(2) # Wait for the connection to establish

except serial.SerialException as e:
    print(f"Error: Could not open port {SERIAL_PORT}. {e}")
    exit()

# Main loop to read data
while True:
    try:
        # Read one line of data from the ESP32
        line = ser.readline()

        # If a line was actually read
        if line:
            # Decode the bytes into a string and remove whitespace
            line_str = line.decode('utf-8').strip()

            # Split the string by the comma to get distance and speed
            data_parts = line_str.split(',')

            # Make sure we got two parts
            if len(data_parts) == 2:
                distance = float(data_parts[0])
                speed = float(data_parts[1])
                
                print(f"Distance: {distance:.2f} cm, Speed: {speed:.2f} cm/s")

    except KeyboardInterrupt:
        print("\nExiting program.")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        # Continue to the next reading
        pass

# Close the port when the loop is broken
ser.close()
print("Serial port closed.")
