import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def time_series_analysis(file_path: str):
    # Load the data
    df = pd.read_csv(file_path, parse_dates=['Timestamp'])
    # Set the Timestamp as index for time series plotting
    df.set_index('Timestamp', inplace=True)

    # Plotting GHI, DNI, DHI, and Tamb over time
    plt.figure(figsize=(15, 8))

    # Subplot 1: Solar Irradiance components (GHI, DNI, DHI)
    plt.subplot(2, 1, 1)
    plt.plot(df.index, df['GHI'], label='GHI', color='orange')
    plt.plot(df.index, df['DNI'], label='DNI', color='blue')
    plt.plot(df.index, df['DHI'], label='DHI', color='green')
    plt.title('Solar Irradiance Components Over Time')
    plt.xlabel('Timestamp')
    plt.ylabel('Solar Irradiance')
    plt.legend()

    # Subplot 2: Temperature (Tamb)
    plt.subplot(2, 1, 2)
    plt.plot(df.index, df['Tamb'], label='Tamb', color='red')
    plt.title('Temperature Over Time')
    plt.xlabel('Timestamp')
    plt.ylabel('Temperature (°C)')
    plt.legend()

    plt.tight_layout()
    plt.show()

    # Evaluate the impact of cleaning on ModA and ModB over time
    plt.figure(figsize=(15, 4))

    # ModA over time
    plt.subplot(1, 2, 1)
    plt.plot(df.index, df['ModA'], label='ModA', color='purple')
    plt.title('ModA Over Time')
    plt.xlabel('Timestamp')
    plt.ylabel('ModA Readings')
    plt.legend()

    # ModB over time
    plt.subplot(1, 2, 2)
    plt.plot(df.index, df['ModB'], label='ModB', color='brown')
    plt.title('ModB Over Time')
    plt.xlabel('Timestamp')
    plt.ylabel('ModB Readings')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Example usage:
# time_series_analysis('path/to/your/solar_data_cleaned.csv')
