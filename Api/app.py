import flask
from flask import jsonify, request
from flask_cors import CORS
from src.data_preprocessing.preprocess import preprocess_csv
from src.data_preprocessing.embeddings import generate_embeddings, upload_embeddings

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


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
    embeds = generate_embeddings("../DB 2.csv")
    upload_embeddings(
		embeddings=embeds
	)
    # Ici, vous pouvez faire votre traitement personnalisé
    # Par exemple, transformer la valeur, faire un calcul, etc.
    resultat = valeur_input

    # Renvoyer le résultat
    return jsonify({"input_original": valeur_input, "resultat_traite": resultat})


app.run()

