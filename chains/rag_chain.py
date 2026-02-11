from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.llms import huggingface_hub
import os
from dotenv import load_dotenv

load_dotenv()

def get_rag_chain(retriever):
    
    prompt = PromptTemplate.from_template(
        """"
        You are a product analyst.

        Context:
        {context}

        Question:
        {question}

        Provide:
        - Clear Answer
        - Key Insights
        - Actionable Recommendations
        
        """
    )
    
    llm = huggingface_hub(
        repo_id="google/flan-t5-large",
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
        model_kwargs={"temperature": 0.2}
    )
    
    output_parser = StrOutputParser()
    
    chain = (
        {"context": retriever, "question": RunnablePassthrough()} | prompt | llm | output_parser
    )
    
    return chain