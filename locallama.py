# from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from langchain_community.llms import Ollama

## env import

import os 
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


# prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please answer to the questions as best as possible."),
        ("user", "{question}")
    ]
)

# streamlit frame work

st.title("Local Llama chatbot")

question = st.text_input("Ask a question")

# ollama LLM

llm = Ollama(model="llama3", temperature=0.7)

# output parser

output_parser = StrOutputParser()


#chain

chain = prompt | llm | output_parser


if question:
    st.write(chain.invoke({"question":question}))

