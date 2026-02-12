# 📊 AI-Driven Customer Feedback Intelligence Engine

An end-to-end **LLM + RAG powered analytics system** that transforms raw customer reviews into structured business insights.

This system allows product teams to:

- Ask natural language questions about customer feedback  
- Retrieve relevant reviews using semantic search  
- Generate AI-powered insights  
- Produce actionable recommendations  
- Evaluate answer quality using embedding-based metrics  

---

## 🚀 System Architecture

```
User Question
      ↓
Preprocessing (RunnableLambda)
      ↓
Query Rewriting (LLM)
      ↓
FAISS Semantic Retrieval
      ↓
RAG Generation (LLM)
      ↓
Evaluation (Relevance + Confidence)
      ↓
Frontend Dashboard
```

---

## 🧠 Core Features

### 🔎 1. Semantic Retrieval (FAISS + Embeddings)
- HuggingFace embedding model  
- Vector search over customer reviews  
- Efficient similarity search using FAISS  

### 🤖 2. LLM-Powered Query Rewriting
Improves retrieval quality by rewriting user queries for better semantic matching.

### 📚 3. Retrieval-Augmented Generation (RAG)
Generates:
- Clear Answer  
- Key Insights  
- Actionable Recommendations  

### 📈 4. LLM Evaluation Layer
Embedding-based evaluation metrics:
- Relevance score (cosine similarity)  
- Confidence labeling (High / Medium / Low)  

### 🌐 5. Full Stack Deployment
- Backend: FastAPI  
- Frontend: Streamlit  
- Deployable on Render  

---

## 🗂 Project Structure

```
AI-Driven-Customer-Feedback-Intelligence-Engine/

├── backend/
│   └── main.py
│
├── chains/
│   ├── preprocessing.py
│   ├── query_rewriter.py
│   ├── retriever_chain.py
│   └── rag_chain.py
│
├── embeddings/
│   └── vector_store.py
│
├── evaluation/
│   ├── relevance.py
│   └── metrics.py
│
├── ingestion/
│   └── fetch_reviews.py
│
├── ui/
│   └── frontend.py
│
├── vectorstore/
│   ├── index.faiss
│   └── index.pkl
│
├── requirements.txt
└── README.md
```

---

## 🛠 Tech Stack

- Python 3.11  
- LangChain  
- HuggingFace Endpoint  
- FAISS  
- FastAPI  
- Streamlit  
- Render Deployment  

---

## 🔧 Local Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/<your-username>/AI-Driven-Customer-Feedback-Intelligence-Engine.git
cd AI-Driven-Customer-Feedback-Intelligence-Engine
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

## ▶️ Run Backend

```bash
uvicorn backend.main:app --reload
```

Open:
```
http://127.0.0.1:8000/docs
```

---

## ▶️ Run Frontend

```bash
streamlit run ui/frontend.py
```

---

## 🌍 Render Deployment

- Environment: Docker  
- Build Command: Leave empty  
- Start Command: Leave empty (Docker handles it)  
- Add Environment Variable:
  - `HUGGINGFACEHUB_ACCESS_TOKEN`

---

## 📊 Example Output

The system generates structured insights including:

- Refined Query  
- Clear Answer  
- Key Insights  
- Actionable Recommendations  
- Relevance Score  
- Confidence Label  

---

## 🎯 Business Value

This system enables:

- Voice of Customer Intelligence  
- Monetization pain point detection  
- Feature sentiment analysis  
- Data-driven product decisions  
- AI-powered customer analytics  

---

## 📈 Why This Project Stands Out

✔ Uses modern LangChain Runnables  
✔ Embedding-based evaluation layer  
✔ Full RAG pipeline  
✔ Production deployment ready  
✔ Modular architecture  
✔ End-to-end AI system  

---

## 👨‍💻 Author

**Manish Mohapatra**

AI Engineer focused on:
- NLP  
- Deep Learning  
- Generative AI  
- Production ML Systems  

---
