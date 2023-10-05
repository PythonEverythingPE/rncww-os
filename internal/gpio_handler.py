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

# Inicialize a biblioteca RPi.GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Configurar os pinos GPIO
all_pins = front + back + right + left
for i in all_pins:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)

GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(SERVO_PIN, GPIO.OUT)
_pwm_ = GPIO.PWM(SERVO_PIN, PWM_FREQUENCY)

# Configurar o buzzer
GPIO.setup(PIN_BUZZER, GPIO.OUT)
buzzer_pwn = GPIO.PWM(PIN_BUZZER, PWM_FREQUENCY)

pwm = buzzer_pwn
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

def servo(graus):
    
    
    ciclo_de_trabalho = (graus / 18) + 2  
    if _pwm_ is None:
        
        _pwm_.start(ciclo_de_trabalho)
    else:
        _pwm_.ChangeDutyCycle(ciclo_de_trabalho)
    

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