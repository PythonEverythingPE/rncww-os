from flask import Flask, jsonify, request, abort, redirect
from ...robot_internal import *
app = Flask(__name__)
app.secret_key = 'secret_key'

app.run(host="0.0.0.0", port=1008, debug=True)