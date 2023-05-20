import streamlit as st
import numpy as np
import pandas as pd
import pickle

def load_model():
    with open('saved_steps_two_two.pkl','rb') as file:
        data = pickle.load(file)
    return data

data = load_model()



    
regressor = data["model"]
le_employee_residence = data["le_employee_residence"]
le_job_title = data["le_job_title"]
le_experience = data["le_experience"]


def show_cyber_predict_page():
    
    experience=(
        'EN',
        'SE',
        'MI',
        'EX'
    )
    exp_turkce ={
        "Junior" :'EN',
        "Senior":'SE',
        "Middle":'MI',
        "Sözleşmeli":'EX'
    }
    
    employee_residence = (
        'DE', 'US', 'CY', 'BA', 'GB', 'CA', 'IN', 'FR', 'ES', 'BR', 'BW',
        'NL', 'CH', 'DK', 'CL', 'SG', 'AU', 'IT', 'PK', 'GR', 'GH', 'AZ',
        'RO', 'AR', 'DZ', 'AF', 'SI', 'HR', 'SE', 'HU', 'ET', 'MX', 'IL',
        'IE', 'PL', 'CR', 'JP', 'PT', 'NG', 'AE', 'NO', 'CZ', 'ID', 'EE',
        'KG', 'KE', 'BG', 'IR', 'NZ', 'BE', 'ZA', 'AT', 'LU', 'EG', 'TW',
        'VN', 'SA', 'LT', 'RU', 'TR'
    )
    e_r_turkce = {
        'Afganistan': 'AF',
        'Almanya': 'DE',
        'Arjantin': 'AR',
        'Avustralya': 'AU',
        'Avusturya': 'AT',
        'Azerbaycan': 'AZ',
        'Belçika': 'BE',
        'Birleşik Arap Emirlikleri': 'AE',
        'Birleşik Krallık': 'GB',
        'Bosna-Hersek': 'BA',
        'Botsvana': 'BW',
        'Brezilya': 'BR',
        'Bulgaristan': 'BG',
        'Çek Cumhuriyeti': 'CZ',
        'Cezayir': 'DZ',
        'Danimarka': 'DK',
        'Endonezya': 'ID',
        'Etiyopya': 'ET',
        'Fransa': 'FR',
        'Gana': 'GH',
        'Güney Afrika': 'ZA',
        'Hindistan': 'IN',
        'Hollanda': 'NL',
        'Hırvatistan': 'HR',
        'İran': 'IR',
        'İrlanda': 'IE',
        'İspanya': 'ES',
        'İsrail': 'IL',
        'İsveç': 'SE',
        'İsviçre': 'CH',
        'İtalya': 'IT',
        'Japonya': 'JP',
        'Kanada': 'CA',
        'Kenya': 'KE',
        'Kıbrıs': 'CY',
        'Kırgızistan': 'KG',
        'Kosta Rika': 'CR',
        'Litvanya': 'LT',
        'Lüksemburg': 'LU',
        'Macaristan': 'HU',
        'Meksika': 'MX',
        'Mısır': 'EG',
        'Nijerya': 'NG',
        'Norveç': 'NO',
        'Pakistan': 'PK',
        'Portekiz': 'PT',
        'Romanya': 'RO',
        'Rusya': 'RU',
        'Singapur': 'SG',
        'Slovenya': 'SI',
        'Suudi Arabistan': 'SA',
        'Tayvan': 'TW',
        'Türkiye': 'TR',
        'Vietnam': 'VN',
        'Yeni Zelanda': 'NZ',
        'Yunanistan': 'GR',
        'İran': 'IR'
    }
    
    
    
    job_title= ('Information Security Officer', 'Security Officer',
       'Security Engineer', 'Penetration Testing Engineer',
       'Security Analyst', 'Security Consultant',
       'Network Security Engineer', 'Penetration Tester',
       'DevSecOps Engineer', 'Security Specialist',
       'Cloud Security Engineer', 'Security Operations Engineer',
       'Head of Information Security',
       'Chief Information Security Officer', 'Cyber Security Analyst',
       'Information Security Manager', 'Network and Security Engineer',
       'Threat Hunter', 'Information Security Compliance Lead',
       'Digital Forensics Analyst',
       'Information Security Compliance Analyst', 'Cyber Threat Analyst',
       'Cyber Security Consultant', 'IT Security Engineer',
       'Cyber Program Manager', 'IT Security Analyst',
       'Security Researcher', 'Application Security Specialist',
       'Security Incident Response Engineer', 'Ethical Hacker',
       'IT Security Manager', 'Application Security Engineer',
       'Vulnerability Analyst', 'Cyber Security Engineer',
       'Information Security Analyst',
       'Principal Application Security Engineer',
       'Cyber Security Architect', 'SOC Analyst',
       'Cyber Threat Intelligence Analyst',
       'Information Security Specialist',
       'Director of Information Security', 'Threat Intelligence Analyst',
       'Cloud Security Engineering Manager',
       'Application Security Analyst', 'Data Security Analyst',
       'Detection Engineer', 'Principal Security Engineer',
       'Information Systems Security Engineer',
       'Staff Application Security Engineer',
       'Information Security Engineer',
       'Information Security Compliance Manager',
       'Vulnerability Management Engineer', 'Azure Security Engineer',
       'Security Operations Analyst', 'DevOps Security Engineer',
       'Security DevOps Engineer', 'Vulnerability Researcher',
       'Computer Forensic Software Engineer', 'Incident Response Analyst',
       'Cloud Security Architect', 'Product Security Engineer',
       'Lead Security Engineer', 'Incident Response Manager',
       'Information Security Architect', 'Cyber Security Specialist',
       'Cyber Security Researcher', 'Infrastructure Security Engineer',
       'Threat Hunting Lead', 'Incident Response Lead',
       'Head of Security', 'Corporate Security Engineer',
       'Security Engineering Manager', 'Staff Security Engineer',
       'Threat Intelligence Response Analyst',
       'Offensive Security Engineer', 'Enterprise Security Engineer',
       'Privacy Manager', 'Cyber Security Training Specialist',
       'IAM Engineer', 'Principal Cloud Security Engineer',
       'Lead Information Security Engineer',
       'Corporate Infrastructure Security Engineer', 'Security Officer 3',
       'Software Security Engineer', 'Lead Application Security Engineer',
       'Concierge Security Engineer')
    
    
    st.title("Siber Güvenlik Maaş Tahmini")
    st.write("""### Lütfen tahmin yapmak için aşağıdaki boşlukları doldurunuz.""")
    e_residence = st.selectbox("Çalışan Konumu", list(e_r_turkce.keys()))
    j_title = st.selectbox("Meslek", job_title)
    exp = st.selectbox("Deneyim", list(exp_turkce.keys()))
    
    experience_ingilizce = exp_turkce[exp]
    e_r_ing = e_r_turkce[e_residence]
    
    ok = st.button("Hesapla")
    if ok:
        X= np.array([[experience_ingilizce,j_title,e_r_ing,]])
        
        X[:, 0] = le_experience.transform(X[:,0])
        X[:, 1] = le_job_title.transform(X[:,1])
        X[:, 2] = le_employee_residence.transform(X[:,2])
        #X = X.astype(float)
        
        salary = regressor.predict(X)
        st.subheader(f"Tahmini maaş: {salary[0]:.0f} dolar")
        st.write("Bu hesaplama tekniğinde Kaggle.com'daki Cyber_Salaries isimli veri seti baz alınmış olup, random forest regressor ile makine öğrenmesi modeli uygulanmıştır.")
    
    
    