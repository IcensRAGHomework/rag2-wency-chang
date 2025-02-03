from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=0
    )
    chunks = text_splitter.split_documents(documents)
    if chunks:
        return chunks[-1]
    else:
        return None

def hw02_2(q2_pdf):
    loader = PyPDFLoader(q2_pdf)
    documents = loader.load()

    full_text = '\n'.join(doc.page_content for doc in documents)

    text_splitter = RecursiveCharacterTextSplitter(chunk_overlap=0, chunk_size=2, separators=[r'(?=\n\s*第\s.*(?:條|章).*)'], is_separator_regex=True)
    split_docs = text_splitter.split_text(full_text)
    return len(split_docs)
