import streamlit as st
from src.chatbot.retrieval import retrieve

def initialize_session_state():
	if 'messages' not in st.session_state:
		st.session_state.messages = []
	if 'qa_chain' not in st.session_state:
		st.session_state.qa_chain = retrieve()
