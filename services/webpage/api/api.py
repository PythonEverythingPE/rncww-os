from  flask import Flask, jsonify, request, abort, redirect, render_template, Blueprint
import json
from api.gpio import *
import subprocess

api = Blueprint("api", __name__)

@api.route('/move', methods=['POST'])
def move_rt():
    data = request.get_json()
    pins = data["pins"]
    
    if data is None:
        return jsonify({"status": "error", "message": "No data provided"})
    else:
        move(pins)
        return jsonify({"status": "ok", "message": "Moving robot"})
    

@api.route('/stop', methods=['POST'])
def stop_rt():
    
    
    
    
    stop()
    return jsonify({"status": "ok", "message": "Stopping robot"})


@api.route('/services/start', methods=['POST'])
def services_rt():
    data = request.get_json()
    id = data["SERVICE_ID"]

    if data is None:
        return jsonify({"status": "error", "message": "No data provided"})
    else:
        with open("config/services.json", "r") as f:
            data = json.load(f)
            for i in data:
                if i["SERVICE_ID"]:
                    if i["SERVICE_ID"] == id:
                        
                        process = subprocess.Popen(["sudo", "python3.10", i["PATH"]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        for line in iter(process.stdout.readline, b''):
                            print(line.decode("utf-8").strip())
                        return jsonify({"status": "ok", "message": "Starting service"})
    

@api.route('/services/stop', methods=['POST'])
def services_rt():
    data = request.get_json()
    id = data["SERVICE_ID"]

    if data is None:
        return jsonify({"status": "error", "message": "No data provided"})
    else:
        with open("config/services.json", "r") as f:
            data = json.load(f)
            for i in data:
                if i["SERVICE_ID"]:
                    if i["SERVICE_ID"] == id:
                        
                        process = subprocess.Popen(["sudo", "pkill", "-9", "-f", i["PATH"]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        for line in iter(process.stdout.readline, b''):
                            print(line.decode("utf-8").strip())
                        return jsonify({"status": "ok", "message": "Stopping Service"})
    return jsonify({"status": "error", "message": "Something went wrong"})
    


