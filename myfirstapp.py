import streamlit as st
import numpy as np
import pandas as pd

st.header("My very first lovely Streamlit App")

st.write('Before you continue, please read the [Terms and Conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
show = st.checkbox('I shall agree the terms and conditions')
if show:
    st.write(pd.DataFrame({
    'Students': ['John', 'Lofa', 'Siti', 'Amy'],
    'Attendance Status': ['yes', 'yes', 'yes', 'no']
    }))
