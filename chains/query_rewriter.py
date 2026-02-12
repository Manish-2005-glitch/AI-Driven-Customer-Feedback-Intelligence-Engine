from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os

load_dotenv()

def get_query_rewriter():

    prompt = ChatPromptTemplate.from_messages([
        ("system", "Rewrite the query to improve semantic retrieval."),
        ("human", "Original Query: {query}\nOptimized Query:")
    ])

    base_llm = HuggingFaceEndpoint(
        repo_id="deepseek-ai/DeepSeek-V3.2",
        huggingfacehub_api_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
    )

    llm = ChatHuggingFace(llm=base_llm)

    output_parser = StrOutputParser()

    return prompt | llm | output_parser
