from stack_predict_page import show_stack_predict_page
from cyber_predict_page import show_cyber_predict_page
import streamlit as st



#show_cyber_predict_page()

st.sidebar.markdown("[Ana Sayfa](https://www.salaryprediction.site)")
page = st.sidebar.selectbox("Lütfen bir veri seti seçiniz",("Siber Güvenlik Veri Seti","StackOverFlow Anketi Veri Seti"))
if page =="Siber Güvenlik Veri Seti":
    show_cyber_predict_page()
elif page== "StackOverFlow Anketi Veri Seti":
    show_stack_predict_page()

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)