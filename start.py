import os
os.system("sudo python3 internal/gpio_handler.py")

while True:
    try:
        os.system("sudo python3 services/automatic.py")
    except KeyboardInterrupt:
        print("STOP")
        break
    
    
