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


print (" \n \n             Constructeur de graphiques sur les véhicules à 2 roues \n \n \n")
# Affichage du menu
print("- Thème 1 : Accidents des deux roues selon l'état du sol ")
print('\n') 
print("- Thème 2 : Accidents des deux roues selon la cause de l'accident ")
print('\n') 
print("- Thème 3 : Accidents des deux roues selon l'heure de la nuit ")
print('\n') 
print("- Thème 4 : Évolution des accidents des deux roues sur une période ")


choix=input(" \n Veuillez choisir un thème (1,2,3,4) : ")

# Saisie du choix de l'utilisateur

choix=input("Veuillez choisir un thème (1,2,3,4) : ")

if choix=='1':
    print("      Thème 1 : Accidents des deux roues selon l'état du sol")
    # Saisie des paramètres de la requête
    Etat_sol=input("\n Veullez indiquer l'etat(s) du sol lors de l'accident \n 1:Humide, 2:Mouillee,  3:Enneigee, 4:Verglacee, 5:Gras boueux, 6:Gravillons, 7:Sec Normal \n : ")
   
   graph1=p.read_sql("SELECT MTypeImplication.libelleType as Nom , COUNT(*) as Nombre , (count(*) * 100.0 / 4611 ) as proba FROM MAccident INNER JOIN MEtatSurface on MAccident.etat_surface_id=MEtatSurface.code_etat_surface INNER JOIN MImplique on MAccident.impliq_id=MImplique.code INNER JOIN MTypeImplication on MImplique.type_code_implique=MTypeImplication.id WHERE (MAccident.etat_surface_id=" + Etat_sol + ") AND (MTypeImplication.id=2 ) GROUP BY Nom", conn)
   graph1.plot( kind="bar",x="Nom", y="proba", legend=False)
   
   if Etat_sol=='1':
       Etat_sol="Humide"
   elif Etat_sol=='2':
       Etat_sol="Mouillee"
   elif Etat_sol=='3':
       Etat_sol="Enneigee"
   elif Etat_sol=='4':
       Etat_sol="Verglacee"
   elif Etat_sol=='5':
       Etat_sol="Gras Boueux"
   elif Etat_sol=='6':
       Etat_sol="Gravillions"
   elif Etat_sol=='7':
       Etat_sol="Sec Normal"
       
   plt.title("Taux d'accidents de deux roues sur un sol " + Etat_sol )
   plt.show()
   

elif choix=='2':
    print("      Thème 2 : Accidents des deux roues selon la cause de l'accident ")
     # Saisie des paramètres de la requête
        
elif choix=="3":
    print("Luminosités renseignées dans la base de données : Nuit éclairée, Nuit éclairée insuffisant et Nuit sans éclairage")
    typeLum=input("Saisissez la luminosite à consulter (1,2,3) : ")
    if typeLum=="1":
        typeLum="Nuit eclairee"
    elif typeLum=="2":
        typeLum="Nuit eclairee insuffisant"
    elif typeLum=="3":
        typeLum="Nuit sans eclairage"
            
    graph3=pandas.read_sql("SELECT HOUR(MDate.DateFormatStandard) as Heure, (MLuminosite.libelle) as Luminosite, COUNT(MLuminosite.libelle_luminosite) as Nombre FROM MAccident INNER JOIN MDate on MAccident.date_id = MDate.date_id INNER JOIN MLuminosite on MAccident.lum_id = MLuminosite.code WHERE impliq_id = 2 AND MLuminosite.libelle = \"" + typeLum + "\" AND HOUR(MDate.DateFormatStandard) NOT BETWEEN 9 AND 15 GROUP BY Heure", conn)
    graph3.plot(kind="bar", x="Heure", y="Nombre")
    plt.show()   
    


elif choix=="4":
    # Saisie des paramètres de la requête
    
    dateDeb=saisieVerif(1984, 1997, "Choisissez la date de départ de la période à consulter (Entre 1984 et 1997) : ")
    dateFin=saisieVerif(1984, 1997, "Choisissez la date de fin de la période à consulter (Entre 1984 et 1997) : ")
    
    #creation du graph
    graph4=pandas.read_sql("SELECT YEAR(MDate.DateFormatStandard) as Annee, COUNT(accident_id) as Nombre FROM MAccident INNER JOIN MDate ON MAccident.date_id = MDate.date_id WHERE impliq_id = 2 AND YEAR(MDate.DateFormatStandard) BETWEEN " + dateDeb + " AND " + dateFin + " GROUP BY Annee", conn)
    graph4.plot(x="Annee", y="Nombre")
    plt.show()
