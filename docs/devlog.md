# 📜 Development Log: AI Automation Infrastructure

This document tracks the technical progression, architectural decisions, and troubleshooting history of the Enterprise RAG Engine project.

## Phase 1: LLM Engine Integration (2026-04-27)
* **Objective:** Establish environment connectivity to the LLM (Llama 3.1) via Groq Cloud.
* **Actions:**
  * Initialized `ChatGroq` utilizing the `langchain-groq` library.
  * Configured API key authentication via `os.environ`.
* **Troubleshooting:**
  * Encountered `BadRequestError` (Error 400).
  * Analysis revealed the `llama3-8b-8192` model was decommissioned. Resolved by migrating to `llama-3.1-8b-instant`, restoring system stability and achieving low-latency inference.

## Phase 2: RAG Architecture & Dependency Management (2026-04-28)
* **Objective:** Construct the RAG ecosystem utilizing LangChain and ChromaDB.
* **Actions:**
  * Configured `HuggingFaceEmbeddings` for vector database processing.
  * Generated a local knowledge base (corporate policies and IT support procedures).
  * Executed a complete paradigm shift from legacy `langchain.chains` to modern **LCEL (LangChain Expression Language)** architecture to bypass severe dependency conflicts within the environment.
* **Troubleshooting:**
  * Addressed `ModuleNotFoundError` and versioning conflicts (`protobuf`, `tokenizers`, `opentelemetry`) through strict version pinning and factory resets of the runtime environment.

## Phase 3: Deep Document Intelligence (2026-04-29)
* **Objective:** Enhance AI capabilities for dynamic external document ingestion (PDF).
* **Actions:**
  * Implemented `PyPDFLoader` for automated data extraction.
  * Optimized `RecursiveCharacterTextSplitter` to maintain semantic context during document chunking.
  * Validated system retrieval accuracy using a simulated corporate document ("PT Maju Mundur AI").
* **Troubleshooting:**
  * Resolved syntax issues related to file path formatting and library restructuring between `langchain-chroma` and `langchain-huggingface`.

## Phase 4: UI Development & Cloud Readiness (2026-05-08)
* **Objective:** Transition from backend logic to a user-friendly interface and prepare the system for cloud deployment.
* **Actions:**
  * Engineered an interactive web interface using **Streamlit**.
  * Replaced ChromaDB with **FAISS** for a more lightweight and efficient in-memory vector store suitable for cloud hosting.
  * Upgraded the core LLM to `llama-3.3-70b-versatile` for enhanced enterprise-grade reasoning.
  * Refactored code structure into modular functions (`process_pdf`, `initialize_session_state`) to meet international coding standards.
  * Implemented robust security measures for API keys utilizing Streamlit's `secrets.toml` and `.gitignore` protocols.