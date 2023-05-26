import io
from io import BytesIO
import logging
import warnings
from importlib_metadata import version  # python3.8+



# disable FutureWarning/DeprecationWarning from prophet/pandas
# For packages verions control
warnings.simplefilter(action='ignore', category=DeprecationWarning)
warnings.simplefilter(action='ignore', category=FutureWarning)


import streamlit as st
from PIL import Image
import pandas as pd 
import prophet
from prophet.diagnostics import cross_validation, performance_metrics



# Workaround to suppress stdout/stderr output from prophet/pystan
import stdout_suppressor

# disable verbose logging from prophet
logging.getLogger('prophet').setLevel(logging.WARNING)


#buf = BytesIO()
#img.save(buf, format="JPEG")
#byte_im = buf.getvalue()


#-------------------- Prophet forecasting ----------------------------------------------------------------


# A Project by Mangle Yann Houphouet for computer science bsc thesis research 
# 9170214004
# ZUST 

#------------------------------Data Page Backend --------------------------------------------------------------





st.set_page_config(
    page_title="Tinay Forecaster",
    page_icon="🔮"

)

display = Image.open('logo-no-back.png')
col1, col2 = st.columns(2)
col1.image(display, width = 800)


st.title("🔮 Data Forecaster")
st.markdown("## Data Upload and Forecasting")

    # Upload the dataset and save as csv
st.markdown(" Upload a csv file for analysis. Don't forget the suitable format for a prophet analysis!") 
st.write("\n")
    
    # Code to upload a single file 
   
uploaded_file = st.file_uploader("Choose a file", type = ['csv'])


if uploaded_file is not None:
    # read the csv file
    df = pd.read_csv(uploaded_file)
    
    if st.button("Forecast ?"):
        if len(df.columns==2) or (df.columns.values==['ds' ,'y']) :


                # create prophet model
            model = prophet.Prophet()

                # this is a workaround to suppress stdout/stderr output from pystan
                # if you want to see the output, comment out the following line
            with stdout_suppressor.suppress_stdout_stderr():
                model.fit(df)  # fit the model

                # prepare the dataframe for the prediction
            future = model.make_future_dataframe(periods=365)
            
            st.subheader("Future DataFrame Timestamps - Tail")
            st.table(future.tail())



                # make the prediction after fitting with the model
            forecast = model.predict(future)
            df_forecast = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper', 'trend']].tail()
            st.subheader("Future DataFrame Predictions - Tail")
            st.table(df_forecast)


            # plot the predictions
            st.header("Matplotlib Plots")
            st.subheader("Prophet Predictions")
            st.pyplot(model.plot(forecast, uncertainty=True,include_legend=True))

            # plot the components
            st.subheader("Prophet Components")
            st.pyplot(model.plot_components(forecast, uncertainty=True))
            

            with st.spinner('Computing '):
            #Perform cross-validation
                st.subheader("Cross-validation Diagnostics")
            # Split the dataset into a training and testing set
            #train_size = int(len(df) * 0.8)
            #train_df = df[:train_size]
            #test_df = df[train_size:]
    
                df_cv = cross_validation(
                     model,
                     initial='730 days',
                     horizon='365 days',
                     period='180 days'
                    )
                st.table(df_cv.head())

            # perform metrics
                st.subheader("Compute performance metrics")
                df_metrics = performance_metrics(df_cv)
                st.code(df_metrics)

        else:
            st.error("Adapt the dataframe for the prediction or go to Data Editor")
    
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
