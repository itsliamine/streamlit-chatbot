import flask
from src.chatbot.retrieval import retrieve
from routes import init_routes

# Lance une instance flask
app = flask.Flask(__name__)
# Autotise le debug
app.config["DEBUG"] = True

# Initialise les routes
init_routes(app)

if __name__ == "__main__":
    app.run()
