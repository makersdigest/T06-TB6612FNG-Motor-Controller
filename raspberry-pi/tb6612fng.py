##
 # Maker's Digest
 # DC Motor Control with tb6612fng dual h-bridge motor controller
##
from time import sleep      # Import sleep from time
import RPi.GPIO as GPIO     # Import Standard GPIO Module

GPIO.setmode(GPIO.BOARD)      # Set GPIO mode to BCM
GPIO.setwarnings(False);

# PWM Frequency
pwmFreq = 100

# Setup Pins for motor controller
GPIO.setup(12, GPIO.OUT)    # PWMA
GPIO.setup(18, GPIO.OUT)    # AIN2
GPIO.setup(16, GPIO.OUT)    # AIN1
GPIO.setup(22, GPIO.OUT)    # STBY
GPIO.setup(15, GPIO.OUT)    # BIN1
GPIO.setup(13, GPIO.OUT)    # BIN2
GPIO.setup(11, GPIO.OUT)    # PWMB

pwma = GPIO.PWM(12, pwmFreq)    # pin 18 to PWM  
pwmb = GPIO.PWM(11, pwmFreq)    # pin 13 to PWM
pwma.start(100)
pwmb.start(100)

## Functions
###############################################################################
def forward(spd):
    runMotor(0, spd, 0)
    runMotor(1, spd, 0)

def reverse(spd):
    runMotor(0, spd, 1)
    runMotor(1, spd, 1)

def turnLeft(spd):
    runMotor(0, spd, 0)
    runMotor(1, spd, 1)

def turnRight(spd):
    runMotor(0, spd, 1)
    runMotor(1, spd, 0)

def runMotor(motor, spd, direction):
    GPIO.output(22, GPIO.HIGH);
    in1 = GPIO.HIGH
    in2 = GPIO.LOW

    if(direction == 1):
        in1 = GPIO.LOW
        in2 = GPIO.HIGH

    if(motor == 0):
        GPIO.output(16, in1)
        GPIO.output(18, in2)
        pwma.ChangeDutyCycle(spd)
    elif(motor == 1):
        GPIO.output(15, in1)
        GPIO.output(13, in2)
        pwmb.ChangeDutyCycle(spd)


def motorStop():
    GPIO.output(22, GPIO.LOW)

## Main
##############################################################################
def main(args=None):
    while True:
        forward(50)     # run motor forward
        sleep(2)        # ... for 2 seconds
        motorStop()     # ... stop motor
        sleep(.25)      # delay between motor runs

        reverse(50)     # run motor in reverse
        sleep(2)        # ... for 2 seoconds
        motorStop()     # ... stop motor
        sleep(.25)      # delay between motor runs

        turnLeft(50)    # turn Left
        sleep(2)        # ... for 2 seconds
        motorStop()     # ... stop motors
        sleep(.25)      # delay between motor runs

        turnRight(50)   # turn Right
        sleep(2)        # ... for 2 seconds
        motorStop()     # ... stop motors
        sleep(2)        # delay between motor runs

if __name__ == "__main__":
    main()

