from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Load model and scaler
model = joblib.load("C:/Users/Administrator/Desktop/AI/AI Project/knn_model.pkl")
scaler = joblib.load("C:/Users/Administrator/Desktop/AI/AI Project/scaler.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Get features from JSON
        features = [
            float(data['sepal_length']),
            float(data['sepal_width']),
            float(data['petal_length']),
            float(data['petal_width'])
        ]

        # Preprocess
        features_scaled = scaler.transform([features])
        prediction = model.predict(features_scaled)[0]

        # Return as JSON
        return jsonify({'prediction': prediction})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
