#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 20:33:43 2019
@author: calsoft
"""

from flask_restful import Api,Resource # some class is a resource 
from flask import Flask, jsonify 
from flask import request
app = Flask(__name__)
api = Api(app)

@app.route("/")
def main_page():
    txt = "This is a simple calculator api having following function: \
           Add,Subtract,Multiply,Divide "
    return txt

def check_data(data,func_name):
    if (func_name == "Add" or func_name == "Sub" or func_name == "Mul"):
        if ("x" not in data or "y" not in data):
            return 301
        else:
            return 200
    if (func_name == "Div"):
        if ("x" not in data or "y" not in data):
            return 301
        elif int(data["y"]) == 0:
            return 302
        else:
            return 200
    
class Add(Resource):
      def post (self):
          data = request.get_json()
          a = check_data(data,"Add")
          if (a!=200):
              retjson={
                      'Message'   : "Missing Value" ,
                      'Status'    : a
                      }
              return jsonify(retjson)  

          else:
              x = int(data["x"])
              y = int(data["y"])
              z = x+y
              retz = {
                       'Message'   : z ,
                       'Status'    : 200
           }
          return jsonify(retz)


class Sub(Resource):
      def post (self):
          data = request.get_json()
          a = check_data(data,"Sub")
          if (a!=200):
              retjson={
                      'Message'   : "Missing Value" ,
                      'Status'    : a
                      }
              return jsonify(retjson)  

          else:
              x = int(data["x"])
              y = int(data["y"])
              z = x-y
              retz = {
                       'Message'   : z ,
                       'Status'    : 200
           }
          return jsonify(retz) 

class Mul(Resource):
      def post (self):
          data = request.get_json()
          a = check_data(data,"Mul")
          if (a!=200):
              retjson={
                      'Message'   : "Missing Value" ,
                      'Status'    : a
                      }
              return jsonify(retjson)  

          else:
              x = int(data["x"])
              y = int(data["y"])
              z = x*y
              retz = {
                       'Message'   : z ,
                       'Status'    : 200
           }
          return jsonify(retz)

class Div(Resource):
      def post (self):
          data = request.get_json()
          a = check_data(data,"Div")
          if (a!=200):
              retjson={
                      'Message'   : "Missing Value" ,
                      'Status'    : a
                      }
              return jsonify(retjson)  

          else:
              x = int(data["x"])
              y = int(data["y"])
              z = x/y
              retz = {
                       'Message'   : z ,
                       'Status'    : 200
           }
          return jsonify(retz)

api.add_resource(Add,"/Add")
api.add_resource(Sub,"/Sub")
api.add_resource(Mul,"/Mul")
api.add_resource(Div,"/Div")


if __name__ == "__main__" :
    app.run(host="0.0.0.0",port=8909 ,debug=True)



