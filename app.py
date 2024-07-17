import main
from main import rag_chain
import streamlit as st
from langchain.llms import OpenAI


import streamlit as st

# Streamlit interface
st.title('ApiConsulte 🐝🍯')

question = st.text_input("Faça uma pergunta sobre Apicultura no Brasil:")

if st.button("Enviar"):
    if question:
        results = rag_chain.invoke({"input": question})
        st.write("Resposta:")
        st.write(results["answer"])

        st.write("Metadata:")
        st.write(results["context"][0].metadata)
    else:
        st.write("Please enter a question.")
