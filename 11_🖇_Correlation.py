import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Function to calculate correlation heatmap
def plot_corr_heatmap(data):
    fig, ax = plt.subplots(figsize=(8,8))
    corr = data.corr()
    sns.heatmap(corr, cmap='coolwarm', annot=True, fmt='.2f', square=True, ax=ax)
    ax.set_title('Correlation Heatmap')
    st.pyplot(fig)

st.title("Correlation")

if st.session_state["data"] is None:
    st.text("Please upload a csv file at homepage")
    data = None
else:
    data = st.session_state["data"]

if data is not None:
    # Select column
    col = st.selectbox("Select a column", data.columns)

    # Check if selected column is numeric
    if pd.api.types.is_numeric_dtype(data[col]):

        # Display correlations with other columns
        st.write("Correlations with selected column:")
        corr = data.corr()[col]
        st.write(corr)

        # Display correlation heatmap
        st.write("Correlation heatmap:")
        plot_corr_heatmap(data)

    else:
        st.write("Selected column is not numeric.")
