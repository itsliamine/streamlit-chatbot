from src.chatbot.retrieval import retrieve

qa = retrieve()
print(qa.memory)

def test_memory_retention():
	# Première interaction
	print("Interaction 1 : Donner un nom")
	result1 = qa({"question": "Je m'appelle Pierre"})
	# print(result1['answer'])
	
	debug_memory_state(qa.memory.chat_memory)
	
	# Deuxième interaction (peut ne pas reconnaître)
	print("\nInteraction 2 : Première tentative de récupération")
	result2 = qa({"question": "Quel est mon nom ?"})
	# print(result2['answer'])
	
	debug_memory_state(qa.memory.chat_memory)
	
	# Troisième interaction (devrait reconnaître)
	print("\nInteraction 3 : Deuxième tentative de récupération")
	result3 = qa({"question": "J'ai fais une demande d'AAH le 26/11 mais je n'ai toujours pas de reponse"})
	# print(result3['answer'])

	print("\nInteraction 4 : Troisième tentative de récupération")
	result3 = qa({"question": "A quel date ai-je fait ma demande ?"})
	# print(result3['answer'])
	
	debug_memory_state(qa.memory.chat_memory)


def debug_memory_state(memory):
	print("\n--- État de la mémoire ---")
	print(f"Nombre de messages : {len(memory.messages)}")
	for i, msg in enumerate(memory.messages):
		print(f"Message {i}:")
		print(f"  Type: {type(msg)}")
		print(f"  Contenu: {msg.content}")
		print(f"  Métadonnées: {msg.additional_kwargs}")

test_memory_retention()