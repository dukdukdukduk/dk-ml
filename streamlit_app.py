import streamlit as st
import pandas as pd

st.title('🗿 App Testing')

st.write('1 2 1 2 mic check, mic check!')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('aimag_data.csv')
  df

  st.write('**X**')
  X = df.drop('Centre', axis = 1)
  X

  st.write('**y**')
  y = df.Centre
  y
