#!/usr/bin/python3.7
#-*-coding:utf-8-*

"""
	This file contain view_roboc.py
"""

# importation des modules;
from classe_carte import *
import os

# création de la carte;
liste_cartes = list()
for carte in os.listdir('cartes/'):
	path = os.path.join('cartes/', carte)
	with open(path, 'r') as fichier:
		carte = CarteClass(fichier.read())
		liste_cartes.append(carte)
		fichier.close()


print("\nListe des niveaux :")
for i,carte in enumerate(cartes.keys()):
	if i == len(cartes) - 1:
		print("   '- <{0}> - Level {0} : {1}.\n".format(i + 1, cartes.keys()[-1]))
	elif i < len(cartes):
		print("   |- <{0}> - Level {0} : {1}.".format(i + 1, cartes.keys()[i]))

# Récupération de l'état des parties précédentes ou création d'une nouvelle :
if os.path.exists('partie/parties_new.txt'):
	try:
		parties_new = unpickler('partie/parties_new.txt')
		assert os.path.exists('partie/parties.txt')
		if os.path.exists('partie/parties.txt'):
			parties = unpickler('partie/parties.txt')
		if len(parties_new) == 2 and type(parties_new) is tuple:
			print("Partie en cours:\n   |_ <{0}> - {1}.".format(len(cartes) + 1, parties_new[0]))
	except EOFError:
		parties_new = tuple()
		enregistrer(parties_new, 'partie/parties_new.txt')
		return selection_partie(cartes, parties_new)
	except AssertionError:
		parties_new = tuple()
		enregistrer(parties_new, 'partie/parties_new.txt')
		return selection_partie(cartes, parties_new)
else:
	parties_new = tuple()
	enregistrer(parties_new, 'partie/parties_new.txt')
return selection_partie(cartes, parties_new)