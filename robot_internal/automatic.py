import time
from automatic_conf import *
import json



FREQUENCIA_AGUDO = 1500
FREQUENCIA_GRAVE = 1175


time.sleep(2)
servo(90)
_ = 0

while True:
            with open("config/services.json", "r") as f:
                data = json.load(f)
                for service in data:
                    if "SERVICE_ID" in service and service["SERVICE_ID"] == "AUTOMATIC_ROBOT" and service["SERVICE_STATUS"] == "STOP":
                        service["SERVICE_STATUS"] = "STOPPED"
                        stop()
                        servo(90)
                        long_alarm(FREQUENCIA_AGUDO)
                        exit
                
            
            if _ == 0:
                long_alarm(FREQUENCIA_AGUDO)
                _ = 1
            
            move(front)
            
            
            
            distance = get_distance()
            if distance == None:
                    bip(FREQUENCIA_AGUDO)
                    stop()
                    
                    bip(FREQUENCIA_AGUDO)
                    
                    while True:
                        distance = get_distance()
                        bip(FREQUENCIA_AGUDO)
                        time.sleep(0.4)
                        if distance != None:
                            print("ALERT | Distance is: " + distance + "cm")
                            bip(FREQUENCIA_AGUDO)
                            time.sleep(0.1)
                            bip(FREQUENCIA_AGUDO)
                            
                            break
            distance = int(distance)
            
            
           
                    
                    
            
            if distance <= 40:
                bip(FREQUENCIA_AGUDO)
                stop()
                time.sleep(0.2)
                move(back)
                time.sleep(1)
                stop()

                
                servo(45)
                time.sleep(0.8)
                distance_45 = get_distance()
               
                servo(135)
                time.sleep(0.8)
                distance_135 = get_distance()
                
                
                if distance_45 <= distance_135:
                    servo(90)
                    move(left)
                    time.sleep(1.25)
                    stop()
                    
                else:
                    servo(90)
                    move(right)
                    time.sleep(1.25)
                    stop()
                    
                 


def service_check():
      with open("config/services.json", "r") as f:
                data = json.load(f)
                for service in data:
                    if "SERVICE_ID" in service and service["SERVICE_ID"] == "AUTOMATIC_ROBOT" and service["BOOT_START"] == False:
                        exit