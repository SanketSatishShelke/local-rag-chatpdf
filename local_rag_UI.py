import os
import tempfile
import streamlit as st
from streamlit_chat import message
from local_rag_backend import ChatPDF

st.set_page_config(page_title="ChatPDF")

def display_messages():
    """
    Displays chat messages in a conversational format using streamlit_chat.

    - User messages are displayed on the right.
    - Assistant messages are displayed on the left.
    """
    st.subheader("Chat")
    for i, (msg, is_user) in enumerate(st.session_state["messages"]):
        message(msg, is_user=is_user, key=str(i))
    st.session_state["thinking_spinner"] = st.empty()


def process_input():
    """
    Processes user input, sends the query to the RAG system, and displays the response.

    - Validates the user input.
    - Uses the ChatPDF assistant to generate a response.
    - Appends the user query and response to the chat history.
    """
    if st.session_state["user_input"] and len(st.session_state["user_input"].strip()) > 0:
        user_text = st.session_state["user_input"].strip()
        with st.session_state["thinking_spinner"], st.spinner("Thinking..."):
            agent_text = st.session_state["assistant"].ask(user_text)

        st.session_state["messages"].append((user_text, True))
        st.session_state["messages"].append((agent_text, False))


def read_and_save_file():
    """
    Handles file uploads and prepares the RAG system for querying.

    - Clears existing chat and assistant state.
    - Saves uploaded files temporarily for processing.
    - Passes files to the ChatPDF ingestion pipeline.
    """
    st.session_state["assistant"].clear()
    st.session_state["messages"] = []
    st.session_state["user_input"] = ""

    for file in st.session_state["file_uploader"]:
        with tempfile.NamedTemporaryFile(delete=False) as tf:
            tf.write(file.getbuffer())
            file_path = tf.name

        with st.session_state["ingestion_spinner"], st.spinner(f"Ingesting {file.name}..."):
            st.session_state["assistant"].ingest(file_path)
        os.remove(file_path)


def page():
    """
    Main Streamlit app function to render the user interface.

    - Displays the file uploader for PDF documents.
    - Shows chat messages and provides an input box for queries.
    - Manages session state for the assistant and chat history.
    """
    if len(st.session_state) == 0:
        st.session_state["messages"] = []
        st.session_state["assistant"] = ChatPDF()

    st.header("ChatPDF")

    st.subheader("Upload a document")
    st.file_uploader(
        "Upload document",
        type=["pdf"],
        key="file_uploader",
        on_change=read_and_save_file,
        label_visibility="collapsed",
        accept_multiple_files=True,
    )

    st.session_state["ingestion_spinner"] = st.empty()

    display_messages()
    st.text_input("Message", key="user_input", on_change=process_input)


if __name__ == "__main__":
    page()
