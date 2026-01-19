import streamlit as st
from agents import Runner

from agent import agent



st.set_page_config(page_title="Chatbot - Valentin Dujour", page_icon="💬")

st.title("Chatbot de Valentin Dujour")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Render chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_question = st.chat_input("Que veux-tu savoir ?")
st.caption("ℹ️ Ce chatbot utilise l'IA pour répondre à vos questions.")

if user_question:
    # Afficher le message de l'utilisateur dans le chat
    st.session_state.messages.append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.markdown(user_question)

    # Appeler l'agent et obtenir la réponse
    with st.chat_message("assistant"):
        with st.spinner("Réflexion en cours..."):
            result = Runner.run_sync(agent, user_question)
            answer = result.final_output
            st.markdown(answer)
    
    st.session_state.messages.append({"role": "assistant", "content": answer})
