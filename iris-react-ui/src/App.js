// iris-react-ui/src/App.js

import React, { useState } from 'react';
import './App.css';

function App() {
  const [features, setFeatures] = useState({
    sepal_length: 5.1,
    sepal_width: 3.5,
    petal_length: 1.4,
    petal_width: 0.2
  });

  const [prediction, setPrediction] = useState('');
  const [confidence, setConfidence] = useState({});
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFeatures({ ...features, [e.target.name]: parseFloat(e.target.value) });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    setPrediction('');
    setConfidence({});

    try {
      const response = await fetch("http://localhost:5001/predict", {
        method: "POST",
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          feature_array: [
            features.sepal_length,
            features.sepal_width,
            features.petal_length,
            features.petal_width
          ]
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      setPrediction(data.prediction);
      setConfidence(data.confidence);
    } catch (error) {
      console.error('Error:', error);
      setError('Failed to get prediction. Please ensure the server is running.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>🌸 Iris Flower Classifier</h1>
      <p>Provide flower measurements to predict its species using a trained logistic regression model.</p>
      
      <form onSubmit={handleSubmit}>
        {Object.entries(features).map(([key, value]) => (
          <div key={key} className="input-group">
            <label>{key.split('_').join(' ')} (cm):</label>
            <input
              type="range"
              min={key.includes('petal_width') ? "0.1" : "1.0"}
              max={key.includes('sepal_length') ? "8.0" : 
                   key.includes('sepal_width') ? "4.5" :
                   key.includes('petal_length') ? "7.0" : "2.5"}
              step="0.1"
              name={key}
              value={value}
              onChange={handleChange}
            />
            <span>{value}</span>
          </div>
        ))}
        <button type="submit" disabled={loading}>
          🔍 {loading ? 'Predicting...' : 'Predict'}
        </button>
      </form>

      {error && <div className="error">{error}</div>}

      {prediction && !error && (
        <div className="prediction">
          <h2>🌼 Predicted Species: {prediction}</h2>
          <h3>📊 Prediction Confidence:</h3>
          <ul>
            {Object.entries(confidence).map(([species, prob]) => (
              <li key={species}>
                {species}: {prob.toFixed(2)}%
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
