# ApiConsult 🐝🍯
## A Data QA System using LangChain Applied to Apiculture in Brazil


This project provides a question-answering (QA) system for apiculture (beekeeping) data using the Langchain framework and OpenAI's GPT-4 model. The system processes PDF documents containing apiculture data, creates embeddings, and uses a retrieval-augmented generation (RAG) approach to answer user questions based on the provided documents. Additionally, a Streamlit interface allows users to interact with the QA system easily.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Additional Information](#additional-information)


## Features

- Load and process PDF documents using Langchain.
- Create text embeddings with OpenAI's GPT-4.
- Implement a retrieval-augmented generation (RAG) approach.
- Interactive Streamlit interface for user questions.
- Provides concise answers and context metadata.
- Sidebar with information about PDF sources and a link to the data.

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Install Dependencies

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/apicultura-RAG
   cd apicultura-RAG

2. Install required Python packages:
   ```bash
   pip install -r requirements.txt

## Usage

1. Place your PDF documents in the ApicultureData folder.

2. Run the Streamlit app:
    ```bash
    streamlit run app.py

3. Open the Streamlit app in your web browser. You should see an interface to ask questions about the apiculture data.

4. Enter your question in the text input field and click the "Submit" button. The system will provide an answer and the context metadata.

## Additional Information

### PDF Sources
All the PDFs used in this project were found on Google Scholar or the Embrapa website (Empresa Brasileira de Pesquisa Agropecuária). They are available on my Google Drive, which can be accessed via this link: [Google Drive](https://drive.google.com/drive/folders/11mwLsOD2smiMje9oNzDUcgs-9iswpxwd?usp=sharing)

### Language
Please, note that the PDFs used are in Portuguese. This ensures accessibility to Brazilian communities that may not speak English.


