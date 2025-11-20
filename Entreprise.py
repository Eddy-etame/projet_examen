liste_clients = ["raphael", "Anthony", "Eddy"]

def ajouter_client(nom):
    if nom not in liste_clients:
        liste_clients.append(nom)
        print(f"Le client {nom} a été ajouté à la liste.")
    else:
        print(f"Le client {nom} existe déjà.")
def supprimer_client(nom):
    reponse = input("etes-vous sur de vouloir supprimer le client ? (o/n)")
    if reponse == "o":
        if nom in liste_clients:
            liste_clients.pop(nom, 0)
            print(f"Le client {nom} a été supprimé de la liste.")
        else:
            print(f"Le client {nom} n'existe pas.")
    else:
        print("Le client n'a pas été supprimé.")

def afficher_clients():
    print("Liste des clients :\n")
    for client in liste_clients:
        print(client, sep ="," )
def rechercher_client(nom):
    if nom in liste_clients:
        print(f"Le client {nom} existe.")
    else:
        print(f"Le client {nom} n'existe pas.")

def gestion_des_clients():
    while True:
        print("Bienvenue dans la gestion des clients")
        print("Que voulez-vous faire ?")
        print("1. Ajouter un client")
        print("2. Supprimer un client")
        print("3. Afficher la liste des clients")
        print("4. Rechercher un client")
        print("5. Quitter")
        choix = input("Entrez votre choix : ")
        if choix == "1":
            nom =input("Entrez le nom du client : ")
            ajouter_client(nom)
            reponse = input("voulez vous continuer ? (o/n)")
            if reponse == "o":
                continue
            else:
                break
        elif choix == "2":
            nom = input("Entrez le nom du client : ")
            supprimer_client(nom)