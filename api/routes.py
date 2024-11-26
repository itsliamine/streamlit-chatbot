from flask import jsonify, render_template, request
from flask_cors import CORS

from src.chatbot.retrieval import retrieve

# Appele le model
qa_chain = retrieve()


# Gere les routes
def init_routes(app):
	# Accepte les Cors
	CORS(app)

	# Route principale
	@app.route("/")

	# Permet le rendering de la page
	def index():
		return render_template("index.html")

	# gere la route pour le transfert de données
	@app.route("/api/data", methods=["POST"])
	def handle_data():
		# Récupère les données en json
		data = request.get_json()

		# Gestion d'erreur
		if not data or "input" not in data:
			return jsonify({"erreur": "Aucune donnée reçue"}), 400

		# Stock la valeur de l'input
		valeur_input = data["input"]

		# Passe la qestion a l'ia
		response = qa_chain.invoke({"question": valeur_input})
		
		# Erreur
		resultat = response.get(
			"result", "Désolé, je ne peux pas répondre à cette question."
		)

		# Retourne le resultat
		return jsonify({"input_original": valeur_input, "resultat_traite": resultat})
