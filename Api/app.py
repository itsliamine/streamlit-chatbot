import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# Route pour le futur front de la page de droit Pluriel
@app.route("/", methods=["GET"])
def home():
    return "<h1>API</h1><p>This is a REST API</p>"


# Route Pour transmettre l'input / demande de l'utlisateur au back
@app.route("/api/chatbot/demande", methods=["POST"])
def chatbot():
    if request.method == "POST":
        data = request.get_json()


# Route pour transmettre au front la reponse de l'ia
@app.route("api/chatbot/response", methods=["POST"])
def chatbotResponse():
    data = ""
    return jsonify(data)


app.run()
