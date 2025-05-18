# Iris Flower Classification Project

A comprehensive iris flower classification system with multiple user interfaces:
- Streamlit Web Application
- React Web Application
- updated the code and requirements to python 3.11

## Project Structure
```
iris-data-set/
├── api/                # Streamlit API & Model
├── api-react/          # Flask API for React apps
├── iris-react-ui/      # React Web UI
└── iris_app.py         # steamlit Web UI
```

## Features
- Machine Learning model for Iris flower classification
- Interactive UIs with sliders for input
- Real-time predictions with confidence scores


## Setup & Installation

### Using Docker (Recommended)
```bash
docker-compose build
docker-compose up
```

Access the applications at:
- Streamlit UI: http://localhost:8501
- React Web UI: http://localhost:3000
- Flask API: http://localhost:5000
- Flask API: http://localhost:5001
### Manual Setup

1. Create virtual environment:
```bash
python -m venv venv # python 3.11
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install --upgrade pip
```

2. Install dependencies for each component:
```bash
# For API services
pip install -r requirements.txt


# For React Web UI
cd iris-react-ui
npm install



## Running Applications

### Streamlit Api 
```bash`
cd api
python api.py
```
### Streamlit App
```bash
streamlit run iris_app.py
```
### React Api
```bash
cd api-react
python app.py

### React Web App
```bash
cd iris-react-ui
npm start
```



## API Endpoints

### Flask API (`/predict`)
- Method: POST
- Payload:
```json
{
  "feature_array": [sepal_length, sepal_width, petal_length, petal_width]
}
```
- Response:
```json
{
  "prediction": "Species name",
  "confidence": {
    "Setosa": percentage,
    "Versicolor": percentage,
    "Virginica": percentage
  }
}
```

## Requirements
- Python 3.11
- Node.js 18+
- Mircrosoft tool c++
- Docker 