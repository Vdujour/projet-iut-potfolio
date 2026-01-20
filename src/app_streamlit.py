import streamlit as st
from agents import Runner

from agent import agent



st.set_page_config(page_title="Chatbot - Valentin Dujour", page_icon="💬")

st.title("Chatbot de Valentin Dujour")

st.caption("ℹ️ Ce chatbot utilise l'IA pour répondre à vos questions.")

# Questions prédéfinies
st.markdown("**💡 Questions suggérées :**")

user_question = None

limit = 5

col1, col2 = st.columns(2)
with col1:
    if st.button("Qui es-tu ?", use_container_width=True):
        user_question = "Qui es-tu ? Présente-toi en quelques lignes."
    if st.button("Quels projets as-tu réalisés ?", use_container_width=True):
        user_question = "Quels projets as-tu réalisés ?"
    if st.button("Comment te contacter ?", use_container_width=True):
        user_question = "Comment puis-je te contacter ?"

with col2:
    if st.button("Parle-moi de ton alternance", use_container_width=True):
        user_question = "Parle-moi de ton alternance"
    if st.button("Quelles sont tes compétences ?", use_container_width=True):
        user_question = "Quelles sont tes compétences"
    if st.button("Comment aller sur ton portfolio ?", use_container_width=True):
        user_question = "Comment aller sur ton portfolio ?"

st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "question_count" not in st.session_state:
    st.session_state.question_count = 0

# Render chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input utilisateur
input_question = st.chat_input("Que veux-tu savoir ?")
st.caption(f"Vous disposez de {limit} questions ({st.session_state.question_count}/{limit}).")

# Prioriser les questions des boutons
if user_question is None:
    user_question = input_question

if user_question:
    # Si le compteur a atteint 10, rediriger vers les informations de contact
    if st.session_state.question_count >= limit:
        user_question = "Comment puis-je te contacter ?"
    
    # Afficher le message de l'utilisateur dans le chat
    st.session_state.messages.append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.markdown(user_question)

    # Appeler l'agent et obtenir la réponse
    with st.chat_message("assistant"):
        with st.spinner("Réflexion en cours..."):
            result = Runner.run_sync(agent, user_question)
            answer = result.final_output
            
            # Si la limite est atteinte, ajouter un message
            if st.session_state.question_count >= limit:
                answer += f"\n\n---\n\n⚠️ Vous avez atteint la limite de {limit} questions. Pour toute question supplémentaire, merci de me contacter directement."
            
            st.markdown(answer)
    
    st.session_state.messages.append({"role": "assistant", "content": answer})
    
    # Incrémenter le compteur (max 10)
    if st.session_state.question_count < limit:
        st.session_state.question_count += 1
    st.rerun()
