# -*- coding: utf-8 -*-
"""
Created on Fri May  6 10:00:10 2022

@author: eetchever004
"""

import pyodbc
import matplotlib.pyplot as plt
import pandas

# Connexion lakartxela
conn=pyodbc.connect('DSN=BD_lakartxela')

# Affichage du menu
print("thème 1 : Accidents des deux roues selon l'état du sol")
print('\n')
print("thème 2 : Accidents des deux roues selon la cause de l'accident ")
print('\n')
print("thème 3 : Accidents des deux roues selon l'heure de la nuit ")
print('\n')
print("thème 4 : Évolution des accidents des deux roues sur une période ")

# Saisie du choix de l'utilisateur
choix=input("Veuillez choisir un thème (1,2,3,4) : ")
"""
if choix==1:

elif choix==2:
"""
elif choix==3:
    # Saisie des paramètres de la requête
    print("Luminosités renseignées dans la base de données : Nuit éclairée, Nuit éclairée insuffisant et Nuit sans éclairage")
    typeLum=input("Saisissez la luminosite à consulter (1,2,3,4) : ")
    """
SELECT HOUR(MDate.DateFormatStandard) as Heure, (MLuminosite.libelle_luminosite) as Luminosite, COUNT(MLuminosite.libelle_luminosite) as Nombre
FROM MAccident
INNER JOIN MDate on MAccident.date_id = MDate.date_id
INNER JOIN MLuminosite on MAccident.lum_id = MLuminosite.code
WHERE MLuminosite.libelle_luminosite = "Nuit eclairee"
GROUP BY Heure
"""
"""
elif choix==4:
    # Saisie des paramètres de la requête
    dateDeb=input("Choisissez la date de départ de la période à consulter (Entre 1984 et 1997) : ")
    dateFin=input("Choisissez la date de fin de la période à consulter (Entre 1984 et 1997) : ")
    
    graph4=pandas.read_sql("select ", conn)
    graph4.plot(x="Reference", y="QteStock")
    plt.show()
    """
    """
SELECT YEAR(MDate.DateFormatStandard) as Annee, COUNT(accident_id)
FROM MAccident
INNER JOIN MDate ON MAccident.date_id = MDate.date_id
GROUP BY Annee"""