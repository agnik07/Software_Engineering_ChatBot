import streamlit as st
from agent import software_agent

st.set_page_config(page_title="Software Engineering Agent")

st.title("💻 Software Engineering AI Agent")

st.write("Ask a programming question.")

# chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# user input
prompt = st.chat_input("Ask a coding question...")

if prompt:

    st.session_state.messages.append({"role":"user","content":prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    response = software_agent(prompt)

    with st.chat_message("assistant"):
        st.code(response, language="python")

    st.session_state.messages.append({"role":"assistant","content":response})