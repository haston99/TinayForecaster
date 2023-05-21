import streamlit as st
import io
from PIL import Image





#-------------------- Prophet forecasting ----------------------------------------------------------------


# A Project by Mangle Yann Houphouet for computer science bsc thesis research 
# 9170214004
# ZUST 

#------------------------------Data Page Backend ------------------------------------


st.set_page_config(
    page_title="Tinay Forecaster",
    page_icon="🕹"

)


display = Image.open('logo-no-back.png')
col1, col2 = st.columns(2)
col1.image(display, width = 800)


st.title("About App")

st.write("")

""" Here is some explanations on how to interpret the forecast results for non Data-Analyst or beginner user!"""

st.subheader("Future DataFrame Prediction")
st.markdown(f'As we know, the prediction are made based on the 5 last rows of the time series data. yhat is the prediction, yhat_lower, and yhat_upper are the uncertainty levels(it basically means the prediction and actual values can vary within the bounds of the uncertainty levels). Next up we have a trend that shows the long-term growth, shrink, or stagnancy of the data, trend_lower, and trend_upper is the uncertainty levels.')

st.subheader("Future DataFrame Prediction")
st.markdown(f'The light blue is the uncertainty level(yhat_upper and yhat_lower), the dark blue is the prediction(yhat) and the black dots are the original data. We can see that predicted data are very close to the actual data. It is safe to say that the predictions are close to accurate.')




hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
