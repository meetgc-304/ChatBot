import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load the .env file
load_dotenv()

# --- MAPPING YOUR .ENV NAMES ---
# We take your custom name and assign it to the environment variable LangChain looks for
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# --- MODEL SETUP ---
# In March 2026, 'gemini-1.5-flash' and 'gemini-3-flash' are outdated/preview.
# 'gemini-3.1-flash-lite-preview' is the current stable choice for free tier.
llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview")

# --- PROMPT & CHAIN ---
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "Question: {question}"),
])

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# --- STREAMLIT UI ---
st.title("Gemini Chatbot🤵‍♂️")
input_text = st.text_input("Ask your query:")

if input_text:
    if not os.environ.get("GOOGLE_API_KEY"):
        st.error("Error: GEMINI_API_KEY not found in .env file!")
    else:
        try:
            response = chain.invoke({"question": input_text})
            st.write(response)
        except Exception as e:
            st.error(f"Failed to call Gemini: {e}")
