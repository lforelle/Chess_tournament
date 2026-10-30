# Gestionnaire de tournois d’échecs

Application en ligne de commande pour gérer les joueurs et les tours d’un
tournoi d’échecs. Les données sont conservées dans des fichiers JSON.

## Prérequis

- Python 3
- `venv` et `pip`

Sur Debian ou Ubuntu, installez les prérequis avec :

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

## Installation

Depuis la racine du projet, créez et activez un environnement virtuel :

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Installez les dépendances du projet :

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Lancer le programme

Depuis la racine du projet, avec l’environnement virtuel activé :

```bash
python main.py
```

Le menu principal permet d’accéder aux fonctions de gestion disponibles dans
l’application.

## Fonctionnalités documentées

### Joueurs

- Créer, afficher, modifier et supprimer un joueur.
- Valider les noms et prénoms, la date de naissance au format `JJ/MM/AAAA`
  et le CNID au format `AB12345`.
- Conserver les joueurs dans `data/players_data/players.json`.

### Tours et rencontres

- Générer des tours et des appairages à partir des joueurs enregistrés.
- Saisir les résultats `1-0`, `0-1` ou `1/2-1/2`.
- Modifier les scores si besoin.
- Terminer un tour.
- Afficher le classement des joueurs et leur total de points.
- Conserver les tours, rencontres, résultats, joueurs exempts et dates dans
  `data/matches_data/matches.json`.

## Données

Les fichiers JSON sont stockés dans le dossier `data/` :

```text
data/
├── players_data/players.json
└── matches_data/matches.json
```

## Structure du projet

```text
Chess_tournament/
├── main.py
├── controllers/
├── data/
├── menus/
├── models/
├── repositories/
├── services/
├── views/
└── requirements.txt
```