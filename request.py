import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'age': 40, 'trestbps':120, 'chol':350, 'thalach':127, 'oldpeak' :3.1})




print(r.json())