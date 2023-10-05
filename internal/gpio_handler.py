import RPi.GPIO as GPIO

if __name__ == "__main__":
    global _pwm_
    front = [12, 26, 14, 20] 
    back = [16, 19, 13, 21]   
    left = [14, 26]  
    right = [12, 20]
    TRIG_PIN = 27
    ECHO_PIN = 22
    SERVO_PIN = 18
    _pwm_ = None
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    all_pins = front + back + right + left
    for i in all_pins:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.LOW)


    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)
    GPIO.setup(SERVO_PIN, GPIO.OUT)
    _pwm_ = GPIO.PWM(SERVO_PIN, 50)
    PIN_BUZZER = 5
    FREQUENCIA_AGUDO = 1500
    FREQUENCIA_GRAVE = 1175
    GPIO.setup(PIN_BUZZER, GPIO.OUT)
    buzzer_pwn = GPIO.PWM(PIN_BUZZER, 50)
else:
    def get_servo_pwn():
        return _pwm_
    def get_buzzer_pwn():
        return buzzer_pwn
