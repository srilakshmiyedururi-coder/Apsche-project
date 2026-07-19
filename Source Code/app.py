from pathlib import Path
import os
import numpy as np
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
import pickle

PROJECT_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = PROJECT_ROOT / 'Templates'
STATIC_DIR = PROJECT_ROOT / 'Static'
MODEL_PATH = PROJECT_ROOT / 'Models' / 'HDI.pkl'

app = Flask(__name__, template_folder=str(TEMPLATE_DIR), static_folder=str(STATIC_DIR), static_url_path='/static')

with MODEL_PATH.open('rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return redirect(url_for('demo_home'))

@app.route('/demo')
def demo_home():
    return render_template('home.html')

@app.route('/demo/Prediction', methods=['POST', 'GET'])
def demo_prediction():
    return render_template('indexnew.html')

@app.route('/demo/Home', methods=['POST', 'GET'])
def demo_my_home():
    return render_template('home.html')

@app.route('/demo/predict', methods=['POST'])
def demo_predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    features_name = ['LifeExpectancy', 'MeanYearsSchooling', 'ExpectedYearsSchooling', 'GNI perCapita']
    df = pd.DataFrame(features_value, columns=features_name)
    output = model.predict(df)

    if hasattr(output, '__len__') and len(output.shape) > 1:
        y_pred = round(output[0][0], 2)
    else:
        y_pred = round(output[0], 2)

    if y_pred >= 0.3 and y_pred <= 0.4:
        return render_template('resultnew.html', prediction_text='Low HDI: ' + str(y_pred))
    elif y_pred > 0.4 and y_pred <= 0.7:
        return render_template('resultnew.html', prediction_text='Medium HDI: ' + str(y_pred))
    elif y_pred > 0.7 and y_pred <= 0.8:
        return render_template('resultnew.html', prediction_text='High HDI: ' + str(y_pred))
    elif y_pred > 0.8 and y_pred <= 0.94:
        return render_template('resultnew.html', prediction_text='Very High HDI: ' + str(y_pred))
    else:
        return render_template('resultnew.html', prediction_text='The given values do not match the range of values: ' + str(y_pred))

@app.route('/Prediction', methods=['POST', 'GET'])
def prediction():
    return redirect(url_for('demo_prediction'))

@app.route('/Home', methods=['POST', 'GET'])
def my_home():
    return redirect(url_for('demo_home'))

@app.route('/predict', methods=['POST'])
def predict():
    return demo_predict()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
