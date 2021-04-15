from flask import Flask, jsonify, render_template, redirect, request, send_from_directory
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
import os
# from test2 import getdata
from config import USER, PASSWORD, ADDRESS, PORT, DATABASE
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
    deaths = Base.classes.cdc_death_table
    session = Session(engine)

    return Base, deaths, session


@app.route("/", methods=["GET"])
def test():

    Base, deaths, session = confg()
    deaths = Base.classes.cdc_death_table
    data = session.query(deaths).all()


    load = []
    content = {}
    for result in data:
        content = {'id': result.id,
                'education': result.education,
                'sex': result.sex,
                'age': result.age,
                'race': result.race,
                'hispanic': result.hispanic,
                'marital_status': result.marital_status,
                'month_of_death:': result.month_of_death,
                'day_of_week_of_death': result.day_of_week_of_death,
                'current_data_year': result.current_data_year,
                'manner_of_death': result.manner_of_death,
                'current_data_year': result.current_data_year,
                'icd_death_code': result.icd_death_code,
                'entity_condition_1': result.entity_condition_1,
                'entity_condition_2': result.entity_condition_2,
                'entity_condition_3': result.entity_condition_3

                }

        load.append(content)
        content = {}
    return load


if (__name__) == '__main__':
    app.debug = True
    app.run()
