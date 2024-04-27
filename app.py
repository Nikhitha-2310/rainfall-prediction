import streamlit as st
import pandas as pd
import pickle
st.image(r"C:\Users\HP\Downloads\images.jpeg",width=700)
st.title("RainFall Prediction 🌧️☔")

with st.sidebar:
    date=st.text_input("Date 📅")
    location=st.text_input("Location 📍")
    MinTemp=st.number_input("Minimum Temperature 🌡️")
    MaxTemp=st.number_input("Maximum Temperature 🌡️")
    Rainfall=st.number_input("Rainfall ☔")
    Evaporation=st.number_input("Evaporation 🌊")
    Sunshine=st.number_input("Sunshine ☀️")
    WindGustDir=st.text_input("WindGustDirl 🍃")
    WindGustSpeed=st.number_input("WindGustSpeed 🍃")
    WindDir9am=st.text_input("WindDir9am 🍃")
    WindDir3pm=st.text_input("WindDir3pm 🍃")
    WindSpeed9am=st.number_input("WindSpeed9am 🍃")
    WindSpeed3pm=st.number_input("WindSpeed3pm 🍃")
    Humidity9am=st.number_input("Humidity9am 🥵")
    Humidity3pm=st.number_input("Humidity3pm 🥵")
    Pressure9am=st.number_input("Pressure9am 🎐")
    Pressure3pm=st.number_input("Pressure3pm 🎐")
    Cloud9am=st.number_input("Cloud9am ☁️")
    Cloud3pm=st.number_input("Cloud3pm ☁️")
    Temp9am=st.number_input("Temp9am 🌡️")
    Temp3pm=st.number_input("Temp3pm 🌡️")
    submit=st.button("Predict")

dict_1={}
if(date and location and MinTemp and MaxTemp and Rainfall and Evaporation and Sunshine and WindGustDir and WindGustSpeed and WindDir9am and WindDir3pm and WindSpeed9am and WindSpeed3pm and Humidity3pm and Pressure9am and Pressure3pm and Cloud9am and Cloud3pm and Temp9am and Temp3pm and submit):
    dict_1['Date']=date
    dict_1['Location']=location
    dict_1['MinTemp']=MinTemp
    dict_1['MaxTemp']=MaxTemp
    dict_1['Rainfall']=Rainfall
    dict_1['Evaporation']=Evaporation
    dict_1['Sunshine']=Sunshine
    dict_1['WindGustDir']=WindGustDir
    dict_1['WindGustSpeed']=WindGustSpeed
    dict_1['WindDir9am']=WindDir9am
    dict_1['WindDir3pm']=WindDir3pm
    dict_1['WindSpeed9am']=WindSpeed9am
    dict_1['WindSpeed3pm']=WindSpeed3pm
    dict_1['Humidity9am']=Humidity9am
    dict_1['Humidity3pm']=Humidity3pm
    dict_1['Pressure9am']=Pressure9am
    dict_1['Pressure3pm']=Pressure3pm
    dict_1['Cloud9am']=Cloud9am
    dict_1['Cloud3pm']=Cloud3pm
    dict_1['Temp9am']=Temp9am
    dict_1['Temp3pm']=Temp3pm
    query_df=pd.DataFrame([dict_1])
    st.write(query_df)


    pipeline=pickle.load(open(r"C:\Users\HP\rainfall_prediction\pipeline.pkl",'rb'))
    gs=pickle.load(open(r"C:\Users\HP\rainfall_prediction\gsmodel.pkl",'rb'))


    def predict(query_df):
        query_df=pipeline.transform(query_df)
        y_pred=gs.predict(query_df)
        return y_pred


    
    output=predict(query_df)
    if(output==1):
        st.subheader('Yes, there is a chance of *Rainfall Tomorrow*')
    else:
        st.subheader('No, there is No chance of *Rainfall Tomorrow*')

else:
    st.subheader('Enter all the features')