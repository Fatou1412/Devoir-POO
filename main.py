from ui import InterfaceUtilisateur
from data_manager import DataManager

def main():
    # Chargement initial des données
    client = DataManager.charger_client("data/clients.json")
    vehicule = DataManager.charger_vehicule("data/vehicules.json")
    
    continuer = True
    while continuer:
        InterfaceUtilisateur.afficher_menu()
        choix = InterfaceUtilisateur.saisir_choix()
        
        if choix == "1":
            InterfaceUtilisateur.afficher_client(client)
        elif choix == "2":
            InterfaceUtilisateur.afficher_vehicule(vehicule)
        elif choix == "7":
            print("Au revoir !")
            continuer = False
        
            
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