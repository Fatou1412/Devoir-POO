import json
import os
from models.client import Client
from models.models.vehicule import Vehicule

class DataManager:
    @staticmethod
    def charger_clients(chemin_fichier):
        """Lit le fichier JSON et retourne une liste d'objets Client"""
        if not os.path.exists(chemin_fichier):
            return []
        
        with open(chemin_fichier, 'r', encoding='utf-8') as f:
            donnees = json.load(f)
            # On transforme chaque dictionnaire du JSON en objet Client
            return [Client.from_dict(d) for d in donnees]

    @staticmethod
    def charger_vehicules(chemin_fichier):
        """Lit le fichier JSON et retourne une liste d'objets Vehicule"""
        if not os.path.exists(chemin_fichier):
            return []
            
        with open(chemin_fichier, 'r', encoding='utf-8') as f:
            donnees = json.load(f)
            return [Vehicule.from_dict(d) for d in donnees]