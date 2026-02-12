from fastapi import FastAPI
from chains.preprocessing import get_preprocessor
from chains.query_rewriter import get_query_rewriter
from chains.rag_chain import get_rag_chain
from chains.retriever_chain import get_retriever
from evaluation.metrics import evaluate


app = FastAPI()

preprocessor = get_preprocessor()
rewriter = get_query_rewriter()
retriever = get_retriever()
rag_chain = get_rag_chain(retriever)

@app.get("/")
def home():
    return {"status": "LangChain Review AI Running"}

@app.post("/ask")
def ask(query:str):
    
    cleaned = preprocessor.invoke(query)
    refined = rewriter.invoke({"query" : cleaned})
    answer = rag_chain.invoke(refined)
    
    metrics = evaluate(refined, answer)
    
    return {
        "refined_query" : refined,
        "answer" : answer,
        "metrics" : metrics
    }