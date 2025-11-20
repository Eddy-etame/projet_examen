liste_clients = ["raphael", "Anthony", "Eddy", "Essomba"]
def ajouter_client(nom):
    if nom not in liste_clients:
        liste_clients.append(nom)
        depenses[nom] = 0.0
        print(f"Le client {nom} a été ajouté à la liste.")
    else:
        print(f"Le client {nom} existe déjà.")
def supprimer_client(nom):
    reponse = input("etes-vous sur de vouloir supprimer le client ? (o/n)")
    if reponse == "o":
        if nom in liste_clients:
            liste_clients.remove(nom)
            if nom in depenses:
                del depenses[nom]
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

def menu_gestion_clients():
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
            reponse = input("Souhaitez-vous retourner au menu principal ? (o/n)")
            if reponse == "o":
                we_are_enterprise()
        elif choix == "2":
            nom = input("Entrez le nom du client : ")
            supprimer_client(nom)
            reponse = input("Souhaitez-vous retourner au menu principal ? (o/n)")
            if reponse == "o":
                we_are_enterprise()
        elif choix == "3":
            afficher_clients()
            reponse = input("Souhaitez-vous retourner au menu principal ? (o/n)")
            if reponse == "o":
                we_are_enterprise()
        elif choix == "4":
            nom = input("Entrez le nom du client : ")
            rechercher_client(nom)
            reponse = input("Souhaitez-vous retourner au menu principal ? (o/n)")
            if reponse == "o":
                we_are_enterprise()
            print
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide!. Veuillez recommencer.")

depenses = {}
for client in liste_clients:
    depenses[client] = 0.0
def ajouter_achat(nom, montant):
    if nom in depenses :
        true = 0
        while True:
            produit = input("Entrez le nom du produit acheté:").strip().lower()
            montant_produit = 0 
            for item in catalogue:  
                if item[0].lower() == produit:  
                    montant_produit = item[1] 
                    true += 1
                    break  
            if montant_produit == 0:
                print("Le produit non trouvé.")
            else:
                depenses[nom] += montant_produit
                print(f"Achat ajouté: {produit} pour {montant_produit} EUR")
                print(f"Dépense totale pour {nom}: {depenses[nom]} EUR")
                if true == 3:
                    break
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
            we_are_enterprise()
        
        else:
            print("Option invalide. Veuillez réessayer.")

nom_produit = ("pistache /kg", "taps /kg", "Avocat", "pomme de terre /kg", "montre")
prix_produit = (2, 1, 0.85, 3, 5)
catalogue_produits = (nom_produit, prix_produit)
catalogue = []
for i in range(len(nom_produit)):
        catalogue.append((nom_produit[i], prix_produit[i]))
#for i in range(len(nom_produit)):
 #   catalogue.append((nom_produit[i], prix_produit[i]))
  #  print(catalogue, "euros")
#catalogue_produits = (catalogue)
#print(catalogue_produits)

def afficher_catalogue():
    print("Catalogue des produits:")
    catalogue_produits = (catalogue)
    for nom_produit, prix in catalogue_produits.items():
        print(f"{nom_produit}: {prix} EUR")

def ajouter_produit():
    nom_produit = input("Entrez le nom du produit: ")
    if any(produit[0].lower() == nom_produit.lower() for produit in catalogue):
        print("Le produit existe déjà.")
    else:
        prix_produit = float(input("Entrez le prix du produit: "))
        catalogue.append((nom_produit, prix_produit))
        print(f"Le produit '{nom_produit}' a été ajouté avec le prix {prix_produit} EUR.")

def supprimer_produit():
    nom_produit = input("Entrez le nom du produit: ")
    for produit in catalogue:
        if produit[0] == nom_produit:
            catalogue.remove(produit)
            print(f"Le produit {nom_produit} a été supprimé.")
            break
        else:
            print(f"Le produit {nom_produit} n'existe pas.")
        catalogue_produits = (catalogue)
        print(catalogue_produits)

def menu_gestion_produits():
    while True:
        print("Menu Gestion des Produits:")
        print("1. Afficher le catalogue des produits")
        print("2. Ajouter un produit")
        print("3. Supprimer un produit")
        print("4. Quitter")
        choix = input("Choisissez une option: ")
        if choix == '1':
            afficher_catalogue()
        elif choix == '2':
            ajouter_produit()
        elif choix == '3':
            supprimer_produit()
        elif choix == '4':
            print("Voulez-vous vraiment quitter le menu gestion des produits ? (o/n)")
            reponse = input("Choisissez une option: ")
            if reponse == 'o':
                we_are_enterprise()
                break
        else:
            print("Option invalide. Veuillez réessayer.")

def chiffre_d_affaires():
    total = sum(depenses.values())
    print(f"Chiffre d'affaires total: {total} EUR")
def meilleur_client():
    if depenses:
        meilleur = max(depenses)
        print(f"Meilleur client: {meilleur} avec des dépenses de {depenses[meilleur]} EUR")
    else:
        print("Aucun client trouvé.")
def client_depense_moins():
    if depenses:
        moins_depensier = min(depenses)
        print(f"Client avec le moins de dépenses: {moins_depensier} avec des dépenses de {depenses[moins_depensier]} EUR")
    else:
        print("Aucun client trouvé.")
def depenses_moyennes():
    if depenses:
        moyenne = sum(depenses.values()) / len(depenses)
        print(f"Dépense moyenne par client: {moyenne} EUR")
    else:
        print("Aucun client trouvé.")
def tri_clients_par_depenses():
    clientstrier = sorted(depenses.items(), reverse=True)
    print("Clients triés par dépenses (du plus élevé au plus bas):")
    for client, montant in clientstrier:
        print(f"{client}: {montant} EUR") 

def menu_gestion_entreprise():
    while True:
        print("Menu Données de l'Entreprise:")
        print("1. Chiffre d'affaires total")
        print("2. Meilleur client")
        print("3. Client avec le moins de dépenses")
        print("4. Dépense moyenne par client")
        print("5. Trier les clients par dépenses")
        print("6. Quitter")
        choix = input("Choisissez une option: ")
        
        if choix == '1':
            chiffre_d_affaires()
        
        elif choix == '2':
            meilleur_client()
        
        elif choix == '3':
            client_depense_moins()
        
        elif choix == '4':
            depenses_moyennes()
        
        elif choix == '5':
            tri_clients_par_depenses()
        
        elif choix == '6':
            print("Quitter le menu données de l'entreprise.")
            break
        
        else:
            print("Option invalide. Veuillez réessayer.")

def we_are_enterprise():
    print("Bienvenue dans l'entreprise, We are Enterprise!")
    print("Vous etes dans le systeme de gestion des clients et des dépenses.")
    print("MENU PRINCIPAL:")
    while True:
        print("1. Gérer les clients")
        print("2. Gérer les dépenses")
        print("3. Gérer les produits")
        print("4. Gérer les donnees de l'entreprise")
        print("5. Quitter le programme")
        choix_utilisateur = input("Choisissez une option: ")
        if choix_utilisateur == '1':
            menu_gestion_clients()
        elif choix_utilisateur == '2':
            menu_depenses()
        elif choix_utilisateur == '3':
            menu_gestion_produits()
        elif choix_utilisateur == '4':
            menu_gestion_entreprise()
        elif choix_utilisateur == '5':
            print("Au revoir !")
            break
        else:
            print("Choix invalide!. Veuillez recommencer.")

we_are_enterprise()








