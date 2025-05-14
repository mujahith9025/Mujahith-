import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
data = pd.read_csv("city_day.csv")

# Select relevant columns and drop missing values
columns = ["PM2.5", "PM10", "NO2", "CO", "SO2", "O3", "AQI"]
data = data[columns].dropna()

X = data[["PM2.5", "PM10", "NO2", "CO", "SO2", "O3"]]
y = data["AQI"]

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model.pkl")
print("✅ Model trained and saved as 'model.pkl'")
