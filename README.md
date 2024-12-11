# Handie

Handie est un chatbot conçu pour aider les personnes en situation de handicap à obtenir des informations juridiques. Le nom "Handie" fait référence à deux concepts : le mot "handicap" et "handy" en anglais, qui signifie "utile". C'est un nom "friendly" en rapport avec le sujet.

## Fonctionnalités
- **Réponses juridiques** : Handie fournit des réponses aux questions juridiques.
- **Facilité d'utilisation** : Le chatbot utilise un langage naturel et est facile à interagir avec.
- **Reconnaissance vocale** : Il est possible de poser des questions en utilisant la voix, grâce à une fonction de reconnaissance vocale.

## Architecture
Le projet est composé de deux parties principales :
1. **API Flask** : Cette API gère les requêtes juridiques et renvoie des réponses traitées.
2. **Webapp React** : L'interface utilisateur, qui permet aux utilisateurs de communiquer avec le chatbot, est construite en React.

## Prérequis

### Pour l'API Flask (Backend)
1. **Python 3.8+**
2. **Flask** pour créer l'API web.

### Pour l'application React (Frontend)
1. **Node.js** et **npm** pour installer les dépendances.
2. **React** pour l'interface utilisateur.

## Installation

### Backend (API Flask)
1. Clonez le repository du backend :

   ```bash
	git clone https://github.com/itsliamine/streamlit-chatbot.git
	cd handie-backend
	```
2. Créez un environnement virtuel et installez les dépendances :

	```bash
	python -m venv venv
	source venv/bin/activate   # Sur Windows : venv\Scripts\activate
	pip install -r requirements.txt
	```
3. Lancez le serveur Flask :

	```bash
	python app.py
	```

L'API sera disponible à l'adresse http://127.0.0.1:5000.

### Frontend (Application React)

1. Pour démarrer le front end, allez dans le dossier webapp

	```bash
	cd webapp/
	```
2. Installez les dépendances :

	```bash
	npm install
	```
3. Lancez l'application React :

	```bash	
	npm start
	```
L'application sera disponible à l'adresse http://localhost:3000.


### Dépendances
## Backend (Flask)
- Flask : Framework web léger pour créer l'API.
- Flask-CORS : Pour gérer les requêtes cross-origin depuis l'application React.*

	```bash
	pip install Flask Flask-CORS
	```
## Frontend (React)
- React : Framework JavaScript pour construire l'interface utilisateur.
- @mui/icons-material : Pour utiliser des icônes comme celle du microphone.
- framer-motion : Animations
- react-markdown : Pour afficher les réponses du chatbot avec un rendu Markdown.

	```bash
	npm install @mui/icons-material react-markdown
	```

# Auteurs
[Farès Aoudia](https://github.com/itsliamine)

[Gwendal Benard](https://github.com/GwEnDoO27)

[Anass El Karoumi](https://github.com/Anasskm)

# Licence
Ce projet est sous licence MIT. Vous pouvez librement utiliser et modifier le code, mais veuillez inclure cette licence dans toute copie du projet.