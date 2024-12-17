# Hash Converter Application #
## Description ##
L'application Hash Converter permet de convertir du texte en trois types de hachage : MD5, SHA-1, et SHA-256.
Elle utilise Flask pour servir une interface web intuitive où les utilisateurs peuvent :

Entrer un texte.
Choisir un type de hachage.
Obtenir instantanément le résultat du hachage.
Les conversions sont automatiquement enregistrées dans un fichier JSON (database.json) pour être consultées ultérieurement.

## Fonctionnalités ##
1. Conversion de texte
Les utilisateurs peuvent saisir un texte et sélectionner un algorithme de hachage parmi les options disponibles :

-MD5
-SHA-1
-SHA-256
2. Historique des conversions
Chaque conversion est enregistrée dans un fichier JSON (database.json) pour être affichée dans un tableau interactif.
L'historique est limité aux 100 dernières conversions.
3. Résultats dynamiques
Après chaque conversion, le résultat est affiché directement sous le formulaire.
Les conversions précédentes sont listées dans un tableau en bas de la page.
## Technologies utilisées ##

Flask : Framework web Python utilisé pour créer l'API et l'interface utilisateur.
HTML/CSS : Pour créer une interface utilisateur claire et responsive.
JSON : Pour stocker les données d'historique des conversions.
##**Installation et utilisation**##
## Prérequis ##
Assurez-vous d'avoir :

Python 3.9 ou supérieur installé.
Docker et Docker Compose installés sur votre machine.

Structure du projet
Voici la structure des fichiers du projet :
convert_doc/
├── app.py              # Le fichier principal de l'application Flask
├── database.json       # Le fichier pour stocker l'historique des conversions
├── Dockerfile          # Fichier de configuration Docker pour l'application Flask
├── docker-compose.yml  # Fichier Docker Compose pour gérer les services
├── requirements.txt    # Liste des dépendances Python nécessaires
├── README.md           # Documentation détaillée du projet
└── images/             # Dossier contenant les captures d'écran du projet

## Utilisation ##
Entrez un texte dans le champ prévu.
Sélectionnez un type de hachage parmi les options disponibles (MD5, SHA-1, SHA-256).
Cliquez sur le bouton "Convertir" :
Le résultat du hachage s'affiche directement sous le formulaire.
L'historique des conversions apparaît dans un tableau sous le formulaire.
Aperçu du projet
Exemple d'interface utilisateur :

## Commandes Docker ##
Construire et exécuter l'application
Copier le code
```bash
docker-compose up --build
```
Arrêter l'application
```bash
docker-compose down
```
## Installation ##
Installez les dépendances :
N'oubliez pas d'installer le fichier requirement 
```
pip install -r requirements.txt
```
Installation
Avec Docker
Clonez ce repository :
```
git clone https://github.com/GeorgesMano/HashConverter.git
```
Construisez et lancez les services avec Docker Compose :
```
docker-compose up --build
```
L'API sera disponible à l'adresse suivante : http://localhost:5000
