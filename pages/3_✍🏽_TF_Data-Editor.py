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
    page_icon="✍🏽"
  
)

display = Image.open('logo-no-back.png')
col1, col2 = st.columns(2)
col1.image(display, width = 800)



st.title("✍🏽 Data Editor")
#st.caption("This is a demo of the `st.experimental_data_editor`.")

st.write("")

"""Upload & Modify your prophet-formated dataset here if you need!"""

data = st.file_uploader("Choose a file", type=["csv"])

if data is not None:
    df = pd.read_csv(data)
    annotated = st.experimental_data_editor(
        df,
        use_container_width=True,
        num_rows="dynamic",
    )
    st.download_button(
        "⬇️ Download modified file as .csv", annotated.to_csv(), "annotated.csv", use_container_width=True
    )









hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
