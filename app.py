import main
from main import rag_chain
import streamlit as st
from langchain.llms import OpenAI


import streamlit as st

# Streamlit interface
st.title('ApiConsulte 🐝🍯')

question = st.text_input("Ask a question about the ApicultureData:")

if st.button("Submit"):
    if question:
        results = rag_chain.invoke({"input": question})
        st.write("Answer:")
        st.write(results["answer"])

        st.write("Context Metadata:")
        st.write(results["context"][0].metadata)
    else:
        st.write("Please enter a question.")
