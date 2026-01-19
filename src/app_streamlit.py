import streamlit as st
from agents import Runner

from agent import agent



st.set_page_config(page_title="Chatbot - Valentin Dujour", page_icon="💬")

st.title("Chatbot de Valentin Dujour")

# Questions prédéfinies
st.markdown("**💡 Questions suggérées :**")
col1, col2 = st.columns(2)

with col1:
    if st.button("📚 Quel est ton parcours ?"):
        user_question = "Quel est ton parcours académique et professionnel ?"
    else:
        user_question = None

with col2:
    if st.button("📧 Comment te contacter ?"):
        if user_question is None:
            user_question = "Comment puis-je te contacter ?"

st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Render chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input utilisateur
input_question = st.chat_input("Que veux-tu savoir ?")
st.caption("ℹ️ Ce chatbot utilise l'IA pour répondre à vos questions.")

# Prioriser les questions des boutons
if user_question is None:
    user_question = input_question

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
