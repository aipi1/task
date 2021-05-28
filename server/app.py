from flask import Flask, request, jsonify
import numpy as np
import pickle
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from os import path

app = Flask(__name__)
# Обучение модели
@app.route('/api/train', methods=['POST'])
def train_model():
    # Получение и загрузка файла с X и y
    file = request.files['file']
    data = pd.read_csv(file, parse_dates = ['date'])
    # Подготовка данных
    data.sort_values(by = 'date', inplace = True, ascending = True)
    data.set_index('date', inplace = True)
    y = data.y.copy()
    X = data.drop('y', axis = 1).copy()
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, shuffle = False)
    # Обучение модели и расчет ошибки
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    loss = mean_squared_error(y_test, preds)
    # Обучение модели на полном сете и обновление файла с моделью pickle
    model.fit(X, y)
    pickle.dump(model, open(modelfile, 'wb'))
    return jsonify(loss)
# Расчет модели
@app.route('/api/predict', methods=['POST'])
def get_predictions():
    # Получение и загрузка файла с X
    file = request.files['file']
    data = pd.read_csv(file, parse_dates = ['date'])
    data.set_index('date', inplace = True)    
    # Формирование и отправка прогнозов для значений y
    predictions = pd.DataFrame({'date': data.index, 'prediction': model.predict(data)})
    return jsonify(predictions.to_dict(orient = 'records'))
# Начало работы
if __name__ == '__main__':
    # Загрузка модели и запуск приложения
    modelfile = path.join(app.root_path, 'model.pickle')
    model = pickle.load(open(modelfile, 'rb'))
    app.run(debug = True, host = '0.0.0.0')