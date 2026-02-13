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