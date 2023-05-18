import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import base64
import numpy as np

st.title("Scaling Numerical Variables")

if st.session_state["data"] is None:
    st.text("Please upload a csv file at homepage")
    data = None
else:
    data = st.session_state["data"]

if data is not None:
    scaling_option = st.selectbox("Select scaling option", ["Select one", "Standard Scaler", "Min-Max Scaler"])
    if scaling_option == "Standard Scaler":
        scaler = StandardScaler()
        for i in data.columns:
            if data[i].dtype in ['int32', 'float32', 'int64', 'float64']:
                col_data = data[i].values.reshape(-1, 1)
                data[i] = scaler.fit_transform(col_data)
    elif scaling_option == "Min-Max Scaler":
        scaler = MinMaxScaler()
        for i in data.columns:
            if data[i].dtype in ['int32', 'float32', 'int64', 'float64']:
                col_data = data[i].values.reshape(-1, 1)
                data[i] = scaler.fit_transform(col_data)

    st.write("Preprocessed data:")
    st.write(data)

    csv = data.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="preprocessed_data.csv">Download preprocessed data</a>'
    st.markdown(href, unsafe_allow_html=True)