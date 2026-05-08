# 🚀 Enterprise AI Automation Infrastructure: RAG Engine

A production-ready Retrieval-Augmented Generation (RAG) system utilizing Llama 3.3 and FAISS vector databases for automated corporate knowledge management. Developed as a core research project for enterprise AI automation.

## System Architecture & Tech Stack
* **Large Language Model (LLM):** Llama-3.3-70b-versatile (via Groq Cloud)
* **Orchestration:** LangChain (LCEL Architecture)
* **Vector Database:** FAISS (Facebook AI Similarity Search) & ChromaDB (Legacy)
* **Embeddings:** HuggingFace (all-MiniLM-L6-v2)
* **User Interface:** Streamlit 

## Core Features
* **Dynamic Document Intelligence:** Automated extraction and contextual chunking of corporate PDF documents.
* **High-Speed Inference:** Sub-second response latency leveraging Groq Cloud's LPU processing.
* **Context-Aware Retrieval:** Semantic search implementation to ensure precise answers based strictly on internal company data.
* **Cloud Deployment Ready:** Configured for seamless deployment on Streamlit Community Cloud with secure environment variable management.

## Installation & Setup
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Configure your API Key:
   * Create a `.streamlit` directory.
   * Add a `secrets.toml` file containing: `GROQ_API_KEY = "your_groq_api_key"`
4. Run the application: `streamlit run app.py`

*Developed by Rexaldo Dhiya Ulhaq*
*This is my learning journey in building RAG system,so if there is anything that suspicious/inefficient code,im truly sorry*