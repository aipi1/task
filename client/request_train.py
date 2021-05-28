import requests
import pandas as pd

url = 'http://0.0.0.0:5000/api/train'

X_train = pd.read_csv('X_train.csv')
y_train = pd.read_csv('y_train.csv')
train = pd.concat([X_train, y_train.y], axis = 1)
# Отправка тренировочных данных X,y
train.to_csv('train_data.csv', index = False)
file = {'file': open("train_data.csv", "rb")}
r = requests.post(url, files = file)
# Вывод полученного обратно значения ошибки
print(f'MSE value = {r.text}')