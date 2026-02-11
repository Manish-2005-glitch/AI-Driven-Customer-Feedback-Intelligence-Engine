from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
import numpy as np
import os

load_dotenv()

embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    task="feature-extraction",
    huggingfacehub_api_token=os.environ.get("HUGGINGFACEHUB_ACCESS_TOKEN")
)

def cosine_similarity(vec1 , vec2):
    vec1 = np.array(vec1).flatten()
    vec2 = np.array(vec2).flatten()
    
    return float(
        np.dot(vec1, vec2) /
        (np.linalg.norm(vec1) * np.linalg.norm(vec2))
    )
    
def relevance_score(question: str, answer: str) -> float:
    
    q_emb = embeddings.embed_query(question)
    a_emb = embeddings.embed_query(answer)
    
    return cosine_similarity(q_emb, a_emb)


