import streamlit as st
import numpy as np
import pandas as pd
import os

# Load the dataset to get column names
dataset = pd.read_csv("avocado.csv")
column_names = dataset.columns.tolist()

# Remove unnecessary columns
if "AveragePrice" in column_names:
    column_names.remove("AveragePrice")
if "Unnamed: 0" in column_names:
    column_names.remove("Unnamed: 0")

# Streamlit app title
st.title("Data Input for CSV Storage")

# Input fields for selected columns
st.header("Input the feature values:")

# Input for Date (stored as a string)
date = st.date_input("Date")
date_input = date.strftime("%Y-%m-%d")  # Store as date string

# Input for Type (stored as is without conversion)
type_option = st.selectbox("Type", dataset["type"].unique())

# Input for Year
year = st.number_input("Year", min_value=2015, max_value=2020, step=1)

# Input for Region (stored as is without conversion)
region = st.selectbox("Region", dataset["region"].unique())

# Input for Total Volume as a number input
# total_volume = st.number_input("Total Volume", value=0.0)

# Create a dictionary to store the input data, setting unspecified columns to NaN
input_data = {
    "Date": date_input,
    "type": type_option,
    "year": year,
    "region": region,
    "Total Volume": 1234,
    "4046": 293008,
    "4225": 295154,
    "4770": 22839,
    "Total Bags": 239639,
    "Small Bags": 182194,
    "Large Bags": 54338,
    "XLarge Bags": 3106,
}

# Ensure all columns are included in the input_data, filling with NaN where needed
for col in column_names:
    if col not in input_data:
        input_data[col] = np.nan

# Convert the input data into a DataFrame
input_df = pd.DataFrame([input_data])

# Ensure the columns in input_df are in the same order as the original dataset
input_df = input_df[column_names]

# Button to save input data to CSV
if st.button("Save to CSV"):
    # Save to CSV
    if os.path.exists("DataFromUser.csv"):
        # Append to existing CSV if it exists
        input_df.to_csv("DataFromUser.csv", mode='a', header=False, index=False)
    else:
        # Create new CSV with headers if it doesn't exist
        input_df.to_csv("DataFromUser.csv", mode='w', header=True, index=False)
    
    st.write("DataFromUser.csv")
