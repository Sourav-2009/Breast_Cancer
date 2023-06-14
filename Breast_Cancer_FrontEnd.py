# Winconsen Breast Cancer Dataset

# Loading Libraries 

import streamlit as st

st.set_page_config(
    page_title="Introduction",
    page_icon="♋",
)

#Background image
import base64
def add_bg_from_local(cry):
    with open(cry, "rb") as cry:
        encoded_string = base64.b64encode(cry.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: 1024x768
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('green.jpg') 
# ===================================


st.write("""<h1 style='color: red; padding: 5px; text-align: center; background-color: rgba(255,255,0,0.5);'>Breast Cancer</h1><hr>""", unsafe_allow_html=True)

# Introduction
st.markdown("""<p style="color:#f2f3f4;font-weight:bolder;background-color:rgba(255,0,0,0.5);padding:50px">Breast cancer is a significant health concern impacting women worldwide. This model provides a comprehensive overview on the emerging role of machine learning in breast cancer detection.</p>""",unsafe_allow_html=True)

# Video Information
st.markdown('<iframe width="560" height="315" src="https://www.youtube.com/embed/KyeiZJrWrys;controls=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

# ====================================================================

st.markdown("""<h1 style="font-size:50px:padding:15px;background-color:white;>Under Construction 🚧🏗</h1>""",unsafe_allow_html=True)
