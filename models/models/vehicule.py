class Vehicule:
    def __init__(self, id_vehicule, marque, modele, cylindree, kilometrage, date_mise_en_circulation):
        self.id_vehicule = id_vehicule 
        self.marque = marque 
        self.modele = modele 
        self.cylindree = int(cylindree) 
        self.kilometrage = kilometrage 
        self.date_mise_en_circulation = date_mise_en_circulation 

    def __str__(self):
        return f"{self.id_vehicule}\n{self.marque} {self.modele} ({self.cylindree} cyl., {self.kilometrage} km)" 
    
    def to_dict(self):
        return vars(self) 

    @staticmethod
    def from_dict(data):
        return Vehicule(**data) 

    