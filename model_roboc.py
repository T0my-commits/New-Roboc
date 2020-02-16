# -*-coding:Utf-*
#/usr/bin/python3.7

''' Classe simulant un classe de type list mais qui permet de selectionner un
élément à supprimer dans une liste grâce à son indice.
En somme, on redéfinit ici seulement la méthode remove(). '''

def nettoyer_liste(liste, indice, supprimer='.', remplacer='0'):
	''' fonction permettant de supprimer le '.' dans une liste, quand
	le personnage est censé le remplacer. '''
	liste = list(liste)
	semi_list1 = list()
	semi_list2 = list()

	for i,elements in enumerate(liste):
		if i < indice:
			semi_list1.append(elements)
		else:
			semi_list2.append(elements)

	semi_list2.remove(supprimer)
	semi_list2.insert(0, remplacer)

	liste = semi_list1 + semi_list2

	return liste


def depart_personnage(liste):
	''' fonction permettant de remplacer le personnage '0' par un point
	'.' quand celui-là se déplace. '''
	liste = list(liste)
