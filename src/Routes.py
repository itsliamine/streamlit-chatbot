from flask import jsonify, request
from flask_cors import CORS

from src.chatbot.retrieval import retrieve

from . import create_app

app = create_app()
CORS(app)

# Appel de la fonction pour utiliser l'ia
qa_chain = retrieve()


# Route pour le futur front de la page de droit Pluriel
@app.route("/api/data", methods=["POST"])
def traiter_donnees():
    # Récupérer les données JSON envoyées
    data = request.get_json()

    # Vérifier que les données sont présentes
    if not data or "input" not in data:
        return jsonify({"erreur": "Aucune donnée reçue"}), 400

    # Récupérer la valeur de l'input
    valeur_input = data["input"]

    # Générer les embeddings
    response = qa_chain.invoke({"query": valeur_input})
    resultat = response.get(
        "result", "Désolé, je ne peux pas répondre à cette question."
    )

    # Renvoyer le résultat
    return jsonify({"input_original": valeur_input, "resultat_traite": resultat})


app.run(debug=True)
