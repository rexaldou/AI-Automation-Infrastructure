# AI Automation Infrastructure 🤖

Sistem RAG (Retrieval-Augmented Generation) berbasis Llama 3.1 dan ChromaDB untuk otomatisasi pengetahuan korporat. Proyek ini dikembangkan sebagai bagian dari riset jalur Project Work (Pengganti Skripsi).

## 🛠️ Tech Stack
* **LLM:** Llama-3.1-8b-instant (via Groq Cloud)
* **Orchestration:** LangChain (LCEL)
* **Database:** ChromaDB
* **Embeddings:** HuggingFace (all-MiniLM-L6-v2)

---

## 📜 DevLog (Catatan Pengembangan)

#[2026-04-27] - Phase 1: LLM Engine Integration
-Objective: Menghubungkan environment Python ke LLM (Llama 3.1) via Groq Cloud.
-Action:
--Inisialisasi ChatGroq menggunakan library langchain-groq.
--Konfigurasi API Key lewat os.environ.
-Challenges: Mendapat BadRequestError (Error 400).
-Analysis: Model llama3-8b-8192 ternyata sudah decommissioned (pensiun) dari server Groq.
-Resolution: Mengupdate parameter model ke llama-3.1-8b-instant. Sistem kembali normal dengan latency sangat rendah.

#[2026-04-28] - Phase 2: RAG Architecture & Dependency Hell
-Objective: Membangun ekosistem RAG (Retrieval-Augmented Generation) menggunakan LangChain dan ChromaDB.
-Action:
-Setup HuggingFaceEmbeddings untuk pengolahan database vektor.
-Pembuatan knowledge base lokal (Data cuti, lembur, dan IT support).
-Implementasi awal arsitektur Chain.
-The "Massive" Challenges & Resolutions:
-Issue 1: Dependency Conflict: Konflik versi pada google-colab, requests, dan opentelemetry.
--Fix: Abaikan warning dan lakukan Restart Session agar library utama tetap ter-load.
-Issue 2: ModuleNotFoundError (langchain.chains): Error terus-menerus meskipun sudah install ulang.
--Analysis: Terjadi kerusakan indexing folder pada sistem Colab.
-Issue 3: Protobuf & Versioning Hell: Error MessageFactory (Protobuf) dan konflik tokenizers (minta v0.23.0 tapi yang ada v0.23.1 atau ghaib).
--Fix: Melakukan Version Pinning manual pada tokenizers==0.22.2 dan protobuf==3.20.3.
-The Final Breakthrough (The Nuclear Option):
--Melakukan Factory Reset (Disconnect & Delete Runtime) untuk membersihkan semua sampah memori.
--LCEL Bypass: Menghilangkan ketergantungan pada modul langchain.chains yang rusak dan membangun pipeline manual menggunakan LCEL (LangChain Expression Language) dengan syntax | (pipe).

#[Future Plans / Next Steps]
-PDF Integration: Upgrade sistem agar bisa membaca dokumen dari file PDF eksternal secara dinamis.
-Memory Management: Menambahkan fitur ConversationBuffer agar AI bisa mengingat konteks percakapan sebelumnya.
-Deployment: Integrasi pipeline ke platform messaging (WhatsApp/Telegram) menggunakan Make.com.
