import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os, sys



def correlation_analysis(file_path: str):
    # Load the data
    df = pd.read_csv(file_path, parse_dates=['Timestamp'])
    # Set the Timestamp as index for time series plotting
    df.set_index('Timestamp', inplace=True)

    # **Step 1: Correlation Matrix for Solar Radiation Components and Temperature Measures**
    plt.figure(figsize=(12, 8))
    
    # Correlation matrix for GHI, DNI, DHI, TModA, and TModB
    corr_matrix = df[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']].corr()
    
    # Plotting the heatmap
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Matrix: Solar Radiation Components and Temperature Measures')
    plt.show()

    # **Step 2: Pair Plot for Solar Radiation Components and Temperature Measures**
    sns.pairplot(df[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']])
    plt.suptitle('Pair Plot: Solar Radiation Components and Temperature Measures', y=1.02)
    plt.show()

    # **Step 3: Scatter Matrix for Wind Conditions and Solar Irradiance**
    wind_conditions = df[['WS', 'WSgust', 'WD']]
    solar_irradiance = df[['GHI', 'DNI', 'DHI']]

    # Scatter Matrix
    scatter_matrix = pd.concat([wind_conditions, solar_irradiance], axis=1)
    scatter_matrix_plot = sns.pairplot(scatter_matrix)
    scatter_matrix_plot.fig.suptitle('Scatter Matrix: Wind Conditions and Solar Irradiance', y=1.02)
    plt.show()