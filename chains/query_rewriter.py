from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import huggingface_hub
import os
from dotenv import load_dotenv

load_dotenv()

def get_query_rewriter():
    
    prompt = PromptTemplate.from_template(
    """
    Rewrite the query to improve semantic retrieval.
    
    Query: {query}
    Optimized Query:
    """)
    
    llm = huggingface_hub( 
        repo_id = "google/flan-t5-large",
        huggingfacehub_api_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"),
        model_kwargs = {"temperature" : 0.1}
    )
    
    output_parser = StrOutputParser()
    
    return prompt | llm | output_parser

