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