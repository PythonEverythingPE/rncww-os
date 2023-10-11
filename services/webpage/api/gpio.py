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