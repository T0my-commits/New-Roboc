#!/usr/bin/python3.7
#-*-coding:utf-8-*

# importation des modules;
import os

# création de la carte;
for carte in os.listdir('cartes/'):
	path = os.path.join('cartes/', carte)
	with open(path, 'r') as fichier:
		carte = CarteClass(fichier.read())
		carte.see()
		mv = input('>> ')
		carte.build(mv)
		carte.see()
		input()
