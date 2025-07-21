import flask
from flask import Flask, request, jsonify, render_template
import os
import numpy as np  
import pandas as pd
from ml_project.pipeline.prediction import PredictionPipeline 

app = Flask(__name__)  # Initialize Flask app

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/train", methods=['GET'])
def train():
    os.system("python main.py")
    return jsonify({"message": "Training completed successfully!"})


@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get input data from the User Form

            fixed_acidity = float(request.form.get('fixed_acidity'))
            volatile_acidity = float(request.form.get('volatile_acidity'))
            citric_acid = float(request.form.get('citric_acid'))
            residual_sugar = float(request.form.get('residual_sugar'))
            chlorides = float(request.form.get('chlorides'))
            free_sulfur_dioxide = float(request.form.get('free_sulfur_dioxide'))
            total_sulfur_dioxide = float(request.form.get('total_sulfur_dioxide'))
            density = float(request.form.get('density'))
            pH = float(request.form.get('pH'))
            sulphates = float(request.form.get('sulphates'))
            alcohol = float(request.form.get('alcohol'))

            data = {
                'fixed_acidity': fixed_acidity,
                'volatile_acidity': volatile_acidity,
                'citric_acid': citric_acid,
                'residual_sugar': residual_sugar,
                'chlorides': chlorides,
                'free_sulfur_dioxide': free_sulfur_dioxide,
                'total_sulfur_dioxide': total_sulfur_dioxide,
                'density': density,
                'pH': pH,
                'sulphates': sulphates,
                'alcohol': alcohol
            }

            input_data = np.array(list(data.values())).reshape(1,11)  # Wrap in a list to match expected input format

            # Initialize prediction pipeline
            prediction_pipeline = PredictionPipeline()
            
            # Make prediction
            prediction = prediction_pipeline.predict(input_data)
            
            return render_template('results.html', prediction= str(prediction))
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    else:
        return render_template('predict.html')


if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=8080, debug=True)  # Run the Flask app
    app.run(host='0.0.0.0', port=8080)