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

## Configuration et lancement

L’application est initialisée dans `main.py`. Aucun fichier de configuration externe n’est chargé au démarrage : les composants sont assemblés directement dans la fonction `main()`.

Au lancement, l’application :

1. crée le dépôt et le contrôleur des joueurs, puis récupère la liste des joueurs ;
2. crée le dépôt et le contrôleur des tournois en leur transmettant cette liste ;
3. initialise les vues des joueurs et des tournois ;
4. lance le menu principal avec ces contrôleurs et ces vues.

Pour lancer l’application depuis le répertoire du projet :

```bash
python main.py
```

Le menu principal permet d’accéder aux fonctions de gestion disponibles dans
l’application.

## Rapport Flake8

Depuis la racine du projet, activez l’environnement virtuel puis générez le
rapport HTML avec :

```bash
source .venv/bin/activate
python -m flake8 \
  --format=html \
  --htmldir=./flake8_rapport \
  --exclude=.venv,env,old,.git,__pycache__,flake8_rapport
```

Le rapport est créé dans `flake8_rapport/`. Ouvrez `flake8_rapport/index.html` dans
un navigateur pour consulter les résultats. Relancez la commande pour générer
un rapport actualisé après vos modifications.

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