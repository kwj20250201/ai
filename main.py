#from dotenv import load_dotenv
#import os
#load_dotenv()
#os.environ



def google_navtive():
    import google.generativeai as gai    
    gai.configure(api_key=os.environ['API_KEY'])
    model=gai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content('hi')
    print(response)

def openai():
    from langchain.chat_models import ChatOpenAI
    model=ChatOpenAI()
    result=model.predict('hi')
    print(result)

from langchain_google_genai import ChatGoogleGenerativeAI
model = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        # other params...
)


import streamlit as st
st.title('인공지능 시인')
content=st.text_input('시의 주제를 제시해주세요.')

if st.button('시작 성 요청하기'):
    with st.spinner('작성 중...'):
        result=model.predict(content+'에 대한 시를 써줘')
        st.write(result)



