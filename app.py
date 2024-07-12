from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser


import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()


os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
## Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="True"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")




## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a brave assistant. Please give smartest response to the user querries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('Langchain Demo with Llama3')
input_text=st.text_input("search the topic you want")


## meta llama3 LLM by using groq api

llm=ChatGroq(model="llama3-70b-8192")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
