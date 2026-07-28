import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="SRC ", layout="wide")

st.markdown(
    """
    <style>
    .stAppDeployButton {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def spearman(df):
    st.dataframe(df)
    x = np.array(df['A'])
    y = np.array(df['B'])

    sum_of_di = 0

    for i in range(len(x)):
        sum_of_di += (x[i] - y[i]) ** 2

    sp_rank = 1 - ((6 * sum_of_di) / (len(x) * (len(x) ** 2 - 1)))

    st.markdown(
        f"<h2 style='text-align: center;'>Spearman Rank Correlation is: {sp_rank:.2f}</h2>", 
        unsafe_allow_html=True
    )

upload_file = st.file_uploader("Choose a CSV File", type=["csv"])
if upload_file is not None:
    if upload_file.name.endswith('.csv'):
        df = pd.read_csv(upload_file)
        spearman(df)