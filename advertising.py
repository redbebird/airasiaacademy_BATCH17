import streamlit as st
import pandas as pd
import pickle

st.write("""
# Sales Prediction App

This app practically predicts the **Sales** value!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    TV = st.sidebar.slider('TV', 0.7, 296.4, 100.0)
    Radio = st.sidebar.slider('Radio', 0.0, 49.6, 20.0)
    Newspaper = st.sidebar.slider('Newspaper', 0.3, 114.0, 50.)
    data = {'TV': TV,
            'Radio': Radio,
            'Newspaper': Newspaper}
    features = pd.DataFrame(data, index=[0])
    return features

data = user_input_features()

st.subheader('User Input parameters')
#st.write(data)
st.write("TV",data.loc[0].TV)
st.write("Radio",data.loc[0].Radio)
st.write("Newspaper",data.loc[0].Newspaper)
loaded_model = pickle.load(open("Advertising_SVR.h5", "rb"))

prediction = loaded_model.predict(data)

st.subheader('Prediction')
st.write(prediction)
