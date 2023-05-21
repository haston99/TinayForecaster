import streamlit as st
import io
import logging
import warnings
from PIL import Image
from importlib_metadata import version  # python3.8+

st.set_page_config(
    page_title="Tinay Forecaster",
    page_icon="🕹"

)

display = Image.open('https://github.com/haston99/TinayForecaster/blob/master/logo-no-back.png.png')
col1, col2 = st.columns(2)
col1.image(display, width = 800)

st.title("Home page")
st.sidebar.success("Navigate above 👆🏽")

st.markdown(''' A web app for time-series-forecasting trained on facebook model **Prophet**.
Load any prophet formated csv dataset and analyze, visualize and predict the future trends !
''')
st.subheader("Prophet Version")
st.markdown(f'Currently used `prophet` library version is `{version("prophet")}`')
st.markdown('''---''')
st.subheader("Other libraries Version")
st.markdown(f'The `cython` version used in this project is `{version("cython")}`')
st.markdown(f'The `streamlit` version used in this project is `{version("streamlit")}`')
st.markdown(f'The `matplotlib` version used in this project is `{version("matplotlib")}`')
st.markdown(f'The `numpy` version used in this project is `{version("numpy")}`')




hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
