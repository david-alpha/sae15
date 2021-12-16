# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 08:41:31 2021

@author: Administrateur
"""

import numpy as np
import datetime

try:
    #with open("evenementSAE_15.ics", encoding="utf8") as fh:
    with open("evenementSAE_15.ics", encoding="utf8") as fh:
        res=fh.read()
except:
        print("Le fichier n'existe pas %s", os.path.abspath(chemin))
#res=tools_sae.lecture_fichier("ADE_Cal.ics")
ress=res.split('\n')
#comptage=ress.count('BEGIN:VEVENT')
tableau_evenements=np.array([])
for event in ress:
    # Initialisation chaine de carcatere
    if event.startswith('BEGIN:VEVENT'):
        evenement=''
    # Code ressource
    if event.startswith('UID'):
        texte1=event.split(":")
        UID=texte1[1]
    #Date ressource    
    if event.startswith('DTSTART'):
        texte1=event.split(":")
        annee1=texte1[1][0:4]
        mois1=texte1[1][4:6]
        jour1=texte1[1][6:8]
        Date1=jour1+"-"+mois1+"-"+annee1+";"
        texte2=texte1[1].split("T")
        heure1=texte2[1][0:2]
        minute1=texte2[1][2:4]
        Date1=Date1+heure1+":"+minute1
    # Duree ressource    
    if event.startswith('DTEND'):
        texte1=event.split(":")
        annee2=texte1[1][0:4]
        mois2=texte1[1][4:6]
        jour2=texte1[1][6:8]
        Date2=jour2+"-"+mois2+"-"+annee2+";"
        texte2=texte1[1].split("T")
        heure2=texte2[1][0:2]
        minute2=texte2[1][2:4]
        Date2=Date2+heure2+":"+minute2+";"
        maDate1 = datetime.datetime(int(annee1),int(mois1),int(jour1),int(heure1),int(minute1), 0)
        maDate2 = datetime.datetime(int(annee2),int(mois2),int(jour2),int(heure2),int(minute2), 0)
        Duree='0'+str(maDate2-maDate1)[:-3]
        
evenement=UID+';'+Date1+';'+Duree+';'+Date2
print(evenement)