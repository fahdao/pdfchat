import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import langchain

from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

# Initialize text splitter and embeddings
text_splitter = CharacterTextSplitter(
    separator="/n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
)



@st.cache_data(show_spinner=False)
def parse_pdf(pdf):
    text = "".join(page.extract_text() for page in PdfReader(pdf).pages)
    chunks = text_splitter.split_text(text)
    load_dotenv()
    embeddings = OpenAIEmbeddings()
    semantic_document = FAISS.from_texts(chunks, embeddings)
    return semantic_document


def pdfchat():

    docs= ""
    st.set_page_config(page_title="PDF Search")
    st.header("Search within your PDF")

    # upload file
    pdf = st.file_uploader("Upload a PDF file", type="pdf")
    if pdf is None:
        return

    # Parse PDF and create semantic document
    semantic_document = parse_pdf(pdf)

    user_question = st.text_input("Ask what u want from the document buddy")
    if user_question:
        docs = semantic_document.similarity_search(user_question)


    # Load question answering chain and get response
    langchain.verbose = False
    llm = OpenAI()
    chain = load_qa_chain(llm, chain_type="stuff")
    with get_openai_callback() as cb:
        response = chain.run(input_documents=docs, question=user_question)
        print(cb)

    st.write(response)


if __name__ == '__main__':
    pdfchat()
