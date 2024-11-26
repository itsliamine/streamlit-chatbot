from src.chatbot.retrieval import retrieve

def test_emergency():
	qa = retrieve()
	print("Interaction 1 : Demander de l'aide pour des attouchements")
	qa({"question": "J'ai subis des attouchements de la part de certains membres de ma famille. J'ai besoin d'aide."})

	debug_memory_state(qa.memory.chat_memory)

	qa = retrieve()
	print("Interaction 1 : Demander de l'aide pour des délais de la CAF")
	qa({"question": "Quels sont les delais de demande pour la CAF ?"})

	debug_memory_state(qa.memory.chat_memory)


def debug_memory_state(memory):
	print("\n--- État de la mémoire ---")
	print(f"Nombre de messages : {len(memory.messages)}")
	for i, msg in enumerate(memory.messages):
		print(f"Message {i}:")
		print(f"  Type: {type(msg)}")
		print(f"  Contenu: {msg.content}")
		print(f"  Métadonnées: {msg.additional_kwargs}")

test_emergency()