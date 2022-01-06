# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 11:03:54 2022

@author: Administrateur
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 08:41:31 2021
@author: Administrateur
"""

import numpy as np
import datetime

try:
    #with open("evenementSAE_15.ics", encoding="utf8") as fh:
    with open("extrait.txt", encoding="utf8") as fh:
        res=fh.read()
except:
        print("Le fichier n'existe pas %s", os.path.abspath(chemin))
#res=tools_sae.lecture_fichier("ADE_Cal.ics")
ress=res.split('\n')
#comptage=ress.count('BEGIN:VEVENT')
tableau_evenements=np.array([])
for event in ress:
    # Initialisation chaine de carcatere
    if event.startswith('11:42'):
        texte=event.split(" ")
        evenement='temps : '+texte[0]+' emetteur : '+texte[2]+' destinataire : '+texte[4]+' flag : '+texte[6]
print(evenement)