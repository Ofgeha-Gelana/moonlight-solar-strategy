
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


df = pd.read_csv("../data/processed/cleaned_data.csv", parse_dates=['Timestamp'])
    # Set the Timestamp as index for time series plotting
df.set_index('Timestamp', inplace=True)

# utils.py

def histogram_for_GHI(df):
    # Create a new figure and axes
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(df['GHI'], bins=30, kde=True, ax=ax)
    ax.set_title('Histogram of GHI (Global Horizontal Irradiance)')
    ax.set_xlabel('GHI (W/m²)')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)  # Pass the figure to st.pyplot()
    
    
def hi

# Histogram for DNI
plt.figure(figsize=(8, 6))
sns.histplot(df['DNI'], bins=30, kde=True)
plt.title('Histogram of DNI (Direct Normal Irradiance)')
plt.xlabel('DNI (W/m²)')
plt.ylabel('Frequency')
plt.show()

