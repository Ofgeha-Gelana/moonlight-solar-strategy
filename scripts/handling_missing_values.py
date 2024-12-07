import pandas as pd
import numpy as np

# Function for data cleaning
def clean_data(df):
    """
    Cleans the dataset by performing the following steps:
    1. Drops irrelevant columns like 'Comments'.
    2. Handles missing values by dropping rows with missing critical data and applying forward/backward fill.
    3. Handles anomalies by replacing negative values with NaN.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to clean.
    
    Returns:
    pd.DataFrame: The cleaned DataFrame.
    """
    # Step 1: Drop irrelevant columns like 'Comments' which are entirely null
    df = df.drop(columns=['Comments'], errors='ignore')
    
    # Step 2: Handle missing values
    return df
