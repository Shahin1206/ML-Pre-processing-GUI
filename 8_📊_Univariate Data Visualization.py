import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Data Visualization")

if st.session_state["data"] is None:
    st.text("Please upload a csv file at homepage")
    data = None
else:
    data = st.session_state["data"]

if data is not None:
    column = st.selectbox("Select a column", data.columns)

    # Check data type of selected column
    if data[column].dtype == "object":
        # Categorical column
        st.subheader(f"Categorical column: {column}")
        plt_type_cat = st.selectbox("Visualization option",["Choose One","Count Plot","Bar Plot"])
        
        if plt_type_cat == "Count Plot":
            # Countplot
            sns.set(font_scale=0.6)
            fig, ax = plt.subplots(figsize=(5, 3))
            sns.countplot(data=data, x=column, ax=ax)
            ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
            st.pyplot(fig)

        if plt_type_cat == "Bar Plot":
            # Bar chart
            sns.set(font_scale=0.6)
            fig, ax = plt.subplots(figsize=(5, 3))
            data[column].value_counts().plot(kind="bar", ax=ax)
            ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
            st.pyplot(fig)
        
    else:
        # Numerical column
        st.subheader(f"Numerical column: {column}")
        plt_type_num = st.selectbox("Visualization option",["Choose One","Histogram","Box Plot"])

        if plt_type_num == "Histogram":
            # Histogram
            fig, ax = plt.subplots(figsize=(5, 3))
            sns.histplot(data=data, x=column, ax=ax)
            st.pyplot(fig)

        if plt_type_num == "Box Plot":
            # Boxplot
            fig, ax = plt.subplots(figsize=(5,3))
            sns.boxplot(data=data, x=column, ax=ax)
            st.pyplot(fig)