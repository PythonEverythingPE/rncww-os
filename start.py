import os
import time
os.system("sudo python3 internal/gpio_handler.py")

time.sleep(1)
os.system("sudo python3 internal/automatic_service.py")

    
