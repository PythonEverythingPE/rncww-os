import RPi.GPIO as GPIO
import time
global _pwm_
global buzzer_pwn

front = [12, 26, 14, 20]
back = [16, 19, 13, 21]
left = [14, 26]
right = [12, 20]
TRIG_PIN = 27
ECHO_PIN = 22
SERVO_PIN = 18
PWM_FREQUENCY = 50
PIN_BUZZER = 5
FREQUENCIA_AGUDO = 1500
FREQUENCIA_GRAVE = 1175


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


all_pins = front + back + right + left
for i in all_pins:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)

GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(SERVO_PIN, GPIO.OUT)



GPIO.setup(PIN_BUZZER, GPIO.OUT)
buzzer_pwn = GPIO.PWM(PIN_BUZZER, PWM_FREQUENCY)
_pwm_ = GPIO.PWM(SERVO_PIN, PWM_FREQUENCY)
_pwm_.start(0)
buzzer_pwn.start(0)


