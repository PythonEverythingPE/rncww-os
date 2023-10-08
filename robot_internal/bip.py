import RPi.GPIO as GPIO
import time
front = [12, 26, 14, 20] 
back = [16, 19, 13, 21]   
left = [14, 26]  
right = [12, 20]  
TRIG_PIN = 27
ECHO_PIN = 22
SERVO_PIN = 18
TRIG_PIN = 27
ECHO_PIN = 22
SERVO_PIN = 18
PWM_FREQUENCY = 50
PIN_BUZZER = 5
FREQUENCIA_AGUDO = 1500
FREQUENCIA_GRAVE = 1175
global _pwm_
global buzzer_pwn
_pwm_ = None
from robot_internal.gpio_setup import  buzzer_pwn

def bip(frequencia):
    pwm =  buzzer_pwn
    pwm.ChangeFrequency(frequencia)
    pwm.ChangeDutyCycle(50) 
    time.sleep(0.1)  
    pwm.ChangeDutyCycle(0) 

def long_alarm(frequencia):
    pwm =  buzzer_pwn
    pwm.ChangeFrequency(frequencia)
    pwm.ChangeDutyCycle(50) 
    time.sleep(5)  
    pwm.ChangeDutyCycle(0)






