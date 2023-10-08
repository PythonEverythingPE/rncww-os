from  flask import Flask, jsonify, request, abort, redirect, render_template, Blueprint
import json
from gpio import *

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


@api.route('/services', methods=['POST'])
def services_rt():
    data = request.get_json()
    id = data["id"]
    new_status = data["status"]
    
    if data is None:
        return jsonify({"status": "error", "message": "No data provided"})
    else:
        with open("....../config/services.json", "r") as f:
            data = json.load(f)
            for i in data:
                if i["SERVICE_ID"] == id:
                    if i["SERVICE_ID"] == id:
                        i["SERVICE_STATUS"] = new_status
        return jsonify({"status": "ok", "message": "Set service status"})
    

