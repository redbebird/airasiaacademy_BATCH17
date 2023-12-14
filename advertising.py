import streamlit as st
import pandas as pd
import pickle

st.write("""
# Sales Prediction App

This app practically predicts the **Sales** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    TV = st.sidebar.slider('TV', 4.3, 7.9, 5.4)
    Radio = st.sidebar.slider('Radio', 2.0, 4.4, 3.4)
    Newspaper = st.sidebar.slider('Newspaper', 1.0, 6.9, 1.3)
    data = {'TV': TV,
            'Radio': Radio,
            'Newspaper': Newspaper}
    features = pd.data(data, index=[0])
    return features

data = user_input_features()

st.subheader('User Input parameters')
st.write(data)

loaded_model = pickle.load(open("Advertising_SVR.h5", "rb"))

prediction = loaded_model.predict(data)

st.subheader('Prediction')
st.write(prediction)
