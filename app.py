import streamlit as st
from stack_predict_page import show_stack_predict_page
from cyber_predict_page import show_cyber_predict_page
import urllib3.contrib.pyopenssl


urllib3.contrib.pyopenssl.inject_into_urllib3()

#show_cyber_predict_page()

st.sidebar.markdown("[Ana Sayfa](http://www.salaryprediction.site)")
page = st.sidebar.selectbox("Lütfen bir veri seti seçiniz",("Siber Güvenlik Veri Seti","StackOverFlow Anketi Veri Seti"))
if page =="Siber Güvenlik Veri Seti":
    show_cyber_predict_page()
elif page== "StackOverFlow Anketi Veri Seti":
    show_stack_predict_page()