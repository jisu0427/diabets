import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda_app():
    st.subheader('데이터 분석')

    df = pd.read_csv('data/diabetes.csv')
    st.dataframe(df)

    st.text('Nan 데이터 확인')
    st.dataframe(df.isna().sum())

    st.subheader('각 컬럼별 히스토그램 확인')
    # 'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'
    select_columns = st.selectbox('컬럼을 선택하세요', df.columns)
    bins = st.slider('bin의 갯수 조절',min_value=10, max_value=50)
    fig1 = plt.figure()
    df[select_columns].hist(bins = bins)
    st.pyplot(fig1)

    
'''
#   warning이 뜨긴 하지만 히스토 그램이 뜬다.
    df.hist()
    plt.show()
    st.pyplot()
'''