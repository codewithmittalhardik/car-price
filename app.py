from flask import Flask, render_template, request
from whitenoise import WhiteNoise
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app, root='static')

car = pd.read_csv('Cleaned_Car_data.csv')

# Load the trained model
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

@app.route('/')
def home():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique(), reverse=True)
    fuel_type = sorted(car['fuel_type'].unique())
    return render_template('index.html', companies=companies, car_models=car_models, years=year, fuel_type=fuel_type)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        car_model = request.form.get('car_model')
        company = request.form.get('company')
        year = int(request.form.get('year'))
        fuel_type = request.form.get('fuel_type').capitalize()  # Capitalize to match training data
        kilometers = float(request.form.get('kilometers'))
        
        # Create a DataFrame with the same structure as training data
        # The model expects: name, company, year, kms_driven, fuel_type
        input_df = pd.DataFrame({
            'name': [car_model],
            'company': [company],
            'year': [year],
            'kms_driven': [kilometers],
            'fuel_type': [fuel_type]
        })
        
        # Make prediction
        prediction = model.predict(input_df)[0]
        
        # Return the prediction as a string
        return str(round(prediction, 2))
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return "Error: Could not predict"

if __name__ == '__main__':
    app.run(debug=True, port=8000)