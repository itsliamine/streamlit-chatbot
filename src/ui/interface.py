import streamlit as st
from src.ui.user_input import handle_user_input
from src.ui.chat_history import display_chat_history
from src.ui.session import initialize_session_state


def ui():
	st.set_page_config(
		page_title="Assistant Juridique",
		page_icon="⚖️",
		layout="centered"
	)

	st.header("💬 Assistant Juridique")
	st.markdown("""
		Bienvenue! Je suis votre assistant virtuel spécialisé dans les droits des personnes en France. 
		Je peux vous aider avec des informations sur:
		- La Loi du 11 février 2005
		- Les prestations d'invalidité (AAH, Pension d'Invalidité)
		- Les droits au travail
		- L'accès aux services
		- Les droits au logement
		""")

	initialize_session_state()
	display_chat_history()
	handle_user_input()

