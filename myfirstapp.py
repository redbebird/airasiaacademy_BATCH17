import streamlit as st
import numpy as np
import pandas as pd
import time

st.header("My very first lovely Streamlit App")

option = st.sidebar.selectbox(
    'Select a mini project',
     ['Line Chart','Map','T&Cs','Long Process'])

if option=='Line Chart':
    chart_data = pd.DataFrame(
      np.random.randn(20, 5),
      columns=['a', 'b', 'c','d','e'])
    st.line_chart(chart_data)

elif option=='Map':
    map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [5.9804, 116.0735],
    columns=['lat', 'lon'])
    st.map(map_data)

elif option=='T&Cs':
    st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
    show = st.checkbox('I agree the terms and conditions')
    if show:
        st.write(pd.DataFrame({
          'Students': ['John', 'Lofa', 'Siti', 'Amy'],
          'Attendance Status': ['yes', 'yes', 'yes', 'no']
        }))
elif option=='Long Process':
    'Starting a long computation...'

    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(1000):
        latest_iteration.text(f'Iteration {i+5}')
        bar.progress(i + 5)
        time.sleep(0.5)

    '...and now we\'re done!'
