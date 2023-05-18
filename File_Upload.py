import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Machine Learning Pre-processing App",
)

st.title("Machine Learning Pre-processing")
st.write("<span style='font-family: Arial, sans-serif;'>Transform your data with ease! Explore your CSV datasets and prepare them for machine learning algorithms.<br><br></span>", unsafe_allow_html=True)

if "data" not in st.session_state:
    st.session_state["data"] = None

#file upload by user
st.subheader("Upload your dataset [in CSV format]")
upload = st.file_uploader("", type=['csv'], accept_multiple_files=False, key='file_uploader')

if upload is not None:
    #checking file type
    if upload.type == 'text/csv':
        data = pd.read_csv(upload)
        st.session_state["data"] = data
        st.write("You have entered: ", data.head())
    else:
        st.error("Invalid file format. Please upload a CSV file.")