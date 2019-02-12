from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Setup Pins for motor controller

GPIO.setup(18, GPIO.OUT)    # PWMA
GPIO.setup(23, GPIO.OUT)    # AIN2
GPIO.setup(24, GPIO.OUT)    # AIN1
GPIO.setup(25, GPIO.OUT)    # STBY
GPIO.setup(22, GPIO.OUT)    # BIN1
GPIO.setup(27, GPIO.OUT)    # BIN2
GPIO.setup(17, GPIO.OUT)    # PWMB

# PWM Frequency
pwmFreq = 100

def motorMove(motor, spd, direction):
    in1 = GPIO.HIGH
    in2 = GPIO.LOW

    if(direction == 1):
        in1 = GPIO.LOW
        in2 = GPIO.HIGH

    if(motor == 0):
        GPIO.output(23, in1)
        GPIO.output(24, in2)
        GPIO.output(18, GPIO.HIGH)
    elif(motor == 1):
        GPIO.output(22, in1)
        GPIO.output(27, in2)
        GPIO.output(17, GPIO.HIGH)


def motorStop(motor):
    if(motor == 0):
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
    elif(motor == 1):
        GPIO.output(22, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)


motorMove(0, 255, 0)
motorMove(1, 255, 0)
sleep(3)
motorStop(0)
motorStop(1)
sleep(1)
motorMove(0, 255, 1)
motorMove(1, 255, 1)
sleep(3)
motorStop(0)
motorStop(1)



# Clockwise

#GPIO.output(23, GPIO.HIGH)
#GPIO.output(24, GPIO.LOW)

#GPIO.output(22, GPIO.HIGH)
#GPIO.output(27, GPIO.LOW)

#GPIO.output(18, GPIO.HIGH)
#GPIO.output(17, GPIO.HIGH)

#GPIO.output(25, GPIO.HIGH)

#sleep(5)

