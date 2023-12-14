import streamlit as st
import numpy as np
import pandas as pd

st.header("My very first lovely Streamlit App")

option = st.sidebar.selectbox(
    'Select a mini project',
     ['Line Chart','Map','T&Cs'])

if option=='Line Chart':
    chart_data = pd.DataFrame(
      np.random.randn(20, 3),
      columns=['a', 'b', 'c'])
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
