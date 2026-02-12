from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEndpointEmbeddings
import os

def get_retriever():
    
    embeddings = HuggingFaceEndpointEmbeddings(
        model="sentence-transformers/all-MiniLM-L6-v2",
        task="feature-extraction",
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
    )
    
    db = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
    )

    
    return db.as_retriever(search_type = "mmr", search_kwargs = {"k":5})