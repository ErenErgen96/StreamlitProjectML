import streamlit as st
import numpy as np
import pandas as pd
import pickle

def load_model():
    with open('saved_steps.pkl','rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_stack_predict_page():
    
    turkish_countries = {
    'Büyük Britanya': 'Great Britain',
    'İsrail': 'Israel',
    'Hollanda': 'Netherlands',
    'Amerika Birleşik Devletleri': 'United States of America',
    'Avusturya': 'Austria',
    'İtalya': 'Italy',
    'Kanada': 'Canada',
    'Almanya': 'Germany',
    'Polonya': 'Poland',
    'Fransa': 'France',
    'Brezilya': 'Brazil',
    'İsveç': 'Sweden',
    'İspanya': 'Spain',
    'Türkiye': 'Turkey',
    'Hindistan': 'India',
    'İsviçre': 'Switzerland',
    'Avustralya': 'Australia',
    'Rusya Federasyonu': 'Russian Federation'
    }
    

    
    turkish_educations = {
    'Yüksek Lisans': 'Master’s degree',
    'Lisans': 'Bachelor’s degree',
    'Lisans Eğitimi Yok': 'Less than a Bachelors',
    'Lisansüstü': 'Post grad'
}

    
    st.title("Yazılımcı Maaş Tahmini")
    st.write("""### Lütfen tahmin yapmak için aşağıdaki boşlukları doldurunuz.""")
    country = st.selectbox("Ülke", list(turkish_countries.keys()))
    education = st.selectbox("Öğrenim Seviyesi", list(turkish_educations.keys()))
    experience = st.slider("Deneyim Yılı",0,40,3)
    
    english_country = turkish_countries[country]
    english_education = turkish_educations[education]

    
    ok = st.button("Hesapla")
    if ok:
        #st.write("Seçilen Ülke (İngilizce):",english_country, english_education),turkish_educations
        X= np.array([[english_country,english_education,experience]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)
        
        salary = regressor.predict(X)
        st.subheader(f"Yıllık tahmini gelir: {salary[0]:.0f} dolar")
        st.write("Bu hesaplama tekniğinde StackOverFlow'un yazılımcılar için yaptığı anketten elde edilen veri seti baz alınmış olup,decision tree regressor ile makine öğrenmesi modeli uygulanmıştır.")

    



