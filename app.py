
import base64
import json
from io import BytesIO

import numpy as np
import requests
from flask import Flask, request, jsonify

# from flask_cors import CORS

app = Flask(__name__)


# Testing URL
@app.route('/healthy/', methods=['GET', 'POST'])
def hello_world():
    return 'good bye'

@app.route('/whereami/', methods=['GET'])
def where_am_i():
    return 'hall 15'