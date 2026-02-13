from datetime import datetime
from models.models.models.Tarifs import TarifsManager

class Reservation:
    def __init__(self, id_reservation, id_client, id_vehicule, date_debut, date_fin, forfait_km, cout_estime=0.0):
        """
        Constructeur de la classe Reservation.
        Le cout_estime est initialisé à 0.0 par défaut pour cette version.
        """
        self.id_reservation = id_reservation
        self.id_client = id_client
        self.id_vehicule = id_vehicule
        self.date_debut = date_debut  
        self.date_fin = date_fin      
        self.forfait_km = forfait_km  
        self.cout_estime = cout_estime

        if cout_estime == 0.0:
            self.cout_estime = self._calculer_cout_estime(cylindree)
        else:
            self.cout_estime = cout_estime

    def _calculer_cout_estime(self, cylindree):
        """Méthode privée pour calculer le coût total de la location"""
        # 1. Conversion des chaînes "AAAA-MM-DD" en objets date
        format_date = "%Y-%m-%d"
        d1 = datetime.strptime(self.date_debut, format_date)
        d2 = datetime.strptime(self.date_fin, format_date)
        
        # 2. Calcul de la différence de jours
        delta = (d2 - d1).days
        
        # Selon le sujet, si on loue et rend le même jour, cela compte pour 1 jour
        nb_jours = max(1, delta)
        
        # 3. Récupération du prix journalier via le TarifsManager
        prix_jour, prix_km_supp = TarifsManager.obtenir_tarif(cylindree, self.forfait_km)
        
        return float(nb_jours * prix_jour)
    
    def __str__(self):
        """Représentation textuelle simple pour le moment"""
        return f"Réservation {self.id_reservation} | Client: {self.id_client} | Véhicule: {self.id_vehicule}"

    def to_dict(self):
        """Prépare l'objet pour la sauvegarde JSON"""
        return vars(self)

    @staticmethod
    def from_dict(data):
        """Crée un objet Reservation à partir d'un dictionnaire JSON"""
        return Reservation(**data)