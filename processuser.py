import pandas as pd
import numpy as np
from numpy import percentile

# Load dataset with date parsing
dataset = pd.read_csv("DataFromUser.csv", parse_dates=['Date'], dayfirst=True)

# Check if Date parsing failed for any row
if dataset['Date'].isna().any():
    print("Warning: Some dates could not be parsed and have been set to NaT.")

# Extract month and day from Date column
dataset['Month'] = dataset['Date'].dt.month
dataset['Day'] = dataset['Date'].dt.day
dataset.drop(columns=["Date"], inplace=True)

# Process each column for outliers
columns = dataset.columns
for j in columns:
    if not pd.api.types.is_numeric_dtype(dataset[j]):
        continue  # Skip non-numeric columns
    
    # Define quartiles, excluding NaN values if any
    quartiles = percentile(dataset[j].dropna(), [25, 75])
    
    # Calculate min/max fences
    lower_fence = quartiles[0] - (1.5 * (quartiles[1] - quartiles[0]))
    upper_fence = quartiles[1] + (1.5 * (quartiles[1] - quartiles[0]))
    
    # Apply limits to handle outliers
    dataset[j] = dataset[j].apply(lambda x: upper_fence if x > upper_fence else (lower_fence if x < lower_fence else x))

# Display the updated dataset
dataset['region'] = pd.Categorical(dataset['region'])
dfDummies_region = pd.get_dummies(dataset['region'], prefix = 'region').astype(int)
dataset = pd.concat([dataset, dfDummies_region], axis=1)
dataset.drop(columns="region",inplace=True)
dataset['Month'] = pd.Categorical(dataset['Month'])
dfDummies_month = pd.get_dummies(dataset['Month'], prefix = 'month').astype(int)
dataset = pd.concat([dataset, dfDummies_month], axis=1)
dataset.drop(columns="Month",inplace=True)


from sklearn import preprocessing 
 
label_encoder = preprocessing.LabelEncoder() 
dataset['type']= label_encoder.fit_transform(dataset['type'])

print(dataset) 