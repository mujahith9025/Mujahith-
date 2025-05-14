import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load("model_sklearn_1_6_1.pkl")  # Replace with your trained model path

# App title and description
st.title("🌍 Air Quality Level Predictor")
st.markdown("""
This app predicts the **Air Quality Index (AQI)** based on environmental pollutant levels using a machine learning model.
""")

# Sidebar inputs
st.sidebar.header("Enter pollutant levels")
pm25 = st.sidebar.number_input("PM2.5 (µg/m³)", 0.0, 500.0, step=1.0)
pm10 = st.sidebar.number_input("PM10 (µg/m³)", 0.0, 600.0, step=1.0)
no2 = st.sidebar.number_input("NO2 (ppb)", 0.0, 300.0, step=1.0)
so2 = st.sidebar.number_input("SO2 (ppb)", 0.0, 300.0, step=1.0)
co = st.sidebar.number_input("CO (ppm)", 0.0, 50.0, step=0.1)
o3 = st.sidebar.number_input("O3 (ppb)", 0.0, 300.0, step=1.0)

# Predict button
if st.sidebar.button("Predict AQI"):
    # Create input DataFrame
    input_data = pd.DataFrame({
        'PM2.5': [pm25],
        'PM10': [pm10],
        'NO2': [no2],
        'SO2': [so2],
        'CO': [co],
        'O3': [o3]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display result
    st.success(f"✅ Predicted AQI Level: **{prediction:.2f}**")

    # Basic AQI interpretation
    if prediction <= 50:
        st.info("Air Quality: Good 😊")
    elif prediction <= 100:
        st.warning("Air Quality: Moderate 😐")
    else:
        st.error("Air Quality: Unhealthy 😷")
