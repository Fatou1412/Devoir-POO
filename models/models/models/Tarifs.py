class TarifsManager:
    TARIFS = {
        4: {
            "100": (35.00, 0.25),
            "200": (50.00, 0.20),
            "300": (65.00, 0.15),
            "+300": (80.00, 0.10)
        },
        5: {
            "100": (45.00, 0.30),
            "200": (60.00, 0.25),
            "300": (75.00, 0.20),
            "+300": (95.00, 0.15)
        },
        6: {
            "100": (60.00, 0.40),
            "200": (80.00, 0.35),
            "300": (100.00, 0.30),
            "+300": (120.00, 0.25)
        }
    }

    @staticmethod
    def obtenir_tarif(cylindree, forfait_km):
        try:
            return TarifsManager.TARIFS[int(cylindree)][str(forfait_km)]
        except KeyError:
            return (0.0, 0.0)

    @staticmethod
    def afficher_grille():
        """Affiche la grille tarifaire formatée"""
        print("\n" + "=" * 70)
        print(f"{'GRILLE TARIFAIRE':^70}") # Le ^70 va me servir à centrer le titre
        print("=" * 70)
        
        print(f"{'Cylindrée':<15} | {'Forfait':<10} | {'Coût/Jour':>12} | {'Km Supp.':>12}")
        print("-" * 70) #<15 pour laisser de l'espace à la colonne cylindrée, <10 pour le forfait, >12 pour aligner à droite les prix

        for cyl in sorted(TarifsManager.TARIFS.keys()):
            for forfait, (journalier, supp) in TarifsManager.TARIFS[cyl].items():
                print(f"{cyl} cylindres   | {forfait:<10} | {journalier:>10.2f}€ | {supp:>10.2f}€")
            
            #Je créée une ligne de sépartion entre les groupes de cylindre
            print("-" * 20)