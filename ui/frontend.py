import streamlit as st 
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")

st.set_page_config(
    page_title="AI Customer Feedback Intelligence",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI-Driven Customer Feedback Intelligence Engine")
st.markdown("Ask insights about customer reviews using AI + RAG")

query = st.text_input(
    "Enter your question: ",
    placeholder= "What is the most loved feature of thi product?" 
    )

if st.button("Analyze"):
    
    if not query.strip():
        st.warning("Please enter a valid question.")
    
    else:
        with st.spinner("Analyzing customer Feedback..."):
            
            try:
                response = requests.post(
                    f"{BACKEND_URL}/ask",
                    params = {"query": query},
                    timeout = 60
                )
                
                if response.status_code == 200:
                    data = response.json()
                    
                    st.success("Analysis complete ✅")
                    
                    st.subheader("🔎 Refined query")
                    st.write(data.get("refined_query", "N/A"))
                    
                    st.subheader("🧠 AI insights")
                    st.write(data.get("answer", "N/A"))
                    
                    st.subheader("📈 Evaluation metrics")
                    metrics = data.get("metrics", {})
                    st.json(metrics)
                
                else:
                    st.error(f"Backend Error: {response.status_code}")
                    st.write(response.text)
                    
            except Exception as e:
                st.error("Connection Failed ❌")
                st.write(str(e))