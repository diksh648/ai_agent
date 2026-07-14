import streamlit as st
from langchain_groq import ChatGroq
import os
import re
from dotenv import load_dotenv
from tools import create_folder, open_chrome, make_call

load_dotenv()

st.set_page_config(page_title="AI Agent", page_icon="🤖")
st.title("AI Agent")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    api_key=os.getenv("GROQ_API_KEY")
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Type your message...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    user_input = prompt.lower()

    if "create folder" in user_input or "make folder" in user_input:

        folder_name = prompt.split()[-1]
        response = create_folder(folder_name)

    elif "open chrome" in user_input:

        response = open_chrome()
    elif "make call" in user_input:
        phone_number = re.search(r'\+?\d+', prompt)
        if phone_number:
            response = make_call(phone_number.group())
        else:
            response = "Please provide a valid phone number to make a call."        

    

    else:

        response = llm.invoke(prompt).content

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    with st.chat_message("assistant"):
        st.write(response)