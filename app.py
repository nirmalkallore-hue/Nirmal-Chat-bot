import streamlit as st
from langchain_groq import ChatGroq

llm = ChatGroq(
    api_key="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",
    model="llama-3.3-70b-versatile"
)

st.title("🤖 Welcome to Nirmal Chat Booooooo Boooooot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Type your message")

if user_input:
    st.session_state.chat_history.append(f"You: {user_input}")

    prompt = "\n".join(st.session_state.chat_history)

    response = llm.invoke(prompt)
    bot_reply = response.content

    st.session_state.chat_history.append(f"Angel: {bot_reply}")

for msg in st.session_state.chat_history:
    st.write(msg)