#!/bin/bash

#Installation des packages de IredMail depuis un depot github#

apt -y install wget

#wget https://github.com/iredmail/iRedMail/archive/1.4.2.tar.gz
wget https://github.com/iredmail/iRedMail/archive/refs/tags/1.5.2.tar.gz


#Extraction du fichier et deplacement dans le dossier#
tar xvf 1.5.2.tar.gz
cd iRedMail-1.5.2


#execution du script iredmail#

#attribution des droits#
chmod +x iRedMail.sh

#execution du script#
pwd
bash iRedmail.sh
