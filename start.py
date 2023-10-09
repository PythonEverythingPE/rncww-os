import json
import requests
import os
import threading
import time

import subprocess
print("RNCWW | Checking for updates...")
with open("config/os_version.json", "r") as os_version_file:
    os_version = json.load(os_version_file)
    installed_version = os_version["RNCWW-OS_VERSION"]
    print("Installed OS version. " + installed_version)
    

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
    print("Connecting to update server...")
    response = requests.get("https://raw.githubusercontent.com/PythonEverythingPE/rncww-os/main/config/os_version.json")
    if response.status_code == 200:
        print("Connected to update server!")
        version = json.loads(response.text)
        github_version = version["RNCWW-OS_VERSION"]
        print("Latest OS version: " + github_version)
        if installed_version != github_version:
            
            os.system("cd ..")
            
            print("Update found!")
            print("Downloading update...")
            os.system("sudo python3.10 ../updater.py")
            exit
        else:
            def start_service(service):
                process = subprocess.Popen(["sudo", "python3.10", service["PATH"]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                for line in iter(process.stdout.readline, b''):
                    print(line.decode("utf-8").strip())
                        
            print("No updates available")
            print("Starting RNCWW OS...")
            with open("config/services.json", "r") as services:
                services = json.load(services)
                for service in services:
                    print("Service Detected: " + service["SERVICE_ID"])
                    if service["SERVICE_ID"] == "SERVICE_END":
                        exit
                        exit()
                    if service["BOOT_START"]:
                        if service["BOOT_START"] == True:
                            print("Starting " + service["SERVICE_ID"])
                            thread = threading.Thread(target=start_service, args=(service,))
                            thread.start()
                            print("Started " + service["SERVICE_ID"])
                            print()
                    else:
                        print(service["SERVICE_ID"] + " is not set to start on boot! Continuing...")
                        print()
    else:
        print("Unable to connect to update server!")
else:
    def start_service(service):
        process = subprocess.Popen(["sudo", "python3.10", service["PATH"]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for line in iter(process.stdout.readline, b''):
            print(line.decode("utf-8").strip())
    print("Unable to connect to the internet!")
    print("Starting RNCWW OS...")
    with open("config/services.json", "r") as services:
                services = json.load(services)
                for service in services:
                    print("Service Detected: " + service["SERVICE_ID"])
                    if service["SERVICE_ID"] == "SERVICE_END":
                        exit
                        exit()
                    if service["BOOT_START"]:
                        if service["BOOT_START"] == True:
                            print("Starting " + service["SERVICE_ID"])
                            thread = threading.Thread(target=start_service, args=(service,))
                            thread.start()
                            print("Started " + service["SERVICE_ID"])
                            print()
                    else:
                        print(service["SERVICE_ID"] + " is not set to start on boot! Continuing...")
                        print()


exit()