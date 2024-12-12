# from dotenv import load_dotenv
# load_dotenv()
import os

import streamlit as st
from langchain_openai import ChatOpenAI

# Streamlit secrets에서 API 키 가져오기
try:
    openai_api_key = st.secrets["OPENAI_API_KEY"]
except:
    openai_api_key = "your-api-key-here"

# ChatOpenAI 인스턴스 생성 시 API 키 전달
chat_model = ChatOpenAI(api_key=openai_api_key, 
                        model="gpt-3.5-turbo",
                        temperature=0)

st.title("인공지능 음악")

content = st.text_input("음악 TOP 10 리스트를 제시해주세요.")

if st.button("음악 리스트 요청하기"):
    with st.spinner("음악 리스트 작성 중..."):
        result = chat_model.predict(content + "에 대한 음악 리스트를 작성해줘.")
        st.write(result)