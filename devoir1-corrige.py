# coding:utf-8

# Je commence par un petit truc que j'ai découvert récemment.
# On peut référer à du code se trouvant dans d'autres fichiers avec la commande «from... import».
# La ligne ci-dessous importe donc notre gigantesque variable «publications» se trouvant dans le document devoir1.py (pas nécessaire d'inscrire «.py»)

from devoir1 import publications

# On commence par déclarer une série de variables dont on va se servir dans notre script
# Il s'agit essentiellement de compteurs

partages = 0 # Va nous servir à compter le nombre de partages pour CHACUN des médias
partagesTotal = 0 # Va nous servir à compter les partage pour L'ENSEMBLE des médias

reactions = 0 # Compte les réactions pour CHACUN des médias
reactionsTotal = 0 # Compte les réactions pour L'ENSEMBLE des médias

commentaires = 0 # Compte les commentaires pour CHACUN des médias
commentairesTotal = 0 # Compte les commentaires pour L'ENSEMBLE des médias

# La variable suivante servira à compter le nombre de publications par média et pour l'ensemble
# Je ne vous l'avais pas demandé, mais j'avais aussi envie de calculer des moyennes afin de comparer les médias entre eux
n = 0
nTotal = 0

# Voici enfin la variable la plus importante de ce script
# Elle nous permet de résoudre le problème que plusieurs ont évoqué: comment passer d'un média au suivant
# On a besoin de deux variables, en fait.
# Une pour mettre le nom du média de la ligne précédente
# L'autre pour mettre le nom du média correspondant à la ligne à laquelle on est rendu

# Comme on connaît le nom du premier média se trouvant dans notre grande variable «publications», on va immédiatement le mettre dans notre variable «mediaPrecedent»
mediaPrecedent = "104,7 Outaouais"

# On passe à travers chacune des publications de la variable «publications» avec cette boucle:
for publication in publications:

	# On commence par vérifier si le nom du média de la ligne qu'on traite est le même que celui de la ligne prédédente
	if mediaPrecedent == publication[0]:

		# Si on traite encore le même média, on ajoute 1 à notre compteur de publications
		n += 1

		# On ajoute aussi, à nos différentes variables, le nombre de partages, de réactions et de commentaires inclus dans la ligne qu'on traite
		partages += publication[3]
		reactions += publication[4]
		commentaires += publication[5]

		# On calcule enfin l'engagement en additionnant partages, réactions et commentaires
		engagement = partages + reactions + commentaires

	# Si le nom du média de la ligne à laquelle on est rendu n'est pas le même que celui de la ligne précédente,
	# c'est le signal qu'on a compté tout ce qu'il faut pour le média précédent
	else:

		# On imprime donc toutes les informations relatives à ce média
		print("~"*80,"    Les {} publications de cet échantillon du média {} sur Facebook ont été partagées {} fois, ont provoqué {} réactions et engendré {} commentaires, pour un engagement total de {} et un engagement moyen de {} par publication.".format(n,mediaActuel,partages,reactions,commentaires,engagement,(round((engagement/n),2))))

		# On en profite aussi pour ajouter à chacun de nos compteurs pour l'ensemble des médias le nombre des partages, des réactions et des commentaires pour le média précédent
		partagesTotal += partages
		reactionsTotal += reactions
		commentairesTotal += commentaires
		engagementTotal = partagesTotal + reactionsTotal + commentairesTotal
		nTotal += n

		# Une fois que l'impression est faite, on peut réinitaliser certaines variables

		# On met tout de suite le nom du média dans la variable «mediaPrecedent»
		mediaPrecedent = publication[0]

		# On «remet à zéro» notre compteur de publications... en fait, on lui donne la valeur de 1
		n = 1

		# On «remet à zéro» nos compteurs de partages, de réactions et de commentaires...
		# En fait, on leur donne la valeur des partages, réactions et commentaires de la ligne où on se trouve,
		# puis que c'est la première ligne d'un nouveau média dont on commence à recueillir les données
		partages = publication[3]
		reactions = publication[4]
		commentaires = publication[5]

	# La ligne suivante se trouve à l'extérieur de la condition «if... else»
	# Elle sert à s'assurer que la variable «mediaActuel» porte le nom du média qu'on vient tout juste de traiter
	# Ainsi, si la ligne suivante concerne un média différent, et qu'on exécute le code de la partie «else» de la condition,
	# c'est le contenu de la variable «mediaActuel» qui sera imprimé
	mediaActuel = publication[0]

# On a besoin de cette ligne à l'extérieur de la boucle pour imprimer les infos du dernier média de la grande variable «publications»
# Je ne le vous demandais pas, mais j'imprime également un engagement moyen par publication
print("~"*80,"    Les {} publications de cet échantillon du média {} sur Facebook ont été partagées {} fois, ont provoqué {} réactions et engendré {} commentaires, pour un engagement total de {} et un engagement moyen de {} par publication.".format(n,mediaActuel,partages,reactions,commentaires,engagement,(round((engagement/n),2))))

# Il faut procéder à un dernier calcul pour ajouter à nos compteurs pour l'ensemble des médias les données pour le dernier média de notre échantillon
partagesTotal += partages
reactionsTotal += reactions
commentairesTotal += commentaires
engagementTotal = partagesTotal + reactionsTotal + commentairesTotal
nTotal += n

# Cela ne vous était pas demandé, mais cette dernière ligne imprime les statistiques pour l'ensemble des médias de la variable «publications»
print("#"*80,"    Les {} publications de cet ensemble de médias ont été partagées {} fois, ont provoqué {} réactions et engendré {} commentaires, pour un engagement total de {} et un engagement moyen de {} par publication.".format(nTotal,partagesTotal,reactionsTotal,commentairesTotal,engagementTotal,(round((engagementTotal/nTotal),2))))