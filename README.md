# Gestionnaire de tournois d'échecs

Application en ligne de commande pour gérer les joueurs d'un tournoi d'échecs.

## Fonctionnalités disponibles

- Créer un joueur avec son nom, prénom, date de naissance, classement et identifiant national d'échecs (CNID).
- Afficher la liste numérotée des joueurs enregistrés.
- Modifier les informations d'un joueur.
- Supprimer un joueur après confirmation.
- Conserver les joueurs entre deux lancements dans `data/players_data/players.json`.
- Valider les données saisies :
  - nom et prénom composés de lettres, espaces ou tirets ;
  - date de naissance au format `JJ/MM/AAAA` ;
  - classement numérique ;
  - CNID au format `AB12345` (deux lettres suivies de cinq chiffres).

## Lancer le programme

Depuis la racine du projet :

```bash
python menu.py
```

## État du développement

Les modèles et fichiers de base pour les tournois, les tours et les matchs sont présents dans le projet. Leur gestion depuis le menu principal et leur persistance ne sont pas encore implémentées ; les options correspondantes ne réalisent donc aucune action à ce stade.

## Architecture du projet

```text
Chess_tournament/
├── menu.py                         # Point d'entrée et menu principal
├── menus/                           # Menus de création, modification et suppression
├── models/                         # Modèles Player, Tournament, Round et Match
├── controllers/                    # Logique métier
├── repositories/                   # Accès aux données des joueurs
├── views/                          # Affichage dans le terminal
├── data/
│   ├── players_data/players.json   # Données persistées des joueurs
│   └── tournaments_data/            # Données de tournois (préparation)
└── requirements.txt                # Dépendances de développement
```
    
