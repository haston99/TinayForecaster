import streamlit as st
import numpy as np
import pandas as pd 
import io
from PIL import Image

#-------------------- Prophet forecasting ----------------------------------------------------------------


# A Project by Mangle Yann Houphouet for computer science bsc thesis research 
# 9170214004
# ZUST 

#------------------------------Data Page Backend ---------------------------------------

st.set_page_config(
    page_title="Tinay Forecaster",
    page_icon="🔎"

)

display = Image.open('Logo-no-back.png')
col1, col2 = st.columns(2)
col1.image(display, width = 800)


st.write("")

"""Upload & Preview your csv dataset here !"""

data = st.file_uploader("Choose a file", type=["csv"])
if data is not None:
    df = pd.read_csv(data)
    with st.spinner('Wait for it...'):
        if st.button("Preview?"):
            st.subheader("Input DataFrame - df.info()")
      # this workaround below is required to show the output of df.info() in the streamlit text widget
            buffer = io.StringIO()
            df.info(
                buf=buffer,
                verbose=True,
                null_counts=False
            )
            df
            st.text(buffer.getvalue())
            st.subheader("Input DataFrame - df.describe()")
            st.table(df.describe())
            st.subheader("Input DataFrame - Head and Tail")
            st.table(pd.concat([df.head(5), df.tail(5)]))
else:
    e = st.info("Upload dataset first")
    print(e)





hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)