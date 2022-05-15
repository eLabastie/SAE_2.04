# -*- coding: utf-8 -*-
"""
Created on Fri May  6 09:49:32 2022

@author: elabastie
"""

import matplotlib.pyplot as plt
import pyodbc
import pandas as p

conn=pyodbc.connect('DSN=elabastie_bd')

print("33[0;37;40m Normal textn")
print (" \n \n             Constructeur de graphiques sur les véhicules à 2 roues \n \n \n")
print("- Thème 1 : Accidents des deux roues selon l'état du sol ")
print('\n') 
print("- Thème 2 : Accidents des deux roues selon la cause de l'accident ")
print('\n') 
print("- Thème 3 : Accidents des deux roues selon l'heure de la nuit ")
print('\n') 
print("- Thème 4 : Évolution des accidents des deux roues sur une période ")


choix=input(" \n Veuillez choisir un thème (1,2,3,4) : ")



if choix=='1':
   print("  \n \n    Thème 1 : Accidents des deux roues selon l'état du sol")
    # Saisie des paramètres de la requête
   Etat_sol=input("\n Veullez indiquer l'etat du sol lors de l'accident \n 1:Humide, 2:Mouillee, 3:Enneigee, 4:Verglacee, 5:Gras boueux, 6:Gravillons, 7:Sec Normal \n : ")
   typegraph=input(" \n Voulez vous le taux d'accidents (1) ou le nombre d'accidents comparé aux véhicules (2) : ")
   if typegraph=='1':
       graph1=p.read_sql("SELECT MTypeImplication.libelleType as Nom  , (count(*) * 100.0 / 4611 ) as proba FROM MAccident INNER JOIN MEtatSurface on MAccident.etat_surface_id=MEtatSurface.code_etat_surface INNER JOIN MImplique on MAccident.impliq_id=MImplique.code INNER JOIN MTypeImplication on MImplique.type_code_implique=MTypeImplication.id WHERE (MAccident.etat_surface_id=" + Etat_sol + ") AND (MTypeImplication.id=2 ) GROUP BY Nom", conn)
       graph1.plot( kind="bar",x="Nom", y="proba", legend=False)
       typeG='Taux'
   elif typegraph=='2':
       graph1=p.read_sql("SELECT MTypeImplication.libelleType as Nom , COUNT(*) as Nombre  FROM MAccident INNER JOIN MEtatSurface on MAccident.etat_surface_id=MEtatSurface.code_etat_surface INNER JOIN MImplique on MAccident.impliq_id=MImplique.code INNER JOIN MTypeImplication on MImplique.type_code_implique=MTypeImplication.id WHERE (MAccident.etat_surface_id=" + Etat_sol + ") AND (MTypeImplication.id=2 OR MTypeImplication.id=3) GROUP BY Nom", conn)
       graph1.plot( kind="bar",x="Nom", y="Nombre", legend=False)
       typeG='Nombre'
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
       
   plt.title( typeG + " d'accidents de deux roues sur un sol " + Etat_sol )
   plt.show()
    
   
    
elif choix=='2':
    print("   \n   Thème 2 : Accidents des deux roues selon la cause de l'accident ")
     # Saisie des paramètres de la requête
    TypeCause=input(" \n Veuillez choisir une catégorie de cause ( perte de controle (1) , pieton (2) , non respect signalisation (3) , Autre (4) ) : \n ")
    if TypeCause=='1':
      NomCat='perte de contrôle'
      TypeCause='("Va stationner a gauche", "Perte de contrôle", "Défaut de maîtrise", "Maitrise du vehicule", "Dépassement a droite", "Dépassement en virage", "Dépassement en carrefour", "Dépassement en 3eme position", "Queue de poisson", "Dépassement dangereux", "Ecart sur le côté", "Roule à  gauche", "Heurte véhicule en stationnement interdit", "Entre sur la chaussée", "En intersection", "En section", "Depassement interdit ou dangereux", "Heurte un obstacle inerte", "Heurte un obstacle mobile","Roule en marche arrière")'
    elif TypeCause=='2':
        NomCat='pieton'
        TypeCause='("Circule sur le trottoir", "Depassement interdit ou dangereux", "Pieton", "Piéton montant dans un t.c.", "Piéton descendant dun t.c.", "Marche sur la chaussée", "Traverse sans précaution", "Traverse hors passage", "Non respect du piéton en section", "Entre ou sort de véhicule en stationnement", "Non respect du piéton en carrefour", "Joue ou travaille sur la chaussée", "Ouverture dune portière")'
    elif TypeCause=='3':
        NomCat='non respect signalisation'
        TypeCause='("non respect feux tricolores", "non respect des signaux", "non respect du stop" ,"Non respect priorité a droite" ,"Non respect priorité a droite (avec feux clignotant)", "Non respect priorité de face", "Non respect des panneaux d interdiction", "Sens interdit", "Tourne à  gauche interdit", "Tourne à  droite interdit", "Non respect dune balise")'
    elif TypeCause=='4':
        NomCat='Autre'
        TypeCause='("indéterminée", "Causes humaines" ,"eclairage insuffisant du véhicule", "Incident mécanique", "ivresse", "malaise", "infirme", "Eblouissement par les phares", "Demi-tour", "Manoeuvre sur parking", "Heurte un véhicule en stationnement", "Quitte le stationnement", "Mauvais positionnement (chgt de file)", "Marche arrière pour stationner", "Stationnement")'
    
    graph2=p.read_sql("SELECT (count(*) * 100.0 / 4611 ) as taux FROM MAccident as a INNER JOIN MCause as c on a.cause_id=c.Cause INNER JOIN MImplique as i on a.impliq_id=i.code WHERE i.type_code_implique=2 AND c.libelle IN " + TypeCause + "", conn)
    graph2.plot(kind="bar", y="taux")
    plt.title("Taux d'accidents du a la cause " + NomCat  )
    plt.show()   
    
elif choix=="3":
    print(" \n     Thème 3 : Accidents des deux roues selon l'heure de la nuit ")
    print("Luminosités renseignées dans la base de données : Nuit éclairée, Nuit éclairée insuffisant et Nuit sans éclairage")
    typeLum=input("Saisissez la luminosite à consulter (1,2,3) : ")
    if typeLum=="1":
        typeLum="Nuit eclairee"
    elif typeLum=="2":
        typeLum="Nuit eclairee insuffisant"
    elif typeLum=="3":
        typeLum="Nuit sans eclairage"
            
    graph3=p.read_sql("SELECT HOUR(MDate.DateFormatStandard) as Heure, (MLuminosite.libelle) as Luminosite, COUNT(MLuminosite.libelle_luminosite) as Nombre FROM MAccident INNER JOIN MDate on MAccident.date_id = MDate.date_id INNER JOIN MLuminosite on MAccident.lum_id = MLuminosite.code WHERE impliq_id = 2 AND MLuminosite.libelle = \"" + typeLum + "\" AND HOUR(MDate.DateFormatStandard) NOT BETWEEN 9 AND 15 GROUP BY Heure", conn)
    graph3.plot(kind="bar", x="Heure", y="Nombre")
    plt.title("Nombre d'accidents de deux roues lors d'une " + typeLum )
    plt.show()   


elif choix=='4':
    print(" \n \n     Thème 4 : Évolution des accidents des deux roues sur une période ")
    
    # Saisie des paramètres de la requête
    dateDeb=input("Choisissez la date de départ de la période à consulter (Entre 1984 et 1997) : ")
    dateFin=input("Choisissez la date de fin de la période à consulter (Entre 1984 et 1997) : ")
    
    graph4=p.read_sql("SELECT YEAR(MDate.DateFormatStandard) as Annee, COUNT(accident_id) as Nombre FROM MAccident INNER JOIN MDate ON MAccident.date_id = MDate.date_id WHERE impliq_id = 2 AND YEAR(MDate.DateFormatStandard) BETWEEN " + dateDeb + " AND " + dateFin + " GROUP BY Annee", conn)
    graph4.plot( x="Annee", y="Nombre")
    plt.title("Nombre d'accidents de deux roues entre " + dateDeb + " et " + dateFin)