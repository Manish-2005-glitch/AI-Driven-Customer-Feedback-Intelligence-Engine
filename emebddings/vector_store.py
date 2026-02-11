from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_core.documents import Document
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def build_store():
    df =pd.read_csv("review.csv")
    
    docs = [
        Document(
            page_content=row["review"],
            metadata = {"rating": row["rating"],
                        "date": row["date"]}
        )
        for _,row in df.iterrows()
    ]
    
    embeddings = HuggingFaceEndpointEmbeddings(
        model="sentence-transformers/all-MiniLM-L6-v2",
        task="feature-extraction"
    )
    
    db = FAISS.from_documents(docs, embeddings)
    
    os.makedirs("vectorstore",exist_ok =True )
    db.save_local("vectorstore")
    
    print("vector store built.")
    
if __name__ == "__main__":
    build_store()