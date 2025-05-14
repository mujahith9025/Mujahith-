import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("model.pkl")

st.title("🌍 Air Quality Level Predictor")
st.markdown("Predict AQI (Air Quality Index) based on pollutant levels.")

# Input sliders
pm25 = st.slider("PM2.5 (µg/m³)", 0.0, 500.0, 50.0)
pm10 = st.slider("PM10 (µg/m³)", 0.0, 500.0, 50.0)
no2 = st.slider("NO2 (µg/m³)", 0.0, 200.0, 40.0)
co = st.slider("CO (mg/m³)", 0.0, 5.0, 1.0)
so2 = st.slider("SO2 (µg/m³)", 0.0, 100.0, 20.0)
o3 = st.slider("O3 (µg/m³)", 0.0, 300.0, 60.0)

# Predict
input_data = np.array([[pm25, pm10, no2, co, so2, o3]])
if st.button("Predict AQI"):
    prediction = model.predict(input_data)[0]
    st.success(f"🌫️ Predicted AQI: {prediction:.2f}")
