from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.schema import Document
import pinecone
from langchain_openai import AzureOpenAIEmbeddings
from pypdf import PdfReader
from langchain_community.vectorstores import Pinecone
from langchain_openai import AzureChatOpenAI
from langchain.chains.summarize import load_summarize_chain
#from langchain-.llms import HuggingFaceHub
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os
os.environ["OPENAI_API_VERSION"] = "2023-12-01-preview"
os.environ["AZURE_OPENAI_ENDPOINT"] = os.getenv("AZURE_OPENAI_ENDPOINT")
os.environ["AZURE_OPENAI_API_KEY"] = os.getenv("AZURE_OPENAI_API_KEY")
import time


def get_pdf_text(pdf_doc):
    text = ""
    pdf_reader = PdfReader(pdf_doc)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


def create_docs(user_pdf_list, unique_id):
    docs=[]
    for filename in user_pdf_list:
        
        chunks=get_pdf_text(filename)
        docs.append(Document(
            page_content=chunks,
            metadata={"name": filename.name,"id":filename.file_id,"type=":filename.type,"size":filename.size,"unique_id":unique_id},
        ))

    return docs

def create_embeddings_load_data():
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    embeddings = AzureOpenAIEmbeddings(model="resume-ranking")  # Initialize AzureOpenAIEmbeddings with the API key
    return embeddings


def push_to_pinecone(pinecone_apikey,pinecone_environment,pinecone_index_name,embeddings,docs):
    load_dotenv()
    
    docsearch = PineconeVectorStore.from_documents(docs, embeddings, index_name=pinecone_index_name)

def pull_from_pinecone(pinecone_api_key,pinecone_environment,pinecone_index_name,embeddings):
    load_dotenv()
    print("20secs delay...")
    time.sleep(20)

    index_name = pinecone_index_name

    index = Pinecone.from_existing_index(index_name, embeddings)
    return index

def similar_docs(query,k,pinecone_api_key,pinecone_environment,pinecone_index_name,embeddings,unique_id):
    load_dotenv()
    index_name = pinecone_index_name

    index = pull_from_pinecone(pinecone_api_key,pinecone_environment,index_name,embeddings)
    similar_docs = index.similarity_search_with_score(query, int(k),{"unique_id":unique_id})
    #print(similar_docs)
    return similar_docs

def get_summary(current_doc):
    load_dotenv()
    llm = AzureChatOpenAI(
        azure_deployment="gpt4-demetrius",  # or your deployment
        api_version="2023-06-01-preview",  # or your api version
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )  
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.run([current_doc])

    return summary