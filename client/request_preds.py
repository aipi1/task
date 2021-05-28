import requests
import pandas as pd
from json import loads

url = 'http://0.0.0.0:5000/api/predict'

file = {'file': open("X_test.csv", "rb")}
# Отправка файла со значениями X и получение прогнозов для y
r = requests.post(url, files = file)
predictions = pd.DataFrame.from_dict(loads(r.text))
predictions['date'] = pd.read_csv('X_test.csv', parse_dates = ['date']).date
predictions.to_csv('predictions.csv', index = False)
print('Success!')