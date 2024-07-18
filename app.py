import dotenv
import main
from main import rag_chain
import streamlit as st
from langchain.llms import OpenAI

dotenv.load_dotenv

import streamlit as st

# Streamlit interface
st.title('ApiConsulte   ')

# Sidebar
st.sidebar.title("Information")
st.sidebar.info(
    """
    All the PDFs used in this project were found on Google Scholar or the Embrapa website.
    They are available on my Google Drive, which can be accessed via this link:
    [Google Drive](https://drive.google.com/drive/folders/11mwLsOD2smiMje9oNzDUcgs-9iswpxwd?usp=sharing)
    """
)



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
