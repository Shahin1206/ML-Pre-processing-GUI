import streamlit as st
import pandas as pd
import base64


st.title("Check For Duplicate Values")

# st.write("You have entered",df)
if st.session_state["data"] is None:
    st.text("Please upload a csv file at homepage")
    data = None
else:
    data = st.session_state["data"]

if data is not None:
    test=data.duplicated().any()
    if test==True:
        duplicate_count = data.duplicated().sum()
        st.write(f"There are currently {duplicate_count} duplicate rows in the dataset.")
        
        dup=st.selectbox("Do You Want to Handle Duplicate Values?", ("Select One","Yes","No"))
        if dup=="Yes":
            # remove duplicate rows
            if st.button("Remove Duplicate Rows"):
                data.drop_duplicates(inplace=True)
                st.write("Duplicate rows have been removed from the dataset.")
                duplicate_count = data.duplicated().sum()
                st.write(f"There are now {duplicate_count} duplicate rows in the dataset.")

            # drop columns with duplicate values
            if st.button("Drop Columns with Duplicate Values"):
                data.drop_duplicates(subset=None, keep="first", inplace=True)
                st.write("Columns with duplicate values have been dropped from the dataset.")

            # drop all duplicate rows except for the first occurrence
            if st.button("Drop All Duplicate Rows Except First"):
                data.drop_duplicates(keep="first", inplace=True)
                st.write("All duplicate rows except for the first occurrence have been dropped from the dataset.")

        if dup=="No":
            st.text("Okay! Duplicate values won't be handled")
        
    else:
        st.success("No duplicate values in dataset!")

    csv = data.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="preprocessed_data.csv">Download preprocessed data</a>'
    st.markdown(href, unsafe_allow_html=True)