// Define the trigger and echo pins for the HC-SR04 sensor
const int trigPin = 5;
const int echoPin = 18;

// Define sound speed in cm/uS
#define SOUND_SPEED 0.034

// Variables for duration and distance
long duration;
float distanceCm;

void setup() {
  // Begin serial communication at a baud rate of 9600
  Serial.begin(9600);

  // Set the pin modes for the trigger and echo pins
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  // Clear the trigPin by setting it to LOW
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // Trigger the sensor by setting the trigPin to HIGH for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read the echoPin, which returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);

  // Calculate the distance in centimeters
  distanceCm = duration * SOUND_SPEED / 2;

  // Print the distance to the Serial Monitor
  Serial.println(distanceCm);

  // Wait for 500 milliseconds before the next reading
  delay(500);
}