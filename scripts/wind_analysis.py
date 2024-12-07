import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from math import pi

def wind_analysis(file_path: str):
    # Load the data
    df = pd.read_csv(file_path, parse_dates=['Timestamp'])
    # Set the Timestamp as index for time series plotting
    df.set_index('Timestamp', inplace=True)

    # **Step 1: Distribution of Wind Speed (WS and WSgust)**
    plt.figure(figsize=(12, 6))

    # Distribution of wind speeds
    sns.histplot(df['WS'], bins=30, kde=True, color='blue', alpha=0.6, label='Wind Speed (WS)')
    sns.histplot(df['WSgust'], bins=30, kde=True, color='green', alpha=0.6, label='Wind Gust (WSgust)')
    
    plt.title('Distribution of Wind Speeds')
    plt.xlabel('Wind Speed (m/s)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

    # **Step 2: Wind Rose for Wind Direction (WD)**
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(12, 6))

    # Convert wind direction to radians for polar plot
    df['WD_rad'] = np.deg2rad(df['WD'])

    # Plot wind rose
    ax.hist(df['WD_rad'], bins=np.linspace(0, 2 * np.pi, 36), color='purple', alpha=0.6)
    
    # Set labels and limits
    ax.set_title('Wind Rose for Wind Direction (WD)')
    ax.set_xticks(np.linspace(0, 2 * np.pi, 12, endpoint=False))
    ax.set_xticklabels(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'], rotation=45)
    ax.set_ylim(0, df['WD_rad'].count() / 2)

    plt.show()

# Example usage:
# wind_analysis('path/to/your/solar_data_cleaned.csv')
