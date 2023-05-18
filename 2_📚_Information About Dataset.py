import streamlit as st
import seaborn as sns
import pandas as pd


st.title("View Information About Dataset")

if st.session_state["data"] is None:
    st.text("Please upload a csv file at homepage")
    data = None
else:
    data = st.session_state["data"]

if data is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())

if data is not None:
    if st.checkbox("DataType of Each Column"):
        st.write(data.dtypes)

# 5. Find Shape of Our Dataset (Number of Rows And Number of Columns)
if data is not None:
    if st.checkbox("Check dimensions of dataset"):
        data_shape = st.selectbox("Which dimension would you like to view?",["Select one", "Rows","Columns"])
        if data_shape=='Rows':
            st.text("Number of Rows")
            st.write(data.shape[0])
        if data_shape=='Columns':
            st.text("Number of Columns")
            st.write(data.shape[1])

# 6. Find Null Values in The Dataset
if data is not None:
    test = data.isnull().values.any()
    if test==True:
        if st.checkbox("Check for null/Missing Values in the dataset"):
            st.text("Dataset contains missing values. Total number of missing values:")
            st.text(data.isnull().sum().sum())
    else:
        st.text("No Missing Values")
        

# 7. Find Duplicate Values in the dataset
if data is not None:
    if st.checkbox("Check for duplicate values in the dataset"):
        test = data.duplicated().any()
        if test==True:
            st.text("Duplicates values are present in the dataset")
        else:
            st.text("No duplicate values in dataset!")

# 8. Get Overall Statistics
if data is not None:
    if st.checkbox("Summary of The Dataset"):
        st.write(data.describe(include='all'))
       