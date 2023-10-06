import requests
import time
import threading
import os
import sys
from gpio_config import *


FREQUENCIA_AGUDO = 1500
FREQUENCIA_GRAVE = 1175


time.sleep(2)
servo(90)
long_alarm(FREQUENCIA_AGUDO)

while True:
            
            move(front)
            
            
            
            distance = get_distance()
            if distance == None:
                    stop()
                    
                    bip(FREQUENCIA_AGUDO)
                    
                    while True:
                        distance = get_distance()
                        bip(FREQUENCIA_AGUDO)
                        time.sleep(0.4)
                        if distance != None:
                            bip(FREQUENCIA_AGUDO)
                            time.sleep(0.1)
                            bip(FREQUENCIA_AGUDO)
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
                    
                 
    



