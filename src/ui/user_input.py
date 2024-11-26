import streamlit as st

def handle_user_input():
	if user_input := st.chat_input("Posez votre question..."):
		st.chat_message("user").markdown(user_input)
		st.session_state.messages.append(
			{"role": "user", "content": user_input})

		with st.spinner('Recherche de la réponse...'):
			response = st.session_state.qa_chain.invoke({
				"question": user_input
			})

			print(response)

			answer = response.get(
				'answer', 'Désolé, je ne peux pas répondre à cette question.')

		with st.chat_message("assistant"):
			st.markdown(answer)
		st.session_state.messages.append(
			{"role": "assistant", "content": answer})
