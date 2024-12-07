import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO


st.sidebar.header('Navigation')
page = st.sidebar.radio('Go to:', ['Home', 'Data Overview', 'Visualizations', 'Settings'])

if page == 'Home':
    st.title('Welcome to the Streamlit App')
    st.write('Introduction to the app and its purpose.')
elif page == 'Data Overview':
    st.title('Data Overview')
    st.write('Description of the data and its structure.')
elif page == 'Visualizations':
    st.title('Data Visualizations')
    st.write('Explore the data through various visualizations.')
elif page == 'Settings':
    st.title('Settings')
    st.write('Adjust the settings and filters for data visualization.')
