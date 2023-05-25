import streamlit as st
import numpy as np
import joblib
import math



def run_app_ml():
    st.subheader('자동차 구매 금액 예측')

    #성별, 나이, 연봉, 카드빚, 순자산을 유저한테서 입력받음

    
    gender = st.radio('성별 선택', ['남자','여자'])
    if gender =='남자':
        gender = 0
    else : 
        gender = 1

    age = st.number_input('나이 입력', 18, 100)
    salary = st.number_input('연봉 입력', 5000, 1000000)
    debt = st.number_input('카드 빚 입력', 0, 1000000)
    worth = st.number_input('자산 입력', 1000, 10000000)

     #버튼을 누르면 예측한 금액을 표시한다.
    if st.button('금액 예측'):
        new_data = np.array([gender, age, salary, debt, worth])
        new_data = new_data.reshape(1,5) #1차원을 2차원으로 
  
        regressor = joblib.load('model/regressor.pkl')#파일불러오기해서 regressor저장
 
        y_pred = regressor.predict(new_data)
        print(y_pred)
   
        # st.text(y_pred)
        #28220달러짜리 차량 구매 가능합니다.
        print(y_pred[0])

        price = round(y_pred[0])

        print(str(price)+'달러짜리 차량 구매 가능합니다.')
        print(f'{price}달러짜리 차량 구매 가능합니다.')
        print('{}달러짜리 차량 구매 가능합니다.'.format(price))

        st.text(f'{price}달러짜리 차량 구매 가능합니다.')
        # st.subheader(f'{price}달러짜리 차량 구매 가능합니다.')



