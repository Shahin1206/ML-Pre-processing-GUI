import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import base64

# Function to calculate outliers using Z-score method
def detect_outliers_zscore(data):
    z_scores = (data - data.mean()) / data.std()
    outliers = np.abs(z_scores) > 3
    return outliers

def remove_outliers(data):
    return data[~data['outlier']]

st.title("Outlier Detection and Removal")

if st.session_state["data"] is None:
    st.text("Please upload a csv file at homepage")
    data = None
else:
    data = st.session_state["data"]

if data is not None:
    # Select column
    col = st.selectbox("Select a column", data.columns[0:(len(data.columns)-1)])

    # Check if selected column is numeric
    if pd.api.types.is_numeric_dtype(data[col]):
        # Detect outliers using Z-score method
        outliers = detect_outliers_zscore(data[col])
        data['outlier'] = outliers

        # Display outliers
        st.write("Outliers:")
        st.write(data[data['outlier']])

        if st.checkbox("Remove outliers"):
            data = remove_outliers(data)
            st.write("Outliers removed!")
            
        # Plot boxplot of selected column with outliers highlighted
        fig, ax = plt.subplots(figsize=(5,3))
        sns.boxplot(data=data, x=col, ax=ax)
        st.pyplot(fig)

    else:
        st.write("Selected column is not numeric.")
    
    csv = data.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="preprocessed_data.csv">Download preprocessed data</a>'
    st.markdown(href, unsafe_allow_html=True)
