import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO





st.sidebar.header('Navigation')
main_page = st.sidebar.radio('Go to:', ['Home', 'Data Overview', 'Visualizations'])

if main_page == 'Home':
    st.title('Welcome to the Solar Radiation Analysis')
    st.write('Introduction to the app and its purpose.')
elif main_page == 'Data Overview':
    sub_page = st.sidebar.selectbox('Data Overview Options:', ['Overview', 'Summary', 'Statistics'])
    if sub_page == 'Overview':
        st.title('Data Overview')
        st.write('Description of the data and its structure.')
    elif sub_page == 'Summary':
        st.title('Data Summary')
        st.write('A brief summary of key data points.')
    elif sub_page == 'Statistics':
        st.title('Data Statistics')
        st.write('Descriptive statistics of the data.')
elif main_page == 'Visualizations':
    sub_page = st.sidebar.selectbox('Visualization Options:', ['Histogram', 'Bubble Chart', 'Scatter Plot'])
    if sub_page == 'Histogram':
        st.title('Histogram')
        st.write('Visualizing data distribution.')
    elif sub_page == 'Bubble Chart':
        st.title('Bubble Chart')
        st.write('Analyzing relationships between variables.')
    elif sub_page == 'Scatter Plot':
        st.title('Scatter Plot')
        st.write('Exploring relationships between data points.')


