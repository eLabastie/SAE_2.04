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

if choix=='1':
    print("      Thème 1 : Accidents des deux roues selon l'état du sol")
    # Saisie des paramètres de la requête
    Etat_sol=input("Veullez indiquer l'etat(s) du sol lors de l'accident \n 1:Humide, 2:Mouillee,  3:Enneigee, 4:Verglacee, 5:Gras boueux, 6:Gravillons, 7:Sec_Normal \n (1 OR 2 OR 5) : ")
   

elif choix=='2':
    print("      Thème 2 : Accidents des deux roues selon la cause de l'accident ")
     # Saisie des paramètres de la requête
        
elif choix=='3':
    print("      Thème 3 : Accidents des deux roues selon l'heure de la nuit ")
    # Saisie des paramètres de la requête
    print("Luminosités renseignées dans la base de données : Nuit éclairée, Nuit éclairée insuffisant et Nuit sans éclairage")
    typeLum=input("Saisissez la luminosite à consulter (1,2,3,4) : ")
    if typeLum=="1":
        typeLum="Nuit eclairee"
    elif typeLum=="2":
        typeLum="Nuit eclairee insuffisant"
    elif typeLum=="3":
        typeLum=="Nuit sans eclairage"
    elif typeLum=="4":
            
    graph3=pandas.read_sql("SELECT HOUR(MDate.DateFormatStandard) as Heure, (MLuminosite.libelle) as Luminosite, COUNT(MLuminosite.libelle_luminosite) as Nombre FROM MAccident INNER JOIN MDate on MAccident.date_id = MDate.date_id INNER JOIN MLuminosite on MAccident.lum_id = MLuminosite.code WHERE impliq_id = 2 AND MLuminosite.libelle = " + luminosite + " AND HOUR(MDate.DateFormatStandard) NOT BETWEEN 9 AND 15 GROUP BY Heure, conn)
    graph3.plot(kind="bar", x="Annee", y="Nombre")
    plt.show()  
    


elif choix=='4':
     print("      Thème 4 : Évolution des accidents des deux roues sur une période ")
    
    # Saisie des paramètres de la requête
    dateDeb=input("Choisissez la date de départ de la période à consulter (Entre 1984 et 1997) : ")
    dateFin=input("Choisissez la date de fin de la période à consulter (Entre 1984 et 1997) : ")
    
    graph4=p.read_sql("SELECT YEAR(MDate.DateFormatStandard) as Annee, COUNT(accident_id) as Nombre FROM MAccident INNER JOIN MDate ON MAccident.date_id = MDate.date_id WHERE impliq_id = 2 AND YEAR(MDate.DateFormatStandard) BETWEEN " + dateDeb + " AND " + dateFin + " GROUP BY Annee", conn)
    graph4.plot( x="Annee", y="Nombre")
    plt.show()
