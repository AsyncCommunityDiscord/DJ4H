# DJ4H - Discord Bot

DJ4H est un bot Discord qui implémente un jeu de timing compétitif appelé "Le jeu des 4h". Les joueurs s'affrontent en envoyant des messages dans un canal désigné après qu'une période de délai configurable soit écoulée depuis le dernier message.

## Installation

### Prérequis

- Python 3.9+
- Poetry (pour la gestion des dépendances)

### Installation des dépendances

```bash
# Cloner le repository
git clone <repository-url>
cd DJ4H

# Installer les dépendances avec Poetry
poetry install
```

## Configuration

### Variables d'environnement

Créez un fichier `.env` à la racine du projet avec les variables suivantes :

```env
BOT_TOKEN=votre_token_discord_bot
DEBUG_GUILD_ID=id_du_serveur_de_dev  # Optionnel
DATABASE_PATH=dj4h.db  # Optionnel, par défaut dj4h.db
```

- `BOT_TOKEN` : Token de votre bot Discord (requis)
- `DEBUG_GUILD_ID` : ID du serveur Discord pour le développement (optionnel)
- `DATABASE_PATH` : Chemin vers le fichier de base de données SQLite (optionnel)

## Lancement

### Mode développement

```bash
# Lancer le bot
poetry run python main.py
```

### Mode production avec Docker

```bash
# Build et lancement avec Docker Compose
docker-compose -f compose-prod.yml up -d
```

### Mode développement avec Docker

```bash
# Build et lancement avec Docker Compose
docker-compose up -d
```

## Fonctionnalités

### Commandes disponibles

- `/leaderboard` : Affiche le classement des joueurs avec une image générée
- `/score` : Affiche le score d'un joueur spécifique

### Règles du jeu

1. Configurez un canal de jeu avec la commande appropriée
2. Les joueurs envoient des messages dans le canal
3. Un point est attribué au joueur précédent si le délai configuré s'est écoulé
4. Les scores sont suivis et affichés dans le leaderboard

## Base de données

Le bot utilise SQLite avec trois tables principales :
- `guilds` : Configuration des serveurs (channel, délai)
- `users` : Scores des utilisateurs par serveur
- `messages` : Suivi des messages pour la logique du jeu

## Développement

### Formatage du code

```bash
# Formater le code avec Black
poetry run black .
```

### Structure du projet

```
DJ4H/
├── main.py                    # Point d'entrée
├── config.py                  # Configuration et logging
├── commands/                  # Commandes Discord
│   ├── cogs/game.py          # Commandes /leaderboard et /score
│   └── handler/events.py     # Logique principale du jeu
├── utils/
│   ├── database/             # Couche base de données
│   │   ├── connection.py     # Connexion SQLite
│   │   ├── schema.py         # Modèles de données
│   │   └── dao/              # Objets d'accès aux données
│   └── image_generator.py    # Génération d'images pour leaderboard
└── docker/                   # Configuration Docker
```

## Support

Pour signaler des bugs ou demander des fonctionnalités, créez une issue sur le repository GitHub.