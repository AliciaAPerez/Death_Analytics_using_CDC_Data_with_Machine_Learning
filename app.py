from flask import Flask, jsonify, render_template, redirect, request, send_from_directory
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
import os
# from test2 import getdata
from aconfig import USER, PASSWORD, ADDRESS, PORT, DATABASE
import collections
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


def confg():
    connection_string = (
        f'postgresql://{USER}:{PASSWORD}@{ADDRESS}:{PORT}/{DATABASE}')
    engine = create_engine(connection_string)
    cn = engine.connect()

    Base = automap_base()
    Base.prepare(engine, reflect=True)
    Base.classes.keys()
    print(Base.classes.keys())
    deaths = Base.classes.leading_causes_death 
    session = Session(engine)

    return Base, deaths, session


@app.route("/data", methods=["GET"])
def test():

    Base, deaths, session = confg()
    deaths = Base.classes.leading_causes_death 
    data = session.query(deaths).all()


    load = []
    for result in data:
        content = {}
        content = {'year': result.year, 
                    'cause': result.cause, 
                    'cause_name': result.cause_name,
                    'state': result.state,
                    'deaths': result.deaths,
                    'age_adjusted_death_rate': result.age_adjusted_death_rate
                    }
                    
        load.append(content)

    
    return jsonify(load)
    print(data)





@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r



if (__name__) == '__main__':
    app.debug = True
    app.run()