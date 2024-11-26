async function SendingData() {
    // Récupérer la valeur de l'input
    const inputElement = document.getElementById('monInput');
    const valeurInput = inputElement.value;

    try {
        // Envoyer une requête POST à l'API
        const reponse = await fetch('http://localhost:5000/api/data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ input: valeurInput })
        });

        // Vérifier la réponse
        if (!reponse.ok) {
            throw new Error('Erreur de requête');
        }

        // Récupérer et afficher les données
        const donnees = await reponse.json();
        document.getElementById('resultat').innerHTML = `
                <p>Question : ${donnees.input_original}</p>
                <p>Reponse : ${donnees.resultat_traite}</p>
            `;
    } catch (erreur) {
        console.error('Erreur:', erreur);
        document.getElementById('resultat').innerHTML = 'Une erreur est survenue';
    }
}



