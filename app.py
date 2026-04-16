import streamlit as st
hide_menu = """
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_menu, unsafe_allow_html=True)
from langchain_groq import ChatGroq

llm = ChatGroq(
    api_key="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",
    model="llama-3.3-70b-versatile"
)

st.title("🤖 Welcome to Angel Chat boooot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Type your message")

if user_input:
    st.session_state.chat_history.append(f"You: {user_input}")

    prompt = "\n".join(st.session_state.chat_history)

    response = llm.invoke(prompt)
    bot_reply = response.content
    with st.chat_message("Angel"):
        st.markdown(bot_reply)

    st.session_state.chat_history.append(f"Angel: {bot_reply}")

for msg in st.session_state.chat_history:
    st.write(msg)
