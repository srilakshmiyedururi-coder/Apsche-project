from pathlib import Path
import os
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import pickle

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_DIR = BASE_DIR / 'templates'
MODEL_PATH = TEMPLATE_DIR / 'HDI.pkl'

app = Flask(__name__, template_folder=str(TEMPLATE_DIR))

with MODEL_PATH.open('rb') as model_file:
    model = pickle.load(model_file)

@app.route('/') 
def home():
    return render_template('home.html') 

@app.route('/Prediction', methods=['POST', 'GET'])
def prediction():
    return render_template('indexnew.html')

@app.route('/Home', methods=['POST', 'GET'])
def my_home():
    return render_template('home.html')

@app.route('/predict', methods=['POST']) 
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    
    # Matching the exact feature columns your model expects
    features_name = ['LifeExpectancy', 'MeanYearsSchooling', 'ExpectedYearsSchooling', 'GNI perCapita']
    df = pd.DataFrame(features_value, columns=features_name)
    
    output = model.predict(df)
    
    if hasattr(output, "__len__") and len(output.shape) > 1:
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

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)