import os
from groq import Groq
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Streamlit app config
st.set_page_config(page_title="Educational Chatbot")
st.title("🎓 Educational Chatbot")

# Choice box for education topics
topic = st.selectbox(
    "Choose a topic to discuss:",
    ["General Education", "Mathematics", "Science", "History", "Programming", "Language Learning", "Exam Preparation"]
)

st.write(f"📚 Selected Topic: **{topic}**")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User prompt
prompt = st.chat_input(f"Ask me anything about {topic}...")

if prompt:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": f"Topic: {topic}\n{prompt}"})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call Groq API
    with st.chat_message("assistant"):
        chat_completion = client.chat.completions.create(
            messages=st.session_state.messages,
            model="gemma2-9b-it",  # or any other available Groq-supported model
        )
        response = chat_completion.choices[0].message.content
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# Button to clear chat
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()
