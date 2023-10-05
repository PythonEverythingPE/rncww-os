import RPi.GPIO as GPIO
import time
from gpio_handler import get_servo_pwn, get_buzzer_pwn
front = [12, 26, 14, 20] 
back = [16, 19, 13, 21]   
left = [14, 26]  
right = [12, 20]  
TRIG_PIN = 27
ECHO_PIN = 22
SERVO_PIN = 18
_pwm_ = None

all_pins = front + back + left + right

def servo(graus):
    global _pwm_
    _pwm_ = get_servo_pwn()
    
    ciclo_de_trabalho = (graus / 18) + 2  
    if _pwm_ is None:
        
        _pwm_.start(ciclo_de_trabalho)
    else:
        _pwm_.ChangeDutyCycle(ciclo_de_trabalho)
    time.sleep(0.5)  


def move(pinos):
    for pino in all_pins:
        if pino in pinos:
            GPIO.output(pino, GPIO.HIGH)
        else:
            GPIO.output(pino, GPIO.LOW)


def stop():
    for pino in all_pins:

        
            GPIO.output(pino, GPIO.LOW)

def get_distance():
    try:
        GPIO.output(TRIG_PIN, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG_PIN, GPIO.LOW)

        while GPIO.input(ECHO_PIN) == 0:
            pulso_inicio = time.time()

        while GPIO.input(ECHO_PIN) == 1:
            pulso_fim = time.time()

        duracao_pulso = pulso_fim - pulso_inicio

        distancia_cm = (duracao_pulso * 34300) / 2 

        
        return distancia_cm
    except:
        return None

PIN_BUZZER = 5
FREQUENCIA_AGUDO = 1500
FREQUENCIA_GRAVE = 1175


ALARM = False

GPIO.setup(PIN_BUZZER, GPIO.OUT)


pwm =   get_buzzer_pwn()
pwm.start(0)


def bip(frequencia):
    pwm.ChangeFrequency(frequencia)
    pwm.ChangeDutyCycle(50) 
    time.sleep(0.1)  
    pwm.ChangeDutyCycle(0) 

def alarm(frequencia):
    pwm.ChangeFrequency(frequencia)
    pwm.ChangeDutyCycle(50) 
    time.sleep(0.1)  
    pwm.ChangeDutyCycle(0) 


def alarm_thread():
    global ALARM
    ALARM = True

    while ALARM:
        alarm(FREQUENCIA_AGUDO)
        time.sleep(0.1)
        alarm(FREQUENCIA_GRAVE)
        time.sleep(0.1)