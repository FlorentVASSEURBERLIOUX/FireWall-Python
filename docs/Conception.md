# Firewall Basique en Python


Description :
-------------
Ce programme implémente un pare-feu basique en utilisant Python et `iptables` pour appliquer des règles de filtrage prédéfinis.
Il permet de bloquer ou autoriser des paquets en fonction de leur IP, port et protocole.

Modules et Fonctions :
----------------------

Classes :
- `FirewallRule` : Classe qui définit une règle de pare-feu, avec les propriétés comme IP source/destination, port, et protocole.
- `FirewallManager` : Classe qui gère l’ajout, la suppression et la consultation des règles de pare-feu.

Fonctions principales de la classe `FirewallRule` :
- `__init__(self, src_ip: str, dest_ip: str, port: int, protocol: str, action: str)` : 
      Initialise une règle avec des propriétés spécifiques.
- `to_command(self) -> str` : Convertit une règle en une commande `iptables` compatible.

Fonctions principales de la classe `FirewallManager` :


Utilisation :
-------------
L’utilisateur peut exécuter le programme en ligne de commande pour ajouter, supprimer ou afficher les règles du pare-feu.
Le programme interprète les règles et applique les commandes `iptables` au niveau système pour assurer le filtrage des paquets.

Prérequis :
-----------
- Python 3.11.0 (version dans laquelle le code a été produit).
- Droits administrateur pour utiliser `iptables`.
- Module `subprocess` de Python pour exécuter des commandes systèmes.


Notes :
-------
Les règles `iptables` appliquées via ce programme peuvent modifier la configuration réseau et perturber l'accès au système.
