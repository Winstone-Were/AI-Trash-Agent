#define PIR_PIN 4       // GPIO pin for the HC-SR501 PIR sensor output
#define LED_RED 2       // GPIO pin for red LED
#define LED_GREEN 15    // GPIO pin for green LED

void setup() {
  pinMode(PIR_PIN, INPUT);       // PIR sensor as input
  pinMode(LED_RED, OUTPUT);      // Red LED as output
  pinMode(LED_GREEN, OUTPUT);    // Green LED as output
  Serial.begin(115200);          // Serial communication
}

void loop() {
  int motionDetected = digitalRead(PIR_PIN);  // Read PIR sensor state

  if (motionDetected == HIGH) {  // Check if motion is detected
    if (Serial.available()) {
      String input = Serial.readStringUntil('\n');  // Read the message from Python
      if (input == "RED") {
        digitalWrite(LED_RED, HIGH);   // Turn on red LED
        digitalWrite(LED_GREEN, LOW); // Turn off green LED
      } else if (input == "GREEN") {
        digitalWrite(LED_RED, LOW);    // Turn off red LED
        digitalWrite(LED_GREEN, HIGH); // Turn on green LED
      }
    }
  } else {
    // Turn off both LEDs if no motion is detected
    digitalWrite(LED_RED, LOW);
    digitalWrite(LED_GREEN, LOW);
  }
}
