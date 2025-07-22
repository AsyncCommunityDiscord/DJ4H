# DJ4H


## Description

DJ4H est un bot Discord conçu pour le "Jeu des 4 heures" du serveur Async - Community 
(anciennement Graven - Développement). Son objectif premier est de permetttre le compte automatique des points.

Bien que conçu pour le serveur Async - Community, le bot peut être utilisé sur d'autres serveurs et fonctionner sur 
plusieurs serveurs simultanément.


## Fonctionnalités

Ce bot supporte les fonctionnalités suivantes :
- Compte automatique des points
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
