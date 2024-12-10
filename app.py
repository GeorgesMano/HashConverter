import hashlib
import json
from datetime import datetime
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Fichier où l'historique des conversions sera stocké
STORAGE_FILE = 'database.json'

# Charger les conversions depuis le fichier JSON
def load_conversions():
    try:
        with open(STORAGE_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Retourner une liste vide si le fichier n'existe pas ou est corrompu

# Sauvegarder une conversion dans le fichier JSON
def save_hash_conversion(input_string, hash_type, hash_result):
    conversions = load_conversions()  # Charger les conversions existantes

    # Créer un enregistrement de la conversion
    conversion = {
        'input': input_string,
        'hash_type': hash_type,
        'hash_result': hash_result,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    conversions.append(conversion)  # Ajouter la conversion à l'historique
    conversions = conversions[-100:]  # Limiter à 100 entrées

    # Sauvegarder dans le fichier JSON
    with open(STORAGE_FILE, 'w') as f:
        json.dump(conversions, f, indent=2)

# Page principale avec formulaire et tableau des résultats
@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    conversions = load_conversions()

    if request.method == 'POST':
        input_string = request.form.get('input_string', '')
        hash_type = request.form.get('hash_type', 'sha256')

        if not input_string:
            result = "Veuillez fournir un texte à hacher."
        else:
            # Générer le hachage en fonction du type choisi
            if hash_type == 'md5':
                hash_result = hashlib.md5(input_string.encode()).hexdigest()
            elif hash_type == 'sha1':
                hash_result = hashlib.sha1(input_string.encode()).hexdigest()
            elif hash_type == 'sha256':
                hash_result = hashlib.sha256(input_string.encode()).hexdigest()
            else:
                result = "Type de hachage non pris en charge."

            if not result:  # Si aucun message d'erreur
                save_hash_conversion(input_string, hash_type, hash_result)
                result = f"Résultat ({hash_type}): {hash_result}"

        # Recharger les conversions après la mise à jour
        conversions = load_conversions()

    return render_template_string(HTML_TEMPLATE, result=result, conversions=conversions)

# Template HTML amélioré
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hash Converter</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f9f9f9;
            color: #333;
        }
        h1 {
            color: #4CAF50;
            text-align: center;
        }
        form {
            max-width: 500px;
            margin: 20px auto;
            padding: 20px;
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        label {
            font-weight: bold;
            margin-top: 10px;
            display: block;
        }
        input, select, button {
            width: 100%;
            padding: 10px;
            margin-top: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-sizing: border-box;
        }
        button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background: white;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        table, th, td {
            border: 1px solid #ddd;
        }
        th {
            background-color: #4CAF50;
            color: white;
        }
        th, td {
            padding: 12px;
            text-align: left;
        }
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h1>Hash Converter By Georges</h1>
    <form method="POST" action="/">
        <label for="input_string">Texte à convertir :</label>
        <input type="text" id="input_string" name="input_string" placeholder="Entrez le texte ici..." required>

        <label for="hash_type">Type de hachage :</label>
        <select id="hash_type" name="hash_type">
            <option value="sha256">SHA-256</option>
            <option value="md5">MD5</option>
            <option value="sha1">SHA-1</option>
        </select>

        <button type="submit">Convertir</button>
    </form>

    <h2>Résultat :</h2>
    <p>{{ result }}</p>

    <h2>Historique des conversions :</h2>
    <table>
        <thead>
            <tr>
                <th>Date et heure</th>
                <th>Texte</th>
                <th>Type de hachage</th>
                <th>Résultat</th>
            </tr>
        </thead>
        <tbody>
            {% for conversion in conversions %}
            <tr>
                <td>{{ conversion.timestamp }}</td>
                <td>{{ conversion.input }}</td>
                <td>{{ conversion.hash_type }}</td>
                <td>{{ conversion.hash_result }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
