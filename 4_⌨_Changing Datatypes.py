import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import base64
import numpy as np

def change_data_type(df, column_name, data_type):
    try:
        df[column_name] = df[column_name].astype(data_type)
    except ValueError:
        st.warning(f"Could not convert {column_name} to {data_type}")
    return df

 # CHECK AND CHANGE DATATYPES OF COLUMNS
st.title("Checking and Changing Datatypes")

if st.session_state["data"] is None:
    st.text("Please upload a csv file at homepage")
    data = None
else:
    data = st.session_state["data"]

if data is not None:
        column_datatypes = {}

        if st.checkbox("DataType of Each Column"):
            # Display the current data types
            st.write("Current data types:")
            st.write(data.dtypes)

        st.write("Change data types:")
        for column_name in data.columns:
            data_type = st.selectbox(f"{column_name}: {data[column_name].dtype}", options=["Select one","int", "float", "object"])
            if data_type == "int":
                data = change_data_type(data, column_name, "int64")
            elif data_type == "float":
                data = change_data_type(data, column_name, "float64")
            elif data_type == "object":
                data = change_data_type(data, column_name, "object")
        
        if st.checkbox("View changed datatypes"):
            # Display the current data types
            st.write("New data types:")
            st.write(data.dtypes)


        csv = data.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="preprocessed_data.csv">Download preprocessed data</a>'
        st.markdown(href, unsafe_allow_html=True)
        