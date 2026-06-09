from dotenv import load_dotenv
from groq import Groq
import streamlit as st
import os

load_dotenv()

api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

SYSTEM_PROMPT = "You are a helpful assistant. Be concise - max 3 sentences per reply."

st.title("AI Chatbot")
st.caption("Built with Groq + Llama 3.1 — Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input at the bottom
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.messages.append({"role": "user", "content": user_input})

    # ── CHANGED: streaming response ──────────────────────────────
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.messages,
            stream=True                          # ← added
        )
        reply = st.write_stream(                 # ← replaces st.write()
            chunk.choices[0].delta.content or ""
            for chunk in stream
        )
    # ────────────────────────────────────────────────────────────

    st.session_state.messages.append({"role": "assistant", "content": reply})