from flask import Flask, jsonify, request, abort, redirect, render_template
import json
from api.api import api
app = Flask(__name__)
app.register_blueprint(api, url_prefix="/api")
@app.route('/')
def index():
    return "oi"

@app.before_request
def before_request():
    if request.path.startswith("/static") or request.method == "POST" or request.path.startswith("/api"):
        return None
    with open("config\services.json", "r") as f:
        data = json.load(f)
        for i in data:
            if "SERVICE_STATUS" in i and i["GLOBAL_SERVICE_STATUS"] == "OFF":
                return render_template("/system/starting.html")
            if "SERVICE_STATUS" in i and i["GLOBAL_SERVICE_STATUS"] == "UPDATING":
                return render_template("/system/updating.html")
            
    return None
    
app.run(host="0.0.0.0", port=80, debug=True)