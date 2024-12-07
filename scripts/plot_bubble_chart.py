import pandas as pd
import matplotlib.pyplot as plt

def plot_bubble_chart(df, x_var, y_var, size_var, title):
    """
    Plot a bubble chart to explore complex relationships between variables.

    Parameters:
    - df: pandas DataFrame containing the data.
    - x_var: The variable to plot on the x-axis.
    - y_var: The variable to plot on the y-axis.
    - size_var: The variable to determine bubble size.
    - title: The title of the plot.

    Returns:
    - A bubble chart.
    """
    # Create the bubble chart
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(df[x_var], df[y_var], s=df[size_var], alpha=0.6, c='blue', edgecolors='w')
    
    # Adding labels and title
    plt.xlabel(x_var)
    plt.ylabel(y_var)
    plt.title(title)
    plt.colorbar(scatter, label=size_var)

    # Show the plot
    plt.grid(True)
    plt.show()

# # Example usage:
# # Load the dataset
# df = pd.read_csv('your_dataset.csv')  # Replace with the path to your dataset

# # Variables to be plotted
# x_var = 'GHI'
# y_var = 'Tamb'
# size_var = 'RH'  # or 'BP' for Barometric Pressure

# # Plot the bubble chart
# plot_bubble_chart(df, x_var, y_var, size_var, 'Bubble Chart: GHI vs. Tamb vs. WS with Bubble Size as RH or BP')
