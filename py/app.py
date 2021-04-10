from flask import Flask, jsonify, render_template, redirect, request, send_from_directory
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
import os
from test2 import getdata
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
# def config():
    #engine = create_engine(
        #'postgres://xyapznezeaqswq:563af6f1a293c52937083ed16940c84d274b616f8e2202c9cd74c95ae39916b8@ec2-52-21-252-142.compute-1.amazonaws.com:5432/d4g7j0al3kor5t')
@app.route("/test")   
def test(): 
    return getdata()
if (__name__) == '__main__':
    app.debug = True
    app.run()