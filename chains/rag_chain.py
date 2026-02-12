from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os

load_dotenv()

def get_rag_chain(retriever):

    prompt = ChatPromptTemplate.from_messages([
        ("system",
         """You are a product analyst.
         Use the provided context to answer the question.

         Provide:
         - Clear Answer
         - Key Insights
         - Actionable Recommendations
         """),
        ("human",
         "Context:\n{context}\n\nQuestion:\n{question}")
    ])

    base_llm = HuggingFaceEndpoint(
        repo_id="deepseek-ai/DeepSeek-V3.2",
        huggingfacehub_api_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
    )

    llm = ChatHuggingFace(llm=base_llm)

    output_parser = StrOutputParser()

    chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | output_parser
    )

    return chain
