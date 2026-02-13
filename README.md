
# 1. Classe `Client`
**Rôle :** Représente une personne physique enregistrée dans le système.
- **id_client** (int) : Identifiant unique du client.
- **nom** (str) : Nom de famille du client.
- **prenom** (str) : Prénom du client.
- **email** (str) : Adresse électronique de contact.
- **telephone** (str) : Numéro de téléphone.

# 2. Classe `Vehicule`
**Rôle :** Représente un véhicule disponible à la location.
- **id_vehicule** (int) : Identifiant unique du véhicule.
- **marque** (str) : Constructeur du véhicule.
- **modele** (str) : Modèle du véhicule.
- **cylindree** (int) : Nombre de cylindres (4, 5 ou 6), utilisé pour le calcul du tarif.
- **immatriculation** (str) : Numéro de plaque minéralogique.

# 3. Classe `Reservation`
**Rôle :** Gère le lien entre un client, un véhicule et une période donnée. Calcule automatiquement le coût prévisionnel.
- **id_reservation** (int) : Identifiant unique de la réservation.
- **id_client** (int) : Référence à l'identifiant du client.
- **id_vehicule** (int) : Référence à l'identifiant du véhicule.
- **date_debut** (str) : Date de début au format ISO (AAAA-MM-DD).
- **date_fin** (str) : Date de fin au format ISO (AAAA-MM-DD).
- **forfait_km** (str) : Type de forfait choisi ("100", "200", "300" ou "+300").
- **cout_estime** (float) : Montant calculé en fonction de la durée et de la cylindrée.

# 4. Classe `TarifsManager`
**Rôle :** Classe utilitaire (statique) contenant la grille tarifaire officielle et les méthodes de calcul des prix.