import streamlit as st
import pandas as pd
import numpy as np

# To run this app type
#
# streamlit run test.py
#
# in the terminal

st.title('Test Streamlit App')

# This is a sample array of pairs of numbers, each pair is to be rendered as a row
frameData = [[1,2],[3,4], [5,6]]

df = pd.DataFrame(
    frameData,
    columns=('Column %d' % i for i in range(2)))

st.dataframe(df)  # Same as st.write(df)