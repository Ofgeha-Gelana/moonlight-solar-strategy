
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


df = pd.read_csv("../data/processed/cleaned_data.csv", parse_dates=['Timestamp'])
    # Set the Timestamp as index for time series plotting
df.set_index('Timestamp', inplace=True)

# utils.py

def histogram_for_GHI(df):
    # Histogram for GHI
    plt.figure(figsize=(8, 6))
    sns.histplot(df['GHI'], bins=30, kde=True)
    plt.title('Histogram of GHI (Global Horizontal Irradiance)')
    plt.xlabel('GHI (W/m²)')
    plt.ylabel('Frequency')
    st.pyplot()  # Use st.pyplot() to render the plot in Streamlit
