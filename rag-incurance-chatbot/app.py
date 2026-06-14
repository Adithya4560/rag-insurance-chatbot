import streamlit as st
from rag import ask
import time
st.set_page_config(page_title="Indian Insurance Chatbot", page_icon="/rag-incurance-chatbot/logo.jpg",layout="centered")
col1,col2=st.columns([1,4])
with col1:
    st.image("/rag-incurance-chatbot/logo.jpg", width=100)
with col2:
    st.title("Indian Insurance Chatbot")
    st.subheader("Ask me anything about Indian government insurance schemes ")


if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
user_input=st.chat_input("Ask me anything about insurance schemes...")
if user_input:
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role":"user","content":user_input})
    response = ask(user_input)
    def stream_response(text):
        for word in text.split():
            yield word + " "
            time.sleep(0.05)
    with st.chat_message("assistant"):
        st.write_stream(stream_response(response))
    st.session_state.messages.append({"role":"assistant","content":response})
    
    
st.markdown("""
<style>
     [data-testid="stImage"] img {
        border-radius: 50%;
        border: 2px solid #ff9933;
    }
    .main {
        background-color: #f0f2f6;
    }
    .stChatMessage {
        animation: fadeIn 0.5s ease-in;
    }
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(10px);}
        to {opacity: 1; transform: translateY(0px);}
    }
    .block-container {
        max-width: 750px;
        margin: auto;
        padding-top: 80px;
    }
    .stChatInput input {
        border-radius: 20px;
        padding: 15px;
    }
    h1 {
        text-align: center;
        font-size: 2.5rem;
    }
    .stSubheader {
        text-align: center;
        color: gray;
    }
</style>
""", unsafe_allow_html=True)

