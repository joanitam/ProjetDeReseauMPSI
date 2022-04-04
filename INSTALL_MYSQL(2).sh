#!/bin/sh

#Installation des dependances pour l'installation de mysql#

#Mise à jour du systeme#
apt update

#installation des packages#
apt install mariadb-client
apt install mariadb-server

#demarrage du service mariadb#
systemctl start mariadb.service
