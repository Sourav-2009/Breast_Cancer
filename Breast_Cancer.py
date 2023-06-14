# Winconsen Breast Cancer Dataset

# Loading Libraries 

import streamlit as st
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix


data = load_breast_cancer()

df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

st.title('Breast Cancer')

st.markdown("""Breast cancer is a significant health concern impacting women worldwide. This model provides a comprehensive overview on the emerging role of machine learning in breast cancer detection.""")




st.markdown('<iframe width="560" height="315" src="https://www.youtube.com/embed/KyeiZJrWrys;controls=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
