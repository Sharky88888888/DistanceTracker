#define TRIG 9
#define ECHO 10

void setup() {
  Serial.begin(9600);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
}

void loop() {
  // Send ultrasonic pulse
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  // Measure pulse duration
  long duration = pulseIn(ECHO, HIGH);
  float distance = duration * 0.034 / 2; // distance in cm

  // Send distance over serial
  Serial.println(distance);
  delay(200); // 5 measurements per second
}
