# 🚀 Enterprise AI Automation Infrastructure: RAG Engine (v1.0.0)

A professional-grade Retrieval-Augmented Generation (RAG) system built with Llama 3.3 and FAISS. This project serves as a stable baseline (v1) for automated corporate knowledge management.

## Current Version: v1.0.0 (Stable)
* **Architecture:** Pure LCEL (LangChain Expression Language) for modularity.
* **Contextual Intelligence:** Advanced conversational memory for multi-turn dialogue.
* **Inference Engine:** Llama-3.3-70b-versatile via Groq LPU.
* **Interface:** Interactive Streamlit UI for seamless document ingestion.

## Tech Stack
* **LLM:** Llama-3.3-70b-versatile
* **Vector DB:** FAISS (In-memory)
* **Embeddings:** HuggingFace `all-MiniLM-L6-v2`
* **Framework:** Streamlit

## 🚀 Roadmap to v2.0.0 (Planned)
Future updates will focus on infrastructure stability and broader file compatibility:
- [ ] **Local Persistence:** Implementing FAISS index saving/loading to prevent data loss.
- [ ] **Multi-Format Ingestion:** Adding support for `.docx` and `.txt` files.
- [ ] **Prompt Optimization:** Refinement of system instructions for higher retrieval accuracy.
- [ ] **UI/UX Enhancement:** Polishing the sidebar and chat aesthetics for a cleaner feel.

## Installation & Usage
1. `git clone https://github.com/rexaldou/ai-automation-infrastructure.git`
2. `pip install -r requirements.txt`
3. Configure `GROQ_API_KEY` in `.streamlit/secrets.toml`.
4. Run: `streamlit run app.py`

*Developed by Rexaldo Dhiya Ulhaq*

*This is my learning journey in building RAG system,so if there is anything that suspicious/inefficient code,im truly sorry*