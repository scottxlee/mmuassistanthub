import openai
import streamlit as st
import time
from dotenv import load_dotenv

client = openai

load_dotenv()

if "start_chat" not in st.session_state:
    st.session_state.start_chat = False
if "thread_id" not in st.session_state:
    st.session_state.thread_id = None

st.set_page_config(page_title="Assistants Hub", page_icon=":speech_balloon:")

# Input for assistant_id
assistant_id = st.sidebar.text_input("Enter Assistant ID", "")

if st.sidebar.button("Start Chat") and assistant_id:
    st.session_state.start_chat = True
    thread = client.beta.threads.create()
    st.session_state.thread_id = thread.id

if assistant_id:
    try:
        assistant = client.beta.assistants.retrieve(assistant_id)
        assistant_name = assistant.name  # Assuming the 'name' field is available
        st.title(f"{assistant_name}")  # Use the dynamic title here
    except Exception as e:
        st.error("Failed to retrieve Assistant details. Check the Assistant ID and your network connection.")
        assistant_name = "The MMU Assistant Hub"  # Fallback title
        st.title(assistant_name)
else:
    assistant_name = "Welcome to the MMU Assistant Hub"  # Default title if no ID is entered
    st.title(assistant_name)

st.write("Here to help with your coursework")

if st.button("Exit Chat"):
    st.session_state.messages = []  # Clear the chat history
    st.session_state.start_chat = False  # Reset the chat state
    st.session_state.thread_id = None

if st.session_state.start_chat:
    if "openai_model" not in st.session_state:
        st.session_state.openai_model = "gpt-4-1106-preview"
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("How can I assist you?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        assistant = client.beta.assistants.retrieve(assistant_id)

        client.beta.threads.messages.create(
                thread_id=st.session_state.thread_id,
                role="user",
                content=prompt
            )
        
        run = client.beta.threads.runs.create(
            thread_id=st.session_state.thread_id,
            assistant_id=assistant_id,
        )

        while run.status != 'completed':
            time.sleep(1)
            run = client.beta.threads.runs.retrieve(
                thread_id=st.session_state.thread_id,
                run_id=run.id
            )
        messages = client.beta.threads.messages.list(
            thread_id=st.session_state.thread_id
        )

        # Process and display assistant messages
        assistant_messages_for_run = [
            message for message in messages 
            if message.run_id == run.id and message.role == "assistant"
        ]
        for message in assistant_messages_for_run:
            st.session_state.messages.append({"role": "assistant", "content": message.content[0].text.value})
            with st.chat_message("assistant"):
                st.markdown(message.content[0].text.value)

else:
    if not assistant_id:
        st.error("Please enter a valid Assistant ID to start the chat.")
    st.write("Click 'Start Chat' to begin.")
