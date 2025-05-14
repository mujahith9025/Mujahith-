import joblib
import streamlit as st

# Load the correct model file
model = joblib.load("model (1).pkl")  # or "model.pkl" if renamed

st.title("🌍 Air Quality Level Predictor")
