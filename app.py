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
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from keras.models import load_model
death_model = load_model('death_machine_keras10.h5')

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

from flask_sqlalchemy import SQLAlchemy
# DATABASE_URL will contain the database connection string:
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
# Connects to the database using the app config
db = SQLAlchemy(app)


##Routes for the jsonified data ////////////////////////////////////////////////////////////////////////////////////////////////
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

#Making the heart disease prediction model /////////////////////////////////////////////////////////////////////////////////////////////////
# Hear Disease model
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))


@app.route('/prediction')
def prediction():
    return render_template('model.html')

@app.route('/predict',methods=['POST'])
def predict():

    model = pickle.load(open('model.pkl', 'rb'))
    scaler = pickle.load(open('scaler.pkl', 'rb'))

    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    final_features = scaler.transform(final_features)    
    prediction = model.predict(final_features)
    print("final features",final_features)
    print("prediction:",prediction)
    output = round(prediction[0], 2)
    print(output)
    # console.log(output)

    if output == 0:
        return render_template('model.html', prediction_text='NOT LIKELY TO HAVE HEART DISEASE')
    else:
        return render_template('model.html', prediction_text='LIKELY TO HAVE HEART DISEASE')
        
@app.route('/predict_api',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)
    print(output)

# ////////////////////////////////////////////////
@app.route('/causes',methods=['GET','POST'])
def causes():
#     data = [float(x) for x in request.form.values()]
#     death_model = load_model('death_machine_keras10.h5')
#     # model = self.death_model()
#     results = death_model.predict([np.array(list(data.values()))])
#     output = results[0]
    model = pickle.load(open('clf_death_model2.pkl', 'rb'))
    # scaler = pickle.load(open('scaler.pkl', 'rb'))

    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    final_features = scaler.transform(final_features)    
    prediction = model.predict(final_features)
    print("final features",final_features)
    print("prediction:",prediction)
    # output = round(prediction[0], 2)
    # print(output)
    # console.log(output)
    return render_template('deathmachine.html', prediction_text= f"Code: {prediction} Please see Legend Below")
        

    # params = flask.request.json
    # if (params == None):
    #     params = flask.request.args

    # if (params != None):
    #     x=pd.DataFrame.from(params, orient='index').transpose():
    #         data["prediction"] = str(death_model.predict()[0][0])
    #         data["success"] = True

    # return flask.jsonify(data)

    # death_model = load_model('death_machine_keras10.h5')
    # features = request.form.values()
    # features = [float(x) for x in request.form.values()]
    # final_features = [np.array(features)]
    # final_features = scaler.transform(final_features)    
    # prediction = model().predict(final_features)
    # print(features)
    # print(final_features)
    # print(prediction)
    # return features
    # return render_template('deathmachine.html', prediction_text= f"Code: {output} Please see Legend Below")


#Creating routes for to return the html//////////////////////////////////////////////////////////////////////////////////////////


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index2")
def index2():
    return render_template("index2.html")

@app.route("/index3")
def index3():
    return render_template("index3.html")

@app.route("/index4")
def index4():
    return render_template("index4.html")

@app.route("/index5")
def index5():
    return render_template("index5.html")

@app.route("/index6")
def index6():
    return render_template("index6.html")    

@app.route("/index7")
def index7():
    return render_template("index7.html")

@app.route("/index8")
def index8():
    return render_template("index8.html")      

@app.route("/index9")
def index9():
    return render_template("index9.html")      

@app.route("/index10")
def index10():
    return render_template("index10.html")    


@app.route("/deathmachine")
def machine():

    return render_template("deathmachine.html")

@app.route("/model")
def model():
    return render_template("model.html")



# @app.route('/static/<path:path>')
# def send_js(path):
#     return send_from_directory('static', path)


# @app.after_request
# def add_header(r):
#     """
#     Add headers to both force latest IE rendering engine or Chrome Frame,
#     and also to cache the rendered page for 10 minutes.
#     """
#     r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     r.headers["Pragma"] = "no-cache"
#     r.headers["Expires"] = "0"
#     r.headers['Cache-Control'] = 'public, max-age=0'
#     return 
    
if (__name__) == '__main__':
    app.debug = True
    app.run()
