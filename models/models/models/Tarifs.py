class TarifsManager:
    TARIFS = {
        4: {"100": (35.0, 0.25), "200": (50.0, 0.20)}, # Partiel pour le moment
        5: {"100": (45.0, 0.30)},
        6: {"100": (60.0, 0.40)}
    }

    @staticmethod
    def obtenir_tarif(cylindree, forfait_km):
        pass

    @staticmethod
    def afficher_grille():
        pass