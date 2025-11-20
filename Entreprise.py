liste_clients = ["Atangana","Moukoko","Ngono","Essomba"]

def ajouter_client(nom):
    if nom not in liste_clients:
        liste_clients.append(nom)
        depenses[nom] = 0.0
    else:
        return "Ce client existe déjà." 

def rechercher_client(nom):
    if nom in liste_clients:
        return True
    else:
        return False
def supprimer_client(nom):
    if nom in liste_clients:
        liste_clients.remove(nom)
        del depenses[nom]
    else:
        return "Ce client n'existe pas."
def menu_clients():
    while True:
        print("Menu Clients:")
        print("1. Ajouter un client")
        print("2. Rechercher un client")
        print("3. Supprimer un client")
        print("4. Afficher tous les clients")
        print("5. Quitter")
        choix = input("Choisissez une option: ")
        
        if choix == '1':
            nom = input("Entrez le nom du client à ajouter: ")
            resultat = ajouter_client(nom)
            if resultat:
                print(resultat)
            else:
                print(f"Client '{nom}' ajouté avec succès.")
        
        elif choix == '2':
            nom = input("Entrez le nom du client à rechercher: ")
            if rechercher_client(nom):
                print(f"Client '{nom}' trouvé.")
            else:
                print(f"Client '{nom}' non trouvé.")
        
        elif choix == '3':
            nom = input("Entrez le nom du client à supprimer: ")
            resultat = supprimer_client(nom)
            if resultat:
                print(resultat)
            else:
                print(f"Client '{nom}' supprimé avec succès.")
        
        elif choix == '4':
            print("Liste des clients:")
            for client in liste_clients:
                print(client)
        
        elif choix == '5':
            print("Quitter le menu clients.")
            break
        
        else:
            print("Option invalide. Veuillez réessayer.")

depenses = {}
for client in liste_clients:
    depenses[client] = 0.0
def ajouter_achat(nom, montant):
    if nom in depenses :
        for i in range (0,3):
            produit = input("Entrez le nom du produit acheté:")
            montant_produit = float(input("Entrez le montant du produit acheté en EUR:"))
            depenses[nom] += montant_produit
            print(f"Achat ajouté: {produit} pour {montant_produit} EUR")
            print(f"Dépense totale pour {nom}: {depenses[nom]} EUR")   
    else:
        print("Client non trouvé.")
def afficher_depenses():
    print("Dépenses des clients:")
    for client, montant in depenses.items():
        print(f"{client}: {montant} EUR")  
def menu_depenses():
    while True:
        print("Menu Dépenses:")
        print("1. Ajouter une dépense")
        print("2. Afficher les dépenses")
        print("3. Quitter")
        choix = input("Choisissez une option: ")
        
        if choix == '1':
            nom = input("Entrez le nom du client pour ajouter une dépense: ")
            if nom in liste_clients:
                ajouter_achat(nom, 0)
            else:
                print("Client non trouvé.")        

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
    
    
