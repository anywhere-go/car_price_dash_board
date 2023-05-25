import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_app_eda():
    st.subheader('데이터 분석')

    df = pd.read_csv('data/Car_Purchasing_Data.csv', encoding ='ISO-8859-1')#한글 처리 encoding

    print(df)

    if st.checkbox('데이터 프레임 보기'):
        st.dataframe(df)

    st.subheader('기본 통계 데이터')
    st.dataframe(df.describe()) #df.describe() 불러오기

    st.subheader('최대 / 최소 데이터 확인하기')

    column = st.selectbox('컬럼을 선택하세요.', df.columns[3:]) # 3번째 컬럼 Gender부터 끝까지 슬라이싱
    st.text('최대 데이터')
    st.dataframe(df.loc[df[column] == df[column].max(),]) #"Age"->column 변수로 바꿈
    st.text('최소 데이터')
    st.dataframe(df.loc[df[column] == df[column].min(),]) #최소값

    #유저 컬럼선택 빈 선택
    st.subheader('컬럼 별 히스토그램')
    column = st.selectbox('히스토그램 확인할 컬럼을 선택하세요.', df.columns[3:])
    bins = st.number_input('빈의 갯수를 입력하세요.', 10, 30, 20) #기본 20개 10개부터 30개

    fig = plt.figure()
    df[column].hist(bins =bins)
    # plt.show() #주피터용

    plt.title(column +' Histogram')
    plt.xlabel(column)
    plt.ylabel('count')

    st.pyplot(fig)

    st.subheader('상관 관계 분석')

    column_list = st.multiselect('상관분석 하고 싶은 컬럼을 선택하세요.', df.columns[3:])
    print(column_list)
    
    # df[column_list].corr()  #원하는 컬럼리스트 상관관계 df[['Age','gender']]
    if len(column_list) >= 2:    #유저가 2개이상 입력했을 때 그림그리기 
        fig2 = plt.figure()
        sns.heatmap(data= df[column_list].corr() , 
                annot=True, vmin=-1, vmax=1, cmap='coolwarm',
                fmt='.2f', linewidths =0.5)
        st.pyplot(fig2)