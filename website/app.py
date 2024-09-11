from flask import Flask, request
import joblib
import numpy as np
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# Load the model
model = joblib.load('website\model.pkl')

@app.route('/predict', methods=['POST','GET'])
def predict():
    # Get specific form values
    in1 = request.form['in1']
    in2 = request.form['in2'] 
    in3 = request.form['in3']
    in4 = request.form['in4']
    in5 = request.form['in5']
    cb1 = 1 if request.form.get('cb1', False) == 'on' else 0
    cb2 = 1 if request.form.get('cb2', False) == 'on' else 0
    cb3 = 1 if request.form.get('cb3', False) == 'on' else 0
    cb4 = 1 if request.form.get('cb4', False) == 'on' else 0
    cb5 = 1 if request.form.get('cb5', False) == 'on' else 0
    cb6 = 1 if request.form.get('cb6', False) == 'on' else 0

    # Convert to a 2D array
    final = [in1, in2, in3, in4, in5, cb1, cb2, cb3, cb4, cb5, cb6]
    final = [int(i) for i in final]
    print('final:',final)
    # Make a prediction
    pred = model.predict([final])
    pred = pred[0]
    print('Prediction:',pred)
    return render_template('home.html', prediction=np.round(pred*100, 2))

if __name__ == '__main__':
    app.run(port=5500, debug=True)