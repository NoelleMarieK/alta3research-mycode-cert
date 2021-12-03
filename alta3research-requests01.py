#!/usr/bin/python3

import json
import html
from flask import Flask
from flask import redirect
from flask import request
from flask import render_template, jsonify

app = Flask(__name__)

coin_data=[]

# read file
with open('./assets.json', 'r') as f:
    coin_data = json.loads(f.read())

@app.route("/")
def index():
    return jsonify(coin_data)


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
