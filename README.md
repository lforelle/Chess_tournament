# Gestionnaire de tournois d'échecs

Application en ligne de commande permettant de gérer les joueurs et les tours
d'un tournoi d'échecs.

## Fonctionnalités

### Gestion des joueurs

- Créer, afficher, modifier et supprimer un joueur.
- Valider les données saisies :
  - nom et prénom composés de lettres, espaces ou tirets ;
  - date de naissance au format `JJ/MM/AAAA` ;
  - CNID au format `AB12345` (deux lettres suivies de cinq chiffres).
- Conserver les joueurs dans `data/players_data/players.json` entre deux
  lancements.

### Gestion des tours et des rencontres

- Générer automatiquement le prochain tour à partir des joueurs enregistrés.
- Effectuer un tirage aléatoire des appariements et des couleurs au premier
  tour.
- Classer les joueurs selon leurs points pour les tours suivants.
- Éviter les adversaires déjà rencontrés lorsque cela est possible ; les
  nouvelles rencontres sont privilégiées avant d'autoriser une revanche.
- Gérer un nombre impair de joueurs : un joueur exempt reçoit un point, en
  privilégiant ceux qui n'ont pas déjà été exempts.
- Saisir les résultats `1-0`, `0-1` ou `1/2-1/2` des rencontres du dernier
  tour.
- Terminer un tour uniquement lorsque tous ses résultats sont enregistrés.
- Empêcher la modification d'un tour terminé et la création d'un nouveau tour
  tant que le précédent n'est pas terminé.
- Afficher le classement des joueurs, avec leur total de points.
- Conserver les tours, rencontres, résultats, joueurs exempts et dates de début
  et de fin dans `data/matches_data/matches.json`.

## Lancer le programme

Depuis la racine du projet :

```bash
python main.py
```

Le menu principal donne accès à la gestion des joueurs, à la génération des
tours, à la saisie des résultats, à la clôture d'un tour et au classement.

## Architecture du projet

```text
Chess_tournament/
├── main.py                         # Point d'entrée
├── menus/                          # Menus interactifs
├── models/                         # Modèles Player, Round et Match
├── controllers/                    # Logique métier
├── repositories/                   # Lecture et écriture des données JSON
├── views/                          # Affichage dans le terminal
├── data/
│   ├── players_data/players.json   # Joueurs persistés
│   └── matches_data/matches.json   # Tours et rencontres persistés
└── requirements.txt                # Dépendances du projet
```
