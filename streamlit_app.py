import streamlit as st
import pandas as pd
st.title('🎈 Machine Learning App')

st.info('This app builds machine learning models')
df=pd.read_csv("Lung Cancer Dataset.csv")
df
