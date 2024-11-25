import flask
from flask import jsonify, render_template, request
from flask_cors import CORS

from src.chatbot.retrieval import retrieve
from src.data_preprocessing.embeddings import generate_embeddings, upload_embeddings

# Initialisation de l'application Flask
app = flask.Flask(__name__)
# Activation du mode debug
app.config["DEBUG"] = True
# Activation de CORS
CORS(app)

#Appel de la fonction pour utiliser l'ia
qa_chain = retrieve()

# Route pour la page d'accueil
@app.route("/")
# Fonction pour la page d'accueil
def index():
    # Renvoyer le template de la page d'accueil
    return render_template("index.html")


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


app.run()
