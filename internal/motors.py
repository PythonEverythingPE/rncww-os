import RPi.GPIO as GPIO
import time

front = [12, 26, 14, 20] 
back = [16, 19, 13, 21]   
left = [14, 26]  
right = [12, 20]  
TRIG_PIN = 27
ECHO_PIN = 22
SERVO_PIN = 18
_pwm_ = None

all_pins = front + back + left + right




def move(pinos):
    for pino in all_pins:
        if pino in pinos:
            GPIO.output(pino, GPIO.HIGH)
        else:
            GPIO.output(pino, GPIO.LOW)


def stop():
    for pino in all_pins:

        
            GPIO.output(pino, GPIO.LOW)

