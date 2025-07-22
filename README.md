# DJ4H - Discord Bot

## Description

DJ4H est un bot Discord conçu pour le "Jeu des 4 heures" du serveur Async - Community 
(anciennement Graven - Développement). Son objectif premier est de permetttre le compte automatique des points.

Bien que conçu pour le serveur Async - Community, le bot peut être utilisé sur d'autres serveurs et fonctionner sur 
plusieurs serveurs simultanément.

DJ4H est un bot Discord qui implémente un jeu de timing compétitif appelé "Le jeu des 4h". Les joueurs s'affrontent en envoyant des messages dans un canal désigné après qu'une période de délai configurable soit écoulée depuis le dernier message.

## Fonctionnalités

Ce bot supporte les fonctionnalités suivantes :
- Comptage automatique des points
- Génération d'une image du classement
- Gestion des points des joueurs (définir/ consulter les scores)


## Commandes

Les paramètres de commandes obligatoires sont indiqués entre crochets (`[obligatoire]`) 
tandis que les paramètres optionnels sont placés entre parenthèses (`(optionnel)`).


### Configuration

Les commandes de cette section concernent la configuration du jeu et sont réservées 
aux utilisateurs ayant assez de privilèges.

- `/config [channel: discord.TextChannel] [delay]`: Définir le canal dans lequel le jeu prend place ainsi que le délai requis pour gagner un point
  - Exemple : `/config jeu-des-4-heures 4h` : Le jeu aura lieu dans le canal `#jeu-des-4-heures` avec un délai de `4 heures`. Les préfixes de temps sont les suivants :
    - `s`: Seconde
    - `m`: Minute
    - `h`: Heure
    - `d`: Jour
- `/set [member: discord.Member] [score: int]`: Définir le score d'un membre à la valeur `score`
  - Exemple : `/set gamingdy 4`: Le score de `@gamingdy` est désormais de `4`
- `/dump_log`: Obtenir le fichier de journaux du bot


### Joueur

Les commandes de cette section concernent les participants au jeu.

- `/leaderboard`: Obtenir une image avec le classement des 10 membres avec le plus de points
- `/score`: Obtenir son propre score


### Règles du jeu

1. Configurez un canal de jeu avec la commande appropriée
2. Les joueurs envoient des messages dans le canal
3. Un point est attribué au joueur précédent si le délai configuré s'est écoulé
4. Les scores sont suivis et affichés dans le leaderboard


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


## Base de données

Le bot utilise SQLite avec trois tables principales :
- `guilds` : Configuration des serveurs (channel, délai)
- `users` : Scores des utilisateurs par serveur
- `messages` : Suivi des messages pour la logique du jeu


## Support

Pour signaler des bugs ou demander des fonctionnalités, créez une issue sur le repository GitHub.
