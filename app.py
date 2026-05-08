import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq

# --- CONFIGURATION ---
st.set_page_config(page_title="Enterprise AI Assistant", page_icon="🤖", layout="wide")

def initialize_session_state():
    """Initializes the chat history and vector store in session state."""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "vector_store" not in st.session_state:
        st.session_state.vector_store = None

def process_pdf(pdf_file):
    """Extracts text, splits it into chunks, and creates a vector store."""
    try:
        reader = PdfReader(pdf_file)
        raw_text = ""
        for page in reader.pages:
            content = page.extract_text()
            if content:
                raw_text += content
        
        # Text Splitting (Chunking)
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = splitter.split_text(raw_text)
        
        # Vector Store Creation
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        vector_store = FAISS.from_texts(chunks, embeddings)
        return vector_store
    except Exception as e:
        st.error(f"Error processing document: {str(e)}")
        return None

# --- UI LAYOUT ---
st.title("🤖 Enterprise Knowledge Assistant")
st.markdown("### Leveraging RAG Technology with Llama 3.3 for Document Intelligence")

with st.sidebar:
    st.header("📂 Knowledge Base")
    st.write("Upload your corporate documents (PDF) to begin the session.")
    
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    
    if uploaded_file:
        if st.button("Process Document"):
            with st.spinner("Analyzing document structure..."):
                st.session_state.vector_store = process_pdf(uploaded_file)
                st.success("Analysis complete. System is ready.")

# --- CHAT INTERFACE ---
initialize_session_state()

# Display Chat History
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input Logic
if prompt := st.chat_input("Ask a question about your document..."):
    # Add user message to history
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Assistant Response
    with st.chat_message("assistant"):
        if st.session_state.vector_store:
            # Similarity Search
            docs = st.session_state.vector_store.similarity_search(prompt, k=3)
            context = "\n".join([doc.page_content for doc in docs])
            
            # LLM Integration
            try:
                llm = ChatGroq(
                    model_name="llama-3.3-70b-versatile", 
                    groq_api_key=st.secrets["GROQ_API_KEY"]
                )
                
                final_prompt = (
                    f"You are a professional corporate assistant. Use the following context "
                    f"to provide an accurate answer.\n\nContext:\n{context}\n\nQuestion: {prompt}"
                )
                
                with st.spinner("Generating insights..."):
                    response = llm.invoke(final_prompt).content
                    st.markdown(response)
                    st.session_state.chat_history.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error("Connection error. Please check the API configuration.")
        else:
            warning_msg = "Please upload and process a document before asking questions."
            st.warning(warning_msg)