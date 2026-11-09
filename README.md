# Gestionnaire de tournois d’échecs

Application en ligne de commande écrite en Python pour gérer des joueurs et
des tournois d’échecs. Elle permet notamment de créer les rencontres,
d’enregistrer les résultats et de consulter le classement. Les données sont
conservées localement dans des fichiers JSON.

## Prérequis

- Python 3
- `venv` et `pip` pour créer un environnement virtuel et installer les outils
  du projet

Sur Debian ou Ubuntu, installez Python et les outils nécessaires avec :

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

## Installation

Depuis la racine du dépôt, créez et activez un environnement virtuel.

Linux et macOS :

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell :

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Installez les dépendances :

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Les dépendances listées dans `requirements.txt` servent à Flake8 et à son
rapport HTML. L’application utilise par ailleurs les modules de la
bibliothèque standard de Python.

## Lancer l’application

À la racine du projet, avec l’environnement virtuel activé, lancez :

```bash
python main.py
```

Le menu principal propose les actions suivantes :

1. Créer un tournoi.
2. Modifier un tournoi.
3. Afficher les tournois.
4. Sélectionner un tournoi pour le gérer.
5. Créer un joueur.
6. Modifier un joueur.
7. Désactiver un joueur.
8. Afficher les joueurs.
0. Quitter.

Une fois un tournoi sélectionné, son menu permet d’inscrire des joueurs actifs,
de générer un tour et ses rencontres, de saisir ou modifier les résultats, de
terminer un tour, d’afficher les joueurs inscrits, de consulter leur classement
et d’afficher les tours et les rencontres.

Les noms et prénoms des joueurs sont affichés par ordre alphabétique. Le CNID 
d’un joueur doit être composé de deux lettres suivies de cinq chiffres (par exemple
`AB12345`) et être unique.

## Fonctionnement des tournois

- Un tournoi contient un nom, un lieu, des dates de début et de fin, une
  description, un nombre de tours et une liste de joueurs inscrits. Le nombre
  de tours est de 4 par défaut et doit être supérieur à zéro.
- Les joueurs doivent être inscrits au tournoi avant la génération des
  rencontres. Un joueur désactivé ne peut pas être inscrit.
- Le premier tour est apparié aléatoirement. Pour les tours suivants, les
  joueurs sont ordonnés selon leurs points ; les adversaires déjà rencontrés
  sont évités si un appariement sans revanche est possible. L’ordre des
  joueurs à égalité et la répartition des couleurs sont aléatoires.
- Si le nombre de joueurs est impair, un joueur reçoit une exemption (« bye »)
  et gagne un point. Le système privilégie un joueur qui n’a pas déjà reçu
  d’exemption.
- Les résultats possibles sont `1-0`, `0-1` et `1/2-1/2`. Les points sont
  respectivement `1–0`, `0–1` et `0,5–0,5`.
- Un tour ne peut être terminé qu’une fois que toutes ses rencontres ont un
  résultat. Une fois terminé, ses résultats ne peuvent plus être modifiés.
- Le classement est calculé par points décroissants, puis par ordre
  alphabétique du nom et du prénom.

## Architecture

Le projet sépare l’interface en ligne de commande, les règles de gestion, les
objets métier et le stockage :

| Dossier ou fichier | Responsabilité |
| --- | --- |
| `main.py` | Point d’entrée ; construit les dépôts, contrôleurs et vues, puis lance le menu principal. |
| `menus/` | Menus et interactions avec l’utilisateur : saisie, choix et messages. |
| `views/` | Affichage des joueurs, tournois, rencontres et classements. |
| `controllers/` | Orchestration des opérations sur les joueurs, tournois, tours, rencontres et classements. |
| `models/` | Objets métier `Player`, `Tournament`, `Round` et `Match`, ainsi que leur représentation en données. |
| `services/` | Logique d’appariement des joueurs et gestion des adversaires déjà rencontrés. |
| `repositories/` | Chargement et sauvegarde des joueurs et des tournois au format JSON. |
| `data/tournaments/` | Fichiers JSON utilisés pour conserver les joueurs et les tournois. |
| `.flake8` | Configuration de Flake8, notamment les exclusions et la longueur maximale des lignes. |
| `flake8_rapport/` | Rapport HTML généré par Flake8. |

Au démarrage, `main.py` charge les joueurs, puis charge les tournois en
reconstruisant les références des joueurs inscrits, des rencontres et des
exemptions à partir de leur CNID. Les contrôleurs appliquent les opérations
et demandent aux dépôts de sauvegarder les modifications.

## Données persistées

Les dépôts utilisent les fichiers suivants, relatifs à la racine du projet :

```text
data/
└── tournaments/
    ├── players.json
    └── tournaments.json
```

`players.json` conserve les informations des joueurs, dont leur statut actif.
`tournaments.json` conserve les informations des tournois, les CNID des joueurs
inscrits, les tours, les rencontres, les résultats et les dates. Il est
recommandé de sauvegarder ces fichiers avant toute modification manuelle.

## Générer le rapport Flake8

Depuis la racine du projet et avec l’environnement virtuel activé, exécutez :

```bash
python -m flake8 \
  --format=html \
  --htmldir=./flake8_rapport \
  --exclude=.venv,env,old,.git,__pycache__,flake8_rapport
```

La liste passée à `--exclude` évite d’analyser les environnements virtuels,
les caches, les fichiers Git et le rapport lui-même. Elle inclut `.venv`,
utilisé dans les instructions d’installation, ainsi que `env`, configuré dans
`.flake8`.

Ouvrez `flake8_rapport/index.html` dans un navigateur pour consulter le
rapport. Relancez la commande après vos modifications pour le mettre à jour.

Pour effectuer une vérification textuelle sans générer le rapport HTML :

```bash
python -m flake8
```

## Structure du projet

```text
Chess_tournament/
├── controllers/
├── data/
│   └── tournaments/
├── menus/
├── models/
├── repositories/
├── services/
├── views/
├── flake8_rapport/
├── .flake8
├── main.py
├── README.md
└── requirements.txt
```
