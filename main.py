taches = []
def afficher_menu():
    print("\n=== GESTION DES TACHES ===")
    print("1. Ajouter une taches 2. Afficher 3. rechercher 0. Quitter")

def ajouter_taches() :
    titre = input("Titre de la tache : ").strip()
    if titre == "":
        print("Erreur :le titre ne peut pas etre vide.")
    else:
        taches.append(titre)
        print("Tache ajoutée avec succes.")
def afficher_taches():
    if len(taches) == 0:
        print("Aucune tache dans la liste.")
    else:
        for i in range(len(taches)):
            print(f"{i+1}. {taches[i]}")

def rechercher_tache():
    mot_cle = input("Mot-cle a rechercher : ").strip().lower()
    trouve = False
    for i in range(len(taches)):
        if mot_cle in taches[i].lower():
            print(f"{i+1}. {taches[i]}")
            trouve = True
    if not trouve:
        print("Aucune tache ne correspond a ce mot-cle.")
def main():
    choix = ""
    while choix != "0":
        afficher_menu()
        choix = input("votre choix : ").strip()
        if choix =="1":
            ajouter_taches()
        elif choix =="2":
            afficher_taches()
        elif choix =="3":
            rechercher_tache()
        elif choix =="0":
            print("Au revoir !")
        else:
            print("Option invalid, veuillez reessayer .")
main()