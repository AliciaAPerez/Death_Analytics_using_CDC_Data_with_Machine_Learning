from flask import Flask, jsonify, render_template, redirect, request, send_from_directory
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
import os
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
def confg():
    engine = create_engine(
        'postgres://xyapznezeaqswq:563af6f1a293c52937083ed16940c84d274b616f8e2202c9cd74c95ae39916b8@ec2-52-21-252-142.compute-1.amazonaws.com:5432/d4g7j0al3kor5t')
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    Base.classes.keys()
    arrivals = Base.classes.clean_arrivals
    revenues = Base.classes.clean_revenues
    session = Session(engine)
    return Base, arrivals, revenues, session
@app.route("/tourism_arr", methods=["GET"])
def handler_arrival_data():
    Base, arrivals, revenues, session = confg()
    arrivals = Base.classes.clean_arrivals
    arrival = session.query(arrivals).all()
    features = []
    for i in arrival:
        feature_dict = {}
        feature_dict['type'] = 'Feature'
        feature_dict['geometry'] = {
            'type': 'Point',
            'coordinates': [(i.longitude), (i.latitude)]
        }
        feature_dict['death'] = {
            'country': i.country,
            'country_code': i.country_code,
            "1995": float(i.total_arrivals_1995),
            
        }
        features.append(feature_dict)
    arrivals_dict = {}
    arrivals_dict['type'] = 'FeatureCollection'
    arrivals_dict['features'] = features
    return arrivals_dict
@app.route("", methods=[""])
def handler_revenue_data():
    Base, arrivals, revenues, session = confg()
    revenues = Base.classes.clean_revenues
    revenue = session.query(revenues).all()
    features = []
    for i in revenue:
        feature_dict = {}
        feature_dict['type'] = 'Feature'
        feature_dict['geometry'] = {
            'type': 'Point',
            'coordinates': [(i.longitude), (i.latitude)]
        }
        feature_dict['properties'] = {
            'country': i.country,
            'country_code': i.country_code,
            "1995": float(i.total_revenues_1995),
            
        }
        features.append(feature_dict)
    revenues_dict = {}
    revenues_dict['type'] = 'FeatureCollection'
    revenues_dict['features'] = features
    return revenues_dict
@app.route("/country_arrival_2019", methods=["GET"])
def handler_arrival_country_2019():
    Base, arrivals, revenues, session = confg()
    arrival = session.query(arrivals).all()
    country_arrival_2019={"arrival_2019": [],
    "country":[]}
    for person in arrival:
        country_arrival_2019["arrival_2019"].append(float(person.total_arrivals_2019))
        country_arrival_2019["country"].append(person.country)
    return country_arrival_2019
@app.route("/country_arrival_2009", methods=["GET"])
def handler_arrival_country_2009():
    Base, arrivals, revenues, session = confg()
    arrival = session.query(arrivals).all()
    country_arrival_2009={"arrival_2009": [],
    "country":[]}
    for person in arrival:
        country_arrival_2009["arrival_2009"].append(float(person.total_arrivals_2009))
        country_arrival_2009["country"].append(person.country)
    return country_arrival_2009
@app.route("/country_revenue_2019", methods=["GET"])
def handler_revenue_country_2019():
    Base, arrivals, revenues, session = confg()
    revenue = session.query(revenues).all()
    country_revenue_2019={"revenue_2019": [],
    "country":[]}
    for person in revenue:
        country_revenue_2019["revenue_2019"].append(float(person.total_revenues_2019))
        country_revenue_2019["country"].append(person.country)
    return country_revenue_2019
@app.route("/country_revenue_2009", methods=["GET"])
def handler_revenue_country_2009():
    Base, arrivals, revenues, session = confg()
    revenue = session.query(revenues).all()
    country_revenue_2009={"revenue_2009": [],
    "country":[]}
    for person in revenue:
        country_revenue_2009["revenue_2009"].append(float(person.total_revenues_2009))
        country_revenue_2009["country"].append(person.country)
    return country_revenue_2009
@app.route("/arrivals_map")
def arrivals():
    return render_template("index_arrivals.html")
@app.route("/revenues_map")
def revenues():
    return render_template("index_revenues.html")
@app.route("/arrival_plotly")
def plotly_2019_2009():
    return render_template("plotly_arrival.html")
@app.route("/revenue_plotly")
def map_2019_2009():
    return render_template("plotly_revenue.html")
@app.route("/")
def index():
    return render_template("index.html")
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