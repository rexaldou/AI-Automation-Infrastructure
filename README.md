# AI Automation Infrastructure 🤖

Sistem RAG (Retrieval-Augmented Generation) berbasis Llama 3.1 dan ChromaDB untuk otomatisasi pengetahuan korporat. Proyek ini dikembangkan sebagai bagian dari riset jalur Project Work (Pengganti Skripsi).

## 🛠️ Tech Stack
* **LLM:** Llama-3.1-8b-instant (via Groq Cloud)
* **Orchestration:** LangChain (LCEL)
* **Database:** ChromaDB
* **Embeddings:** HuggingFace (all-MiniLM-L6-v2)

---

## 📜 DevLog (Catatan Pengembangan)

# AI Automation Infrastructure 🤖

Sistem RAG (*Retrieval-Augmented Generation*) berbasis Llama 3.1 dan ChromaDB untuk otomatisasi pengetahuan korporat. Proyek ini dikembangkan sebagai bagian dari riset jalur *Project Work* (Pengganti Skripsi).

---

## 📜 Project DevLog

### [2026-04-27] - Phase 1: LLM Engine Integration
* **Objective:** Menghubungkan *environment* Python ke LLM (Llama 3.1) melalui Groq Cloud.
* **Action:**
    * Inisialisasi `ChatGroq` menggunakan library `langchain-groq`.
    * Konfigurasi API Key melalui `os.environ`.
* **Challenges:** Mendapatkan `BadRequestError` (Error 400).
* **Analysis:** Model `llama3-8b-8192` ternyata sudah tidak aktif (*decommissioned*) pada server Groq.
* **Resolution:** Memperbarui parameter model ke `llama-3.1-8b-instant`. Sistem kembali normal dengan latensi yang sangat rendah.

---

### [2026-04-28] - Phase 2: RAG Architecture & Dependency Management
* **Objective:** Membangun ekosistem RAG menggunakan LangChain dan ChromaDB.
* **Action:**
    * Konfigurasi `HuggingFaceEmbeddings` untuk pengolahan database vektor.
    * Pembuatan *knowledge base* lokal (kebijakan cuti, prosedur lembur, dan IT support).
    * Implementasi awal arsitektur *Chain*.
* **Major Challenges & Resolutions:**
    * **Issue 1: Dependency Conflict:** Konflik versi pada `google-colab`, `requests`, dan `opentelemetry`.
        * **Fix:** Mengabaikan *warning* dan melakukan *Restart Session*.
    * **Issue 2: ModuleNotFoundError (`langchain.chains`):** Modul tidak ditemukan secara terus-menerus.
        * **Analysis:** Terjadi kesalahan *indexing* folder pada sistem *backend* Colab.
    * **Issue 3: Protobuf & Versioning Hell:** Error `MessageFactory` dan konflik `tokenizers`.
        * **Fix:** Melakukan *Version Pinning* manual pada `tokenizers==0.22.2` dan `protobuf==3.20.3`.

* **The Final Breakthrough (The Nuclear Option):**
    * **Factory Reset:** Melakukan *Disconnect & Delete Runtime* untuk membersihkan sisa memori dan *cache*.
    * **LCEL Bypass:** Menghindari ketergantungan pada modul `langchain.chains` yang rusak dengan membangun *pipeline* manual menggunakan **LCEL (LangChain Expression Language)** dengan sintaks `|` (*pipe*).

---

# AI Automation Infrastructure 🤖

Sistem RAG (*Retrieval-Augmented Generation*) modular untuk otomatisasi pengetahuan korporat.

---

## 📜 DevLog: Phase 3 - Deep Document Intelligence

### [2026-04-29] - PDF Integration & Dependency Hardening
> **Status:** Success ✅

#### 🎯 Objective
Meningkatkan kapabilitas AI agar mampu mengolah dokumen eksternal secara dinamis (PDF) alih-alih menggunakan teks statis di dalam kode.

#### 🛠️ Actions Taken
* **Document Loading:** Implementasi `PyPDFLoader` untuk ekstraksi data otomatis dari file PDF.
* **Text Processing:** Optimalisasi `RecursiveCharacterTextSplitter` guna membagi dokumen menjadi *chunks* yang lebih bermakna untuk menjaga konteks.
* **Vector Sync:** Sinkronisasi ulang `vectorstore` (Chroma) dengan data fisik untuk memastikan database selalu *up-to-date*.

#### ⚠️ Challenges & Lessons Learned
* **Syntax Awareness (`NameError`):** Terjadi *error* akibat pemanggilan *path* file tanpa tanda kutip. 
  * *Lesson:* Path file dalam Python wajib dianggap sebagai **String**.
* **Library Sensitivity:** Menangani perubahan struktur LangChain yang memisahkan modul `langchain-chroma` dan `langchain-huggingface`.
* **Dependency War:** Resolusi konflik `opentelemetry` pada *environment* Google Colab menggunakan teknik *version pinning*.

#### 🏆 Result
AI berhasil melakukan *retrieval* data secara akurat dari dokumen **"PT Maju Mundur AI"**, mencakup detail spesifik seperti angka denda keterlambatan, kontak keamanan (Hyuga Santa Claus), dan syarat tunjangan sertifikasi.

---

## 🚀 Future Plans / Next Steps
* **PDF Integration:** Upgrade kemampuan sistem agar dapat membaca dokumen dari file PDF secara dinamis.
* **Memory Management:** Menambahkan fitur `ConversationBuffer` agar AI dapat mengingat konteks percakapan.
* **Deployment:** Integrasi *pipeline* ke platform *messaging* (WhatsApp/Telegram) melalui Make.com.

---
*Developed by Rexaldo Dhiya Ulhaq*
*Proyek ini terus dikembangkan sebagai bagian dari riset AI Automation.*
