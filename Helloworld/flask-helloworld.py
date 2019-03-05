#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 20:33:43 2019

@author: calsoft
"""
from flask import Flask, jsonify
import psutil 
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello world 1!"

@app.route("/cpufreq")
def cpu_freq():
    while True:
          return jsonify(psutil.cpu_freq(percpu=True))



if __name__ == "__main__" :
    app.run(host="0.0.0.0",port=8909)


