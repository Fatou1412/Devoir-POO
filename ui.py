class InterfaceUtilisateur:
    @staticmethod
    def afficher_menu():
        """Affiche le menu principal tel que défini dans l'annexe"""
        print("\n" + "=" * 60)
        print(f"{'SYSTÈME DE LOCATION DE VÉHICULES':^60}")
        print("=" * 60)
        print("1. Afficher les clients")
        print("2. Afficher les véhicules")
        print("3. Créer une réservation")
        print("4. Afficher la grille tarifaire")
        print("5. Afficher toutes les réservations")
        print("6. Afficher les réservations d'un client")
        print("7. Quitter")
        print("=" * 60)

    @staticmethod
    def saisir_choix():
        """Récupère le choix de l'utilisateur"""
        return input("\nVotre choix (1-7) : ")
    

    @staticmethod
    def afficher_clients(liste_clients):
        """Affiche la liste des clients (Option 1 du menu)"""
        print("\n" + "=" * 60)
        print(f"{'LISTE DES CLIENTS':^60}")
        print("=" * 60)
        
        if not liste_clients:
            print("Aucun client enregistré.")
        else:
            for client in liste_clients:
                # Ici, Python appelle automatiquement la méthode __str__ de la classe Client
                print(client)
                print("-" * 60)

    @staticmethod
    def afficher_vehicules(liste_vehicules):
        """Affiche la liste des véhicules (Option 2 du menu)"""
        print("\n" + "=" * 60)
        print(f"{'LISTE DES VÉHICULES':^60}")
        print("=" * 60)
        
        if not liste_vehicules:
            print("Aucun véhicule enregistré.")
        else:
            for vehicule in liste_vehicules:
                # Ici, Python appelle automatiquement la méthode __str__ de la classe Vehicule
                print(vehicule)
                print("-" * 60)