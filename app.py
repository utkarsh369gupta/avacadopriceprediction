import streamlit as st
import numpy as np
import pandas as pd
import random

# Load the dataset to get column names
dataset = pd.read_csv("avocado.csv")

# Select the specific columns you need as inputs
selected_columns = ["Date", "type", "year", "region", "Total Volume"]

# Streamlit app title
st.title("XGBoost Regression Predictor (Simulated)")

# Input fields for selected columns
st.header("Input the feature values:")

input_data = []

# Input for Date (may require special handling if it needs to be numerical or specific format)
date = st.date_input("Date")
input_data.append(date.toordinal())  # Convert date to ordinal for numerical input

# Input for Type (dropdown for selecting categorical type)
type_option = st.selectbox("Type", dataset["type"].unique())
input_data.append(1 if type_option == "organic" else 0)  # Convert to numerical

# Input for Region (dropdown for selecting categorical region)
region = st.selectbox("Region", dataset["region"].unique())
input_data.append(dataset["region"].unique().tolist().index(region))  # Convert to numerical index

# Button to trigger prediction
if st.button("Predict"):
    # Generate a random value between 0.80 and 1.4
    prediction = random.uniform(0.80, 1.4)
    
    # Display the prediction in larger, bold text
    st.markdown(f"<h2 style='font-size: 2em; color: #4CAF50;'><strong>Predicted value: ${prediction:.2f}</strong></h2>", unsafe_allow_html=True)
