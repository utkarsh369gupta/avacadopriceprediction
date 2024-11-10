import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the dataset to get column names
dataset = pd.read_csv("avocado.csv")

# Select the specific columns you need as inputs
selected_columns = ["Date", "type", "year", "region", "Total Volume"]

# Load the trained model
model = joblib.load("xgb_regressor_model.pkl")

# Streamlit app title
st.title("XGBoost Regression Predictor")

# Input fields for selected columns
st.header("Input the feature values:")

input_data = []

# Input for Date (may require special handling if it needs to be numerical or specific format)
date = st.date_input("Date")
input_data.append(date.toordinal())  # Convert date to ordinal for numerical input

# Input for Type (dropdown for selecting categorical type)
type_option = st.selectbox("Type", dataset["type"].unique())
input_data.append(1 if type_option == "organic" else 0)  # Convert to numerical

# Input for Year (numerical input)
year = st.number_input("Year", min_value=2015, max_value=2020, step=1)
input_data.append(year)

# Input for Region (dropdown for selecting categorical region)
region = st.selectbox("Region", dataset["region"].unique())
input_data.append(dataset["region"].unique().tolist().index(region))  # Convert to numerical index

# Input for Total Volume (numerical input)
total_volume = st.number_input("Total Volume", value=0.0)
input_data.append(total_volume)

# Convert input data to a NumPy array for prediction
input_array = np.array(input_data).reshape(1, -1)

# Button to trigger prediction
if st.button("Predict"):
    prediction = model.predict(input_array)
    st.write(f"Predicted value: {prediction[0]:.2f}")
