##
 # Maker's Digest
 # DC Motor Control with tb6612fng dual h-bridge motor controller
##
from time import sleep      # Import sleep from time
import RPi.GPIO as GPIO     # Import Standard GPIO Module

GPIO.setmode(GPIO.BCM)      # Set GPIO mode to BCM

# PWM Frequency
pwmFreq = 100

# Setup Pins for motor controller
GPIO.setup(18, GPIO.OUT)    # PWMA
GPIO.setup(23, GPIO.OUT)    # AIN2
GPIO.setup(24, GPIO.OUT)    # AIN1
GPIO.setup(25, GPIO.OUT)    # STBY
GPIO.setup(22, GPIO.OUT)    # BIN1
GPIO.setup(27, GPIO.OUT)    # BIN2
GPIO.setup(13, GPIO.OUT)    # PWMB

pwma = GPIO.PWM(18, pwmFreq)    # pin 18 to PWM  
pwmb = GPIO.PWM(13, pwmFreq)    # pin 13 to PWM
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
    GPIO.output(25, GPIO.HIGH);
    in1 = GPIO.HIGH
    in2 = GPIO.LOW

    if(direction == 1):
        in1 = GPIO.LOW
        in2 = GPIO.HIGH

    if(motor == 0):
        GPIO.output(23, in1)
        GPIO.output(24, in2)
        #GPIO.output(18, GPIO.HIGH)
        pwma.ChangeDutyCycle(spd)
    elif(motor == 1):
        GPIO.output(22, in1)
        GPIO.output(27, in2)
        #GPIO.output(17, GPIO.HIGH)
        pwmb.ChangeDutyCycle(spd)


def motorStop():
    GPIO.output(25, GPIO.LOW)
#    if(motor == 0):
#        GPIO.output(23, GPIO.LOW)
#        GPIO.output(24, GPIO.LOW)
#        GPIO.output(18, GPIO.LOW)
#    elif(motor == 1):
#        GPIO.output(22, GPIO.LOW)
#        GPIO.output(27, GPIO.LOW)
#        GPIO.output(17, GPIO.LOW)

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

