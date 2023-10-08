import json
import requests
import os
from robot_internal.gpio_setup import *
from robot_internal.gpio_config import *
print("Checking for updates...")
with open("config/os-version.json") as os_version_file:
    os_version = json.load(os_version_file)
    version = os_version["RNCWW-OS_VERSION"]

def is_connected():
    try:
        
        response = requests.get("https://www.google.com")
        
        if response.status_code == 200:
            return True
    except:
        pass
    return False

if is_connected():
    print("Connected to the internet!")
    print("Checking for updates...")
    response = requests.get("https://raw.githubusercontent.com/RNCWW/RNCWW-OS/main/config/os-version.json")
    if response.status_code == 200:
        
        if os_version["RNCWW-OS_VERSION"] != version:
            os.system("cd ..")
            bip(FREQUENCIA_AGUDO)
            time.sleep(0.1)
            bip(FREQUENCIA_GRAVE)
            time.sleep(0.1)
            bip(FREQUENCIA_AGUDO)
            time.sleep(0.1)
            bip(FREQUENCIA_GRAVE)
            time.sleep(0.1)
            bip(FREQUENCIA_AGUDO)
            time.sleep(0.1)
            bip(FREQUENCIA_GRAVE)
            time.sleep(0.1)
            print("Update found!")
            print("Downloading update...")
            os.system("cd ..")
            os.system("sudo rm -rf rncww-os")
            os.system("sudo git clone https://github.com/PythonEverythingPE/rncww-os.git")
            print("Update Downloaded!")
            print("Installing requirements...")
            os.system("cd rncww-os")
            os.system("sudo python3.10 -m pip install -r requirements.txt")
            print("Requirements installed!")
            print("Restarting with update...")
            os.system("sudo reboot")
        else:
            print("No updates found!")
            print("Starting RNCWW OS...")
            with open("config/services.json") as services:
                services = json.load(services)
                for service in services:
                    print("Service Detected: " + service["SERVICE_ID"])
                    if service["BOOT_START"] == True:
                        print("Starting " + service["SERVICE_ID"])
                        os.system("sudo python3.10 -m " + service["PATH"])
                        print("Started " + service["SERVICE_ID"])
                    else:
                        print( service["SERVICE_ID"] + " is not set to start on boot! Continuing...")
                        print
                
            