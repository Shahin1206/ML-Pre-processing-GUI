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

# Check if data has been uploaded
if data is not None:
    # Select columns for bivariate visualization
    col1, col2 = st.columns(2)
    with col1:
        x_col = st.selectbox("Select first column", data.columns)
    with col2:
        y_col = st.selectbox("Select second column", data.columns)

    # Bivariate visualization options
    plot_type = st.selectbox("Select plot type", ["Select One", "Scatterplot", "Lineplot","Heatmap"])
    if plot_type == "Scatterplot":
        # Scatterplot
        fig, ax = plt.subplots()
        sns.scatterplot(data=data, x=x_col, y=y_col)
        st.pyplot(fig)
    elif plot_type == "Lineplot":
        # Lineplot
        fig, ax = plt.subplots()
        sns.lineplot(data=data, x=x_col, y=y_col)
        st.pyplot(fig)
    elif plot_type == 'Heatmap':
        # Heatmap
        fig2, ax2 = plt.subplots(figsize=(4, 2))
        sns.heatmap(data[[x_col, y_col]].corr(), annot=True, cmap="coolwarm", ax=ax2)
        st.pyplot(fig2)