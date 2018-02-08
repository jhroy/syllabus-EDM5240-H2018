# -*- coding: utf-8 -*-
# ©2016 Jean-Hugues Roy. GNU GPL v3.

n = 0
for a in reversed(range(1930,2019)): # Boucle qui passe toutes les années en ordre inverse, de 2016 à 1930
	for x in range(1001,2000): # Boucle qui passe les 1000 numéros de permis possible à chaque année 
		n += 1
		noPermis = "{}{}".format(str(a)[2:],str(x)[1:]) # On confectionne chaque numéro de permis en assemblant des parties de nos deux boucles
		print("On recherche le {}e permis: {}".format(n,noPermis)) # Affichage à l'écran pour chacun des numéros de permis potentiels vérifiés