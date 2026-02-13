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