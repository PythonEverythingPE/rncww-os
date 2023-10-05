import requests
import time
import threading
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
internal_dir = os.path.join(current_dir, "..", "internal")
sys.path.append(internal_dir)
from motors import *
from gpio_handler import *

FREQUENCIA_AGUDO = 1500
FREQUENCIA_GRAVE = 1175


time.sleep(3)
servo(90)
bip(FREQUENCIA_AGUDO)
time.sleep(0.1)
bip(FREQUENCIA_AGUDO)



while True:
            
            move(front)
            
            
            
            distance = get_distance()
            print(distance)
            print(f"Distância: {distance} cm")
            if distance == None:
                    stop()
                    
                    bip(FREQUENCIA_AGUDO)
                    stop()
                    while True:
                        distance = get_distance()
                        bip()
                        time.sleep(0.4)
                        if distance != None:
                            bip()
                            time.sleep(0.1)
                            bip()
                            ALARM = False
                            break
            distance = int(distance)
            
            
           
                    
                    
            
            if distance <= 40:
                bip(FREQUENCIA_AGUDO)
                print(stop())
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
                    
                else:
                    servo(90)
                    move(right)
                    time.sleep(1.25)
                    
                 
    



