import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import base64
import numpy as np

def label_encode(df, col):
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    return df

def onehot_encode(df, col):
    ohe = OneHotEncoder()
    ohe_df = pd.DataFrame(ohe.fit_transform(df[[col]]).toarray(), columns=[col+'_'+str(i) for i in range(len(ohe.categories_[0]))])
    df = pd.concat([df, ohe_df], axis=1)
    df = df.drop(columns=[col])
    return df

def encode_categorical(df, col, method):
    if method == 'Label Encoding':
        df = label_encode(df, col)
    elif method == 'One-Hot Encoding':
        df = onehot_encode(df, col)
    return df

st.title("Encoding Categorical Variables")

if st.session_state["data"] is None:
    st.text("Please upload a csv file at homepage")
    data = None
else:
    data = st.session_state["data"]

if data is not None:
    categorical_cols = [col for col in data.columns if data[col].dtype == 'object']
    if len(categorical_cols) > 0:
        selected_col = st.selectbox("Select a column to encode", categorical_cols)
        selected_method = st.selectbox("Select a method of encoding", ["Label Encoding", "One-Hot Encoding"])
        if st.button("Encode"):
            data = encode_categorical(data, selected_col, selected_method)
   
    st.write("Preprocessed data:")
    st.write(data)

    csv = data.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="preprocessed_data.csv">Download preprocessed data</a>'
    st.markdown(href, unsafe_allow_html=True)