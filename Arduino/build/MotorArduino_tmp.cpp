const uint8_t joystickPin = A2;

// Servo command byte from the datasheet
const uint8_t MOVE_SERVO = 0x1E; 

const int servoMin = 818;
const int servoMax = 511;

void setup() {
  Serial.begin(19200);
  // pinMode(joystickPin, INPUT);
  // printf("%d\n", joystickPin);
  // Serial.write(MOVE_SERVO);
  // Serial.write(highByte(0x00));
  // Serial.write(lowByte(0x00));
}

void loop() {
  // printf("%d\n", joystickPin);
    // analogRead reads 10 bit
    uint16_t joystickValue = analogRead(joystickPin);

  // Map the joystick value to the servo position range
  // printf("%d\n", joystickValue);
  uint16_t servoAngle = map(joystickValue, 0, 1023, servoMin, servoMax);

  // printf("%u\n", (unsigned int) joystickValue);
  Serial.write(MOVE_SERVO);
  // Serial.write(highByte(servoAngle));
  Serial.write(lowByte(servoAngle));
  Serial.write(highByte(servoAngle));
  delay(100);
}