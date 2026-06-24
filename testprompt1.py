from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openrouter import ChatOpenRouter
import streamlit as st
from setting import settings

llm_cohere = ChatOpenRouter(
    model='cohere/north-mini-code:free',
    api_key=settings.OPENROUTER_API_KEY)


st.header('Reasearch tool')

user_input = st.text_input('Enter your prompt')

if st.button('Summerize'): 
    result = llm_cohere.invoke(user_input)
    st.write(result.content)