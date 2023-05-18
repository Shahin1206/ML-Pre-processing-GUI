import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import base64
import numpy as np

st.title("Handling Missing Values")

if st.session_state["data"] is None:
    st.text("Please upload a csv file at homepage")
    data = None
else:
    data = st.session_state["data"]

if data is not None:
    #creating list of numerical and categorical columns in dataset
        numeric_columns = []
        for i in data.columns:
            if data[i].dtype in ['int32', 'float32', 'int64', 'float64']:
                numeric_columns.append(i)
        
        categoric_columns = []
        for i in data.columns:
            if data[i].dtype in ['object']:
                categoric_columns.append(i)

        # (1) CHECK AND HANDLE MISSING NUMERICAL VALUES
        if st.checkbox("Handle numerical missing values"):
            st.subheader("Numerical Missing Values")
            missing_value_option_num = st.selectbox("Select missing value handling option for numerical attributes", ["Select method","Drop Missing Values", "Replace with mean", "Replace with median"])
            missing_values = data[numeric_columns].isna().sum().sum()
            if missing_values > 0:
                st.write(f"There are {missing_values} missing numerical values in the data.")

                if missing_value_option_num == "Drop Missing Values":
                    # drop rows with missing values
                    data = data.dropna()
                    st.write("Rows with missing values have been dropped.")
                elif missing_value_option_num == "Replace with mean":
                    # fill missing values with mean
                    data.fillna(data.mean(), inplace=True)
                    st.write("Missing values have been filled with the mean.")
                elif missing_value_option_num == "Replace with median":
                    # fill missing values with mean
                    data.fillna(data.median(), inplace=True)
                    st.write("Missing values have been filled with the median.")
            else:
                st.write("There are no missing numerical values in the data.")
        
        # CHECK AND HANDLE MISSING CATEGORICAL VALUES
        if st.checkbox("Handle categorical missing values"):
            st.subheader("Categorical Missing Values")
            missing_value_option_cat = st.selectbox("Select missing value handling option for categorical attributes", ["Select method","Replace with mode"])
            missing_values = data[categoric_columns].isna().sum().sum()
            if missing_values > 0:
                st.write(f"There are {missing_values} missing categorical values in the data.")
                if missing_value_option_cat == "Replace with mode":
                    # fill missing values with mode
                    data[categoric_columns] = data[categoric_columns].fillna(data.mode().iloc[0])
                    st.write("Missing categorical values have been filled with the mode.")
            else:
                st.write("There are no missing values in the data")

        # display preprocessed data
        st.write("Preprocessed data:")
        st.write(data)


        #download preprocessed data
        csv = data.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="preprocessed_data.csv">Download preprocessed data</a>'
        st.markdown(href, unsafe_allow_html=True)
