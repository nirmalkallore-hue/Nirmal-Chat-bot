
import streamlit as st
hide_menu = """
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
#####Green colour
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #d4f7d4;
    }
    </style>
    """,
    unsafe_allow_html=True
)
##Green colou code end 

### Author Name
st.markdown("""
<style>
.footer {
    position: fixed;
    bottom: 10px;
    left: 15px;
    font-size: 13px;
    color: gray;
    opacity: 0.7;
}
</style>

<div class="footer">Built by Nirmal Kallore</div>
""", unsafe_allow_html=True)
### Author NAme 
st.markdown(hide_menu, unsafe_allow_html=True)
from langchain_groq import ChatGroq

llm = ChatGroq(
    api_key=st.secrets["GROQ_API_KEY"],
    model="llama-3.3-70b-versatile"
)

st.title("🤖 Welcome to Angel Chat bot")
st.caption("Built by Nirmal Kallore")

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
