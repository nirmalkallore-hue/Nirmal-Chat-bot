import streamlit as st
hide_menu = """
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

##watermark
watermark = """
<style>
.watermark {
    position: fixed;
    bottom: 10px;
    right: 15px;
    opacity: 0.4;
    font-size: 14px;
    color: black;
    z-index: 100;
}
</style>

<div class="watermark">Nirmal Kallore</div>
"""

st.markdown(watermark, unsafe_allow_html=True)

st.markdown(hide_menu, unsafe_allow_html=True)
from langchain_groq import ChatGroq

llm = ChatGroq(
    api_key=st.secrets["GROQ_API_KEY"],
    model="llama-3.3-70b-versatile"
)

st.title("🤖 Welcome to Angel Chat boooot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Type your message")

if user_input:
    st.session_state.chat_history.append(f"You: {user_input}")

    prompt = "Always reply in English.\n" +"\n".join(st.session_state.chat_history)

    response = llm.invoke(prompt)
    bot_reply = response.content
    

    st.session_state.chat_history.append(f"Angel: {bot_reply}")

for msg in st.session_state.chat_history:
    st.write(msg)
