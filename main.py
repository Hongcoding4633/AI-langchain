# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain_openai import ChatOpenAI

chat_model = ChatOpenAI()

st.title("인공지능 음악")

content = st.text_input("음악 TOP 10 리스트를 제시해주세요.")

if st.button("음악 리스트 요청하기"):
    with st.spinner("음악 리스트 작성 중..."):
        result = chat_model.predict(content + "에 대한 음악 리스트를 작성해줘.")
        st.write(result)