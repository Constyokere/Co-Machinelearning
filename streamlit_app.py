import streamlit as st
import pandas as pd
st.title('🎈 Machine Learning App')

st.info('This app builds machine learning models')
df=pd.read_csv("https://github.com/Constyokere/Lungcercancer-dataset/edit/main/Lung%20Cancer%20Dataset.cs")
df
