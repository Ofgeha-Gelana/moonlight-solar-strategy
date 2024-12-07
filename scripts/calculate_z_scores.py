import pandas as pd
import numpy as np

def calculate_z_scores(df, columns, threshold=3):
    """
    Calculate Z-scores for specified columns in the DataFrame and flag data points as outliers.

    Parameters:
    - df: pandas DataFrame containing the data.
    - columns: List of column names for which Z-scores need to be calculated.
    - threshold: The Z-score threshold to identify outliers. Default is 3.

    Returns:
    - DataFrame with an additional 'Outlier' column for each specified variable.
    """
    for column in columns:
        # Calculate Z-scores for the column
        z_scores = (df[column] - df[column].mean()) / df[column].std()
        
        # Flag outliers
        df[f'{column}_Outlier'] = np.abs(z_scores) > threshold
    
    return df

