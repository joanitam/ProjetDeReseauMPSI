# ProjetDeReseauMPSI
Projet reseau MPSI

# DOCUMENTATION DU PROJET PYTHON RÉSEAU

## Environnement technique

Pour l'installation de nos trois machines virtuelles, nous avons installé 
VirtualBox. 
Et comme indiqué dans le projet, nous avons installé deux machines virtuelles linux et une machine virtuelle Kali

1. **Machine Server**
     Ubuntu 20.04
2. **Machine client**
    Ubuntu 20.04
3. **Machine « Man in the middle »**
    KaliLinux
***
## Documentation des scripts

1. **INSTALL_ALL_DEPENDANCES(1).sh**

Ce script execute les scriptes **INSTALL_MYSQL(1).sh** et  **INSTALL_IREDMAIL_DEPENDANCES(1).sh** qui servent respectivement à installer et configurer MySQL (la base de données) et IRedMail (le serveur de messagerie)  .

2. **INSTALL_MYSQL(1).sh**

Ce script exécute les actions suivantes :
- Mise à jour du système    
    ```
    apt update
    ```
- Installation des packages Mariadb et Mariadb-server
    ``` 
    apt install mariadb-client
    apt install mariadb-server 
    ```
- Démarrage du service mariadb
    ```
    systemctl start mariadb.service
    ```
---
3. **INSTALL_IREDMAIL_DEPENDANCES(1).sh**
Ce script exécute les actions suivantes :
installation de toutes les dépendances requises pour l’installation de IREDMAIL

Lancement des scripts

Cote serveur
Le script etablit une communication avec le client et récupère les informations entrées par le client pour effectuer 
des enregistrements dans la base de données. 

sudo python3 server.py
saisi du mot de passe
Demarrage du serveur

cote client 
le script client.py permet d'interagir avec le serveur en ecoute, tous deux sur le meme port.
Avec le script, une connexion est etablie avec le serveur se trouvant dans le meme reseau
lancement du script client.py et en fonction de l'option choisi le serveur reagit

sudo python3 client.py
 L'option 1 correspond à la connexion de l'utilisateur qui existe déjà dans la base de données
 L'option 2 correspond à l'inscription d'un utilisateur qu'on enrégistre dans la base de données
 L'option 3 consiste à quitter




    
