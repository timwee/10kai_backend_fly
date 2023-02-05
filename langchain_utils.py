from langchain.llms import OpenAI
from langchain.vectorstores.faiss import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, HypotheticalDocumentEmbedder
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

recursive_text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 600,
    chunk_overlap  = 30,
    length_function = len,
)

chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff")

def search_doc(q, docsearch, **kw_args):
    docs = docsearch.similarity_search(q)
    return chain({"input_documents": docs, "question": q}, **kw_args)