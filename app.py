import streamlit as st

st.set_page_config(page_title = "AI Enterprise Assistant", page_icon = "☁")

st.title ("☁AI Enterprise Assisnant")
st.write ("Sistem siap melayani,siap menanyakan sesuatu")

with st.sidebar :
    st.header ("Knowledge base")
    st.write ("Upload dokumen perusahaan disini")
    uploaded_file = st.file_uploader ("Pilih file pdf", type=["pdf"])

    if uploaded_file is not None :
        st.success : (f"file '{uploaded_file_name}' berhasil diunggah!")
        st.info : ("Nanti bagian ini kita sambungin ke core engine kita yah")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.write(chat["content"])

if prompt := st.chat_input("Ketik pertanyaan Bapak di sini..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        response = f"Memproses pertanyaan: '{prompt}'. (Ini masih UI awal, ya wajar,namanya manusia boy,gw bukan dewa juga kan)"
        st.write(response)

    st.session_state.chat_history.append({"role": "assistant", "content": response})