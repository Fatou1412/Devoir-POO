Client:
   Attributs: "id_client" (chaîne), "nom", "prenom", "mail", "telephone", "adresse

Véhicule:
    Attributs: "id_vehicule" (chaîne), "marque", "modele", "cylindree"
    (entier : 4, 5 ou 6), "kilometrage_actuel" (nombre), "date_mise_en_circulation" (chaîne ou date)

Réservation:
    Attributs: "id_reservation", "id_client", "id_vehicule", "date_depart" (format "AAAA-MM-JJ"), "date_retour" (format "AAAA-MM-JJ"), "forfait_km" (100, 200, 300 ou +300),"cout_journalier", "prix_km_supp", "cout_estime