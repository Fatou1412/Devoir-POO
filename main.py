from ui import InterfaceUtilisateur

def main():
    continuer = True
    
    while continuer:
        InterfaceUtilisateur.afficher_menu()
        choix = InterfaceUtilisateur.saisir_choix()
        
        if choix == "1":
            print("\n[Action] Affichage des clients bientôt disponible...")
        elif choix == "2":
            print("\n[Action] Affichage des véhicules bientôt disponible...")
        elif choix == "7":
            print("\nAu revoir !")
            continuer = False
        else:
            print("\nOption non implémentée ou choix invalide.")

if __name__ == "__main__":
    main()