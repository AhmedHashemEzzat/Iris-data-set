# streamlit run iris_app.py
import streamlit as st
import pickle
import numpy as np
import os

# Set app title
st.set_page_config(page_title="Iris Classifier", page_icon="🌸")
st.title("🌸 Iris Flower Classifier")
st.write("Provide flower measurements to predict its species using a trained logistic regression model.")

# Load the model from 'api/Model.pkl'
model_path = os.path.join("api", "Model.pkl")
target_names = ["Setosa", "Versicolor", "Virginica"]

try:
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at: {model_path}")

    with open(model_path, "rb") as f:
        model = pickle.load(f)

except Exception as e:
    st.error(f"❌ Failed to load model: {e}")
    st.stop()

st.subheader("🌿 Input Flower Features")
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.1)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

if st.button("🔍 Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    prediction = model.predict(input_data)[0]
    prediction_proba = model.predict_proba(input_data)[0]

    st.success(f"🌼 Predicted Species: **{target_names[prediction]}**")
    st.write("📊 Prediction Confidence:")
    for i, name in enumerate(target_names):
        st.write(f"- {name}: {prediction_proba[i]*100:.2f}%")