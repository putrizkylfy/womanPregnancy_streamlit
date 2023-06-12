import pickle
import streamlit as st

#membaca model
womanPregnancy_model = pickle.load(open('womanPregnancy.sav', 'rb'))

#judul web
st.title('Memprediksi Resiko Wanita Hamil')

#mengatur pembagian kolom
col1, col2 = st.columns(2)

with col1: 
    Age = st.text_input ('input umur')

with col2:
    SystolicBP = st.text_input ('input tekanan nilai SystolicBP')

with col1:
    DiastolicBP = st.text_input ('input nilai DiastolicBP')

with col2:
    BS = st.text_input ('input nilai Blood Pressure')

with col1:
    BodyTemp = st.text_input ('input nilai BodyTemp')

with col2:
    HeartRate = st.text_input('input nilai HeartRate')

#code mulai predict
womanPregnancy_diagnosis= ''

#membuat button untuk memulai predict
if st.button('Test Predict Woman Pregnancy'):
    womanPregnancy_prediction = womanPregnancy_model.predict([[Age, SystolicBP, DiastolicBP, BS, BodyTemp, HeartRate]])
    
    if(womanPregnancy_prediction[0] == 0):
        womanPregnancy_diagnosis = 'Wanita hamil tersebut memiliki resiko yang kecil'
        if(womanPregnancy_prediction[-1] == 1):
            womanPregnancy_diagnosis = 'Wanita hamil tersebut memiliki resiko yang sedang'
    else : 
        womanPregnancy_diagnosis = 'Wanita hamil tersebut memiliki resiko'
    
    st.success(womanPregnancy_diagnosis)
