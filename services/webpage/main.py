from flask import Flask, jsonify, request, abort, redirect, render_template, Response, make_response, url_for
import json
import datetime
import timedelta
from api.api import api
import picamera
import io
app = Flask(__name__)
app.register_blueprint(api, url_prefix="/api")
import os
with open("config/users.json", "r") as f:
        users = json.load(f)





@app.route('/')
def index():
    return redirect("/main_pannel")

@app.route("/login")
def login():
    if request.cookies.get("RNCWW_UD") is not None:
        return redirect("/main_pannel", 301)
    return render_template("pages/login.html")
@app.route("/main_pannel")
def render():
    if request.cookies.get("RNCWW_UD") is None:
        return redirect("/login", 301)
    return render_template("pages/index.html", USER_DATA=json.loads(request.cookies.get("RNCWW_UD")))

@app.route("/logout")
def logout():
    response = make_response(redirect("/login"))
    response.set_cookie("RNCWW_UD", "", expires=0)
    return response

@app.route("/settings")
def render_setting():
    if request.cookies.get("RNCWW_UD") is None:
        return redirect("/login", 301)
    return render_template("pages/settings.html", USER_DATA=json.loads(request.cookies.get("RNCWW_UD")))

@app.route("/services")
def services():
    if request.cookies.get("RNCWW_UD") is None:
        return redirect("/login", 301)
    with open("config/services.json", "r") as f:
        services = json.load(f)
        
            
    return render_template("pages/services.html", USER_DATA=json.loads(request.cookies.get("RNCWW_UD")), SERVICES_LIST=services)

@app.route("/services/manual-service")
def manual():
    if request.cookies.get("RNCWW_UD") is None:
        return redirect("/login", 301)
    with open("config/services.json", "r") as f:
        services = json.load(f)
        
            
    return render_template("pages/manual_control.html", USER_DATA=json.loads(request.cookies.get("RNCWW_UD")), SERVICES_LIST=services)
@app.route("/camera")
def render_cameraa():
    if request.cookies.get("RNCWW_UD") is None:
        return redirect("/login", 301)
    return app.send_static_file("pages/camera.html")



def generate_frames():
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 30
        while True:
            stream = io.BytesIO()
            try:
                for _ in camera.capture_continuous(stream, 'jpeg',
                                                   use_video_port=True, quality=10):
                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + stream.getvalue() + b'\r\n')
                    stream.seek(0)
                    stream.truncate()
                    
            except Exception as e:
                print(f"Error capturing frames: {e}")

















@app.route("/verify-login", methods=["POST"])
def verify_login():
    username = request.get_json()["username"]
    password = request.get_json()["password"]
    with open("config/users.json", "r") as f:
        users = json.load(f)
    for user in users:
        if user["USERNAME"] == username:
            if user["PASSWORD"] == password:
                return user["USERNAME"]
    return "FALSE"



@app.route("/callback")
def callback():
    username = request.args.get("user")
    with open("config/users.json", "r") as f:
        users = json.load(f)
    for user in users:
        if user["USERNAME"] == username:
            user_data = user
            
            response = make_response(redirect("/main_pannel"))
            
            response.set_cookie("RNCWW_UD", json.dumps(user_data), expires="")
            return response
    return "User not found"
        

app.run(host="0.0.0.0", port=80, debug=True)

