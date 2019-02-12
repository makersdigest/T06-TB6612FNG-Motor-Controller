/*
 * Maker's Digest
 *
 * DC Motor control using the tb6612fng dual h-bridge motor
 * controller
 * 
 * In this example I have created some functions for you to
 * examine and use. They will drive a bot forward, reverse
 * left turn and right turn. It can look compilcated, but the 
 * absolute minumum you need to run a motor in the loop are 
 * these three commands:
 * 
 * analogWrite(pwmPin, 128); // Value from 0 - 255 for speed.
 * digitalWrite(dirPin1, HIGH);
 * digitalWrite(dirPin2, LOW);
 * 
 * analogWrite(pwmPin, val) tells the motor what speed to run.
 * 
 * the two digitalWrite() commands need to be HIGH AND LOW. This
 * determines the direction. Just flip the values of HIGH and
 * LOW to reverse the direction
 */

// Setup pins
int standBy = 10;

// Motor A
int PWMA = 3;   // PWM Speed Control
int AIN1 = 9;   // Direction pin 1
int AIN2 = 8;   // Direction pin 2

// Motor B
int PWMB = 5;   // PWM Speed Control
int BIN1 = 11;  // Direction pin 1
int BIN2 = 12;  // Direction pin 2

void setup() {

  // Setup Pins as OUTPUT
  pinMode(standBy, OUTPUT);

  // Motor A
  pinMode(PWMA, OUTPUT);
  pinMode(AIN1, OUTPUT);
  pinMode(AIN2, OUTPUT);

  // Motor B
  pinMode(PWMB, OUTPUT);
  pinMode(BIN1, OUTPUT);
  pinMode(BIN2, OUTPUT);

  Serial.begin(19200);
  Serial.println("Makers Digest: Ready");
}

void loop() {
  forward(128);   // Move forward
  delay(2000);    // ... for 2 seconds
  stop();         // ... Stop the motors
  delay(250);     // Delay between motor runs.
  
  reverse(255);   // Move in reverse
  delay(2000);    // ... for 2 seconds
  stop();         // ... Stop the Motors
  delay(250);     // Delay between motor runs.

  turnLeft(64);   // Turn Left
  delay(2000);    // ... for 2 seconds
  stop();         // ... stop the motors
  delay(250);     // Delay between motor runs.

  turnRight(255); // Turn Right
  delay(2000);    // ... for 2 seconds
  stop();         // ... stop the motors
  delay(2000);    // Delay between motor runs.
}

/*
 * Functions
 * *****************************************************
 */

void turnLeft(int spd)
{
  runMotor(0, spd, 0);
  runMotor(1, spd, 1);
}

void turnRight(int spd)
{
  runMotor(0, spd, 1);
  runMotor(1, spd, 0);
}

void forward(int spd) 
{
  runMotor(0, spd, 0);
  runMotor(1, spd, 0);
}

void reverse(int spd)
{
  runMotor(0, spd, 1);
  runMotor(1, spd, 1);
}

void runMotor(int motor, int spd, int dir)
{
  digitalWrite(standBy, HIGH); // Turn on Motor

  boolean dirPin1 = LOW;
  boolean dirPin2 = HIGH;

  if(dir == 1) {
    dirPin1 = HIGH;
    dirPin2 = LOW;
  }

  if(motor == 1) {
    digitalWrite(AIN1, dirPin1);
    digitalWrite(AIN2, dirPin2);
    analogWrite(PWMA, spd);
  } else {
    digitalWrite(BIN1, dirPin1);
    digitalWrite(BIN2, dirPin2);
    analogWrite(PWMB, spd);
  }
  
}

void stop() {
  digitalWrite(standBy, LOW);
}
