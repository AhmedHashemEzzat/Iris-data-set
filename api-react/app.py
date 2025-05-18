from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Load the model
model_path = os.getenv("MODEL_PATH", os.path.join("api", "Model.pkl"))
target_names = ["Setosa", "Versicolor", "Virginica"]

try:
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at: {model_path}")
        
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    print(f"Successfully loaded model from: {model_path}")
except Exception as e:
    print(f"Error loading model: {e}")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Files in current directory: {os.listdir('.')}")
    raise

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        features = np.array([data['feature_array']])

        prediction = model.predict(features)[0]
        probabilities = model.predict_proba(features)[0]

        response = {
            'prediction': target_names[prediction],
            'confidence': {
                target_names[i]: float(prob) * 100
                for i, prob in enumerate(probabilities)
            }
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    port = int(os.getenv("FLASK_PORT", 5001))
    app.run(debug=True, port=5001, host='0.0.0.0')
