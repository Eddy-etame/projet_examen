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






for client in liste_clients:
    depenses[client] = 0
def ajouter_depense(nom, montant):
    if nom in depenses:
        depenses[nom] += montant
    else:
        return "Ce client n'existe pas."
def afficher_depenses():
    print("Dépenses des clients:")
    for client, montant in depenses.items():
        print(f"{client}: {montant} unités")
def menu_depenses():
    while True:
        print("\nMenu Dépenses:")
        print("1. Ajouter une dépense")
        print("2. Afficher les dépenses")
        print("3. Quitter")
        choix = input("Choisissez une option: ")
        
        if choix == '1':
            nom = input("Entrez le nom du client: ")
            try:
                montant = float(input("Entrez le montant de la dépense: "))
                resultat = ajouter_depense(nom, montant)
                if resultat:
                    print(resultat)
                else:
                    print(f"Dépense de {montant} unités ajoutée pour le client '{nom}'.")
            except ValueError:
                print("Montant invalide. Veuillez entrer un nombre.")
        
        elif choix == '2':
            afficher_depenses()
        
        elif choix == '3':
            print("Quitter le menu dépenses.")
            break
        
        else:
            print("Option invalide. Veuillez réessayer.")











print("Bienvenue dans le système de gestion des clients et des dépenses.")
print("MENU PRINCIPAL:")
while True:
    print("1. Gérer les clients")
    print("2. Gérer les dépenses")
    print("3. Quitter le programme")
    choix_utilisateur = input("Choisissez une option: ")
    
    if choix_utilisateur == '1':
        menu_clients()
    elif choix_utilisateur == '2':
        menu_depenses()
    
    
