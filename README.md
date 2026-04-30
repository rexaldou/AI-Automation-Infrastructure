# AI Automation Infrastructure 

Sistem RAG (Retrieval-Augmented Generation) berbasis Llama 3.1 dan ChromaDB untuk otomatisasi pengetahuan korporat. Proyek ini dikembangkan sebagai bagian dari riset jalur Project Work (Pengganti Skripsi).

##  Tech Stack
* **LLM:** Llama-3.1-8b-instant (via Groq Cloud)
* **Orchestration:** LangChain (LCEL)
* **Database:** ChromaDB
* **Embeddings:** HuggingFace (all-MiniLM-L6-v2)

---

## 📜 DevLog (Catatan Pengembangan)

# AI Automation Infrastructure 

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

*Sistem RAG (*Retrieval-Augmented Generation*) modular untuk otomatisasi pengetahuan korporat.*

---

## 📜 DevLog: Phase 3 - Deep Document Intelligence

### [2026-04-29] - PDF Integration & Dependency Hardening
> **Status:** Success 

####  Objective
Meningkatkan kapabilitas AI agar mampu mengolah dokumen eksternal secara dinamis (PDF) alih-alih menggunakan teks statis di dalam kode.

####  Actions Taken
* **Document Loading:** Implementasi `PyPDFLoader` untuk ekstraksi data otomatis dari file PDF.
* **Text Processing:** Optimalisasi `RecursiveCharacterTextSplitter` guna membagi dokumen menjadi *chunks* yang lebih bermakna untuk menjaga konteks.
* **Vector Sync:** Sinkronisasi ulang `vectorstore` (Chroma) dengan data fisik untuk memastikan database selalu *up-to-date*.

####  Challenges & Lessons Learned
* **Syntax Awareness (`NameError`):** Terjadi *error* akibat pemanggilan *path* file tanpa tanda kutip. 
  * *Lesson:* Path file dalam Python wajib dianggap sebagai **String**.
* **Library Sensitivity:** Menangani perubahan struktur LangChain yang memisahkan modul `langchain-chroma` dan `langchain-huggingface`.
* **Dependency War:** Resolusi konflik `opentelemetry` pada *environment* Google Colab menggunakan teknik *version pinning*.

####  Result
AI berhasil melakukan *retrieval* data secara akurat dari dokumen **"PT Maju Mundur AI"**, mencakup detail spesifik seperti angka denda keterlambatan, kontak keamanan (Santa Claus), dan syarat tunjangan sertifikasi.

---

## 📖 Devlog: RAG Engine v1 (30 April 2026)

###  Detail Pengerjaan
* Transisi dari arsitektur *legacy* (`langchain.chains`) ke arsitektur modern berbasis **LCEL** (LangChain Expression Language).
* Implementasi sistem **History-Aware Retriever** agar AI memiliki *Persistent Memory* antar percakapan.
* Uji coba PoC berhasil: AI mampu mengekstraksi dan menjawab *query* spesifik dari dokumen PDF internal (Panduan Operasional Karyawan) tanpa kehilangan konteks chat sebelumnya.

###  Daftar Error & Solusi (Troubleshooting History)
| Error Code / Issue | Penyebab | Solusi |
| :--- | :--- | :--- |
| `ModuleNotFoundError: 'langchain.chains'` | Bentrok instalasi bawaan Colab akibat *quiet mode* yang menumpuk. | Beralih penuh ke arsitektur LCEL; berhenti memanggil modul `.chains`. |
| `Dependency Conflict` | Inkompatibilitas versi *library* karena *downgrade* spesifik. | *Update* seluruh ekosistem LangChain ke versi *Latest*, mengunci `opentelemetry` di `1.38.0`. |
| `ImportError: 'is_offline_mode'` | Modul *embedding* kekurangan mesin pembaca yang kompatibel dengan HuggingFace terbaru. | Menambahkan `sentence-transformers` secara eksplisit ke *script* instalasi utama. |
| `GroqError: api_key client option` | Instance `ChatGroq` dipanggil sebelum otorisasi variabel *environment*. | Reposisi *code block*; mendeklarasikan `os.environ["GROQ_API_KEY"]` sebelum inisialisasi LLM. |
| `BadRequestError: 400` | Model `llama-3.1-70b-versatile` resmi dipensiunkan (*decommissioned*). | Memperbarui parameter model ke versi terbaru: `llama-3.3-70b-versatile`. |
| `CustomError: Failed to save` | *Timeout* otentikasi API dari sesi Google Colab ke GitHub. | Menggunakan jalur *bypass*: unduh `.ipynb` lokal dan unggah *commit* manual ke repositori. |

---

## 🗺️ Goal Coding Update

** Big Goal:** Membangun AI Otomatisasi mandiri kelas Enterprise yang mampu menyortir dan merespons berdasarkan data internal untuk kebutuhan bisnis.

###  Posisi Sekarang
* **[Python - AI Development]**
  * **Level:** Intermediate-Advanced
  * **Status:** Core Engine Selesai (100%). Otak AI beroperasi dengan memori konteks aktif dan pembacaan dokumen privat berjalan lancar.

###  Next Step (Roadmap)
- [ ] **Demonstrasi Proof of Concept (PoC):** Presentasi kemampuan dasar AI ke klien.
- [ ] **User Interface (UI):** Membangun antarmuka interaktif menggunakan Streamlit atau Gradio.
- [ ] **Integrasi Chat API:** Menyambungkan AI Engine ke platform komunikasi klien (WhatsApp/Telegram) untuk otomatisasi respons.
- [ ] **Cloud Deployment:** Mengunggah sistem inti ke cloud server (AWS/GCP) agar AI beroperasi 24/7 tanpa henti.
- [ ] **Analytics Dashboard:** Membangun sistem pemantauan untuk merekam tren pertanyaan dari operasional perusahaan.

---
*Developed by Rexaldo Dhiya Ulhaq*
*Proyek ini terus dikembangkan sebagai bagian dari riset AI Automation.*
