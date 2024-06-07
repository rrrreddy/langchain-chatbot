from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv


load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

## Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")



## Prompt template

prompt = ChatPromptTemplate.from_messages(
    [("system", "You are a helpfull assistant. You help people with their questions."),

    ("user", "Question:{question}")
    ]
)


## steamlit framework

st.title("chatbot")

question = st.text_input("Ask a question")


# LLM

llm = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo")

#output parser 
output_parser = StrOutputParser()


# chain

chain = prompt|llm|output_parser


if question:
    st.write(chain.invoke({"question": question}))




