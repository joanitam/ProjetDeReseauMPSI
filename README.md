# ProjetDeReseauMPSI
Projet reseau MPSI

# DOCUMENTATION DU PROJET PYTHON RÉSEAU

## Environnement technique

Pour l'installation de nos trois machines virtuelles, nous avons installé 
VirtualBox.  

Nous avons réalisé le travail avec trois machines virtuelles 

1. **Machine Server**
     


2. **Machine client**



3. **Machine « Man in the middle »**

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
- Installation des packages de IredMail depuis un depot github

    ```
    apt -y install wget
    wget https://github.com/iredmail/iRedMail/archive/refs/tags/1.5.2.tar.gz
    ```

- Extraction du fichier et deplacement dans le dossier

    ```
    tar xvf 1.5.2.tar.gz
    cd iRedMail-1.5.2
    ```
- Attribution des droits

    ```
    chmod +x iRedMail.sh
    ```

- Execution du script

    ```
    pwd
    bash iRedmail.sh
    ```
