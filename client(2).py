import socket
import json
host= "192.168.10.1"
port = 5566
clientInfo = [] #Creation de la variable qui va contenir les information du client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creation de socket
try:
   
    client.connect((host, port))  # Connexion au server avec le host et le port
    data = client.recv(1024)
    data = data.decode("utf8")
    print(data)
    print("1. ModeConnexion :")
    print("2. ModeInscription :")
    print("3. Quitter :")
    choix = int(input("S'il vous plait faites un choix  : "))
    if choix == 1:
        #Le client entre les coordonnées de connexion
        mail = input("Saisi d'adresse mail :")
        mdp = input("Saisi du mot de passe :")
        clientInfo.append(mail)
        clientInfo.append(mdp)
        #On definit le type d'operation
        clientInfo.append("Connexion")
        #On le transforme en JSOn
        messagesend = json.dumps(clientInfo)
        messagesend = messagesend.encode("utf8")
        #On l'envoi au serveur
        client.sendall(messagesend)
        #On recupere la reponse du serveur puis on l'affiche
        data = client.recv(1024)
        data = data.decode("utf8")
        print(data)
    elif choix == 2 :
        #Le client insert les coordonnees
        nom = input("Saisi du nom :")
        mail = input("Saisi du prenom :")
        mdp = input("Saisi du mot de passe :")
        mdp1 = input("Confirmation du mot de passe :")
        if mdp == mdp1 :
                clientInfo.append(nom)
                clientInfo.append(mail)
                clientInfo.append("Inscription")
                clientInfo.append(mdp)
                 #On le transforme en JSOn
                messagesend = json.dumps(clientInfo)
                messagesend = messagesend.encode("utf8")
                #On l'envoi au serveur
                client.sendall(messagesend)
                #On recupere la reponse du serveur puis on l'affiche
                data = client.recv(1024)
                data = data.decode("utf8")
        else:
            print("Mot de passe identique")
        pass
    elif choix == 3 :
        print("Quitter")
        exit()
    else:
        print("choix inccorect")
        pass

except Exception as e:
    print(e)
finally:
    #On ferme la connection
    client.close()


