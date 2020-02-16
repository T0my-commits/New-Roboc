# -*-coding:Utf-8-*
#!/usr/bin/python3.7

"""
Fichier contenant la classe CarteClass.
Cette classe définit nos cartes et héberge les méthodes suivantes:
	- objet.see()		permet d'afficher la carte en couleurs;
	- objet.build(mv)	fais bouger notre personnage;
"""

# importation des modules;
from model_roboc import *

class CarteClass():
	''' classe permettant de modéliser une carte. '''

	def __init__(self, carte):
		''' constructeur de notre classe '''
		liste = []
		for caractere in carte:
			liste.append(caractere)
#		print(list)

		dico = {}
		list_dico = []
		indice = 0
		for caractere in liste:
#			print('CARACTERE :', caractere)
			if caractere != '\n':
				list_dico.append(caractere)
			else:
				dico[indice] = list(list_dico)
				list_dico = []
				indice += 1
#		print(dico)

		self.carte = list(liste)
		self.dictionnaire = dict(dico)

	def __repr__(self):
		''' représentation de notre carte. '''
		print(''.join(self.carte))

	def cleanScreen():
		if os.uname().sysname == 'Linux':
			os.system('clear')
		else:
			os.system('cls')

	def _mv_lateral(self, mouvement):
		''' méthode permettant un déplacement latéral d'un cran vers la gauche
		ou la droite du personnage.
		'''
		liste = list(self.carte)
		indice_personnage = [i for i,caractère in enumerate(self.carte) if caractère == '0']
		indice_personnage = indice_personnage[0]

		i = 1
		continuer = True
		while continuer:
			if liste[indice_personnage-i] == ' ':
				pass
			elif liste[indice_personnage-i] == '.' or liste[indice_personnage-i] == '/':
				liste = nettoyer_liste(liste, indice_personnage, '.', '0')
		
		self.carte = list(liste)

	def _mv_vertical(self, mouvement):
		''' méthode permettant un déplacement vertical d'un cran vers le haut
		ou le bas du personnage.
		'''
		dico = dict(self.dictionnaire)
		for cle in dico.keys():
			for indice,caractère in enumerate(dico[cle]):
				if caractère == '0':
					indice_personnage = (cle, indice)

		print(indice_personnage)
		print('DICTIONNAIRE', dico)
		dico.setdefault(indice_personnage[0]).remove('0')
		if mouvement == 'z':
			dico[indice_personnage[0]-1].insert(indice, '0')

			semi_list1 = []
			semi_list2 = []
			for indice,caractère in enumerate(dico[indice_personnage[0]-1]):
				if indice < indice_personnage[1]:
					semi_list1.append(caractère)
				elif indice >= indice_personnage[1]:
					semi_list2.append(caractère)

#			print(semi_list2)
#			print('\n', ''.join(dico[indice_personnage[0]]))
			semi_list2.remove('.')
			nouvelle_list = semi_list1 + semi_list2
			dico[indice_personnage[0]-1] = list(nouvelle_list)

		else:
			dico.setdefault(indice_personnage[0]+1).insert(indice, '0')

			semi_list1 = []
			semi_list2 = []
			for indice,caractère in dico.setdefault(indice_personnage[0]+1):
				if indice < indice_personnage[1]:
					semi_list1.append(caractère)
				elif indice >= indice_personnage[1]:
					semi_list2.append(caractère)

			semi_list2.remove('.')
			nouvelle_list = semi_list1 + semi_list2
			dico[indice_personnage[0]+1] = list(nouvelle_list)

		self.dictionnaire = dict(dico)
		i = 0
		liste = []
		while i <= len(dico)-1:
			for indice,element in enumerate(dico[i]):
				liste.append(element)
				i += 1
		self.carte = list(liste)

	def see(self):
		''' méthode représentant notre carte en couleurs. '''
		murs = '\x1b[1;2m' # gras et assombris;
		chemin = '\x1b[33;1m' # jaune et gras;
		extras = '\x1b[32;1;3m' # vert, gras et italique;
		personnage = '\x1b[35;4;1m' # violet, barré et gras;
		porte = '\x1b[33;1;3m' # violet et souligné;
		zero = '\x1b[0m' # remise à zéro;

#		print(self.carte)
		for caractère in self.carte:
			if caractère == '#':
				print(murs + caractère + zero, end='')
			elif caractère == '.':
				print(chemin + caractère + zero, end='')
			elif caractère == '>':
				print(porte + caractère + zero, end='')
			elif caractère == '/':
				print(porte + caractère + zero, end='')
			elif caractère == '0':
				print(personnage + caractère + zero, end='')
			elif caractère == '!' or '?':
				print(extras + caractère + zero, end='')
			else:
				pass
		return self.carte

	def build(self, mouvement):
		''' méthode permettant de faire évoluer notre personnage dans le labyrinte. '''
		
		if not isinstance(mouvement, str):
				raise TypeError
		elif len(mouvement) > 1:
			raise ValueError

		if mouvement == 'q' or mouvement == 'd':
			self._mv_lateral(mouvement)
		elif mouvement == 'z' or mouvement == 's':
			self._mv_vertical(mouvement)
		else:
			print('\n[ x ]  déplacement.. failed !')
	""" Fonction permettant de se déplacer. """
# On fait ici déplacer notre personnage. Le parcours est régie de la manière suivante :
#		- <0> : le personnage
#		- <.> : le personnage avance
#		- <#> : le personnage est bloque par le mur
#		- <//> : le personnage traverse la porte
#		- <?> : le personnage participe à un conversation
#		- <!> : le personnage bénificie d'une aide... ou le contraire !

# On défini le système de déplacements :
# On à les variables suivantes :
#	- parties : notre labyrinthe découpé {numéro:liste}
#	- parties_inversé : parties inversé {numéro:liste}
#	- liste_inversé : liste inversée [c,b,a]
#	- position : emplacement du personnage [liste,indice]
#	- déplacement : indications de déplacement du personnage [indice, direction]
#	effacer_ecran()	
#input()
	self.cleanScreen()

#	print("\n")
	if choix == 1:
		parties = unpickler('partie/parties.txt')
	elif choix == 0:
		parties_new = unpickler('partie/parties_new.txt')
		parties = partie(parties_new)
		enregistrer(parties, 'partie/parties.txt')
#		print(parties)
	afficher_labyrinthe()
	if pivot == 0:
		nombre_déplacements, direction_déplacements = pivotement(parties)
	else:
		nombre_déplacements, direction_déplacements = list(pivot)
#		print(pivot)
#		print(parties)
	numero_ligne, indice_liste = personnage()
# On crée des objets qui vont se parcourir à l'envers :
	variable = len(parties)
	parties_inversé = dict()
	while variable > 0:
		parties_inversé[list(parties.keys())[variable-1]] = list(parties.values())[variable-1]
		variable -= 1

	liste_inversé = list(parties[numero_ligne])
	liste_inversé.reverse()

# On défini les différentes issues :
#	afficher_labyrinthe(parties_inversé)
#	print(liste_inversé)
	if direction_déplacements == 'd':
		i = 0
		v = 0
		for i,v in enumerate(parties[numero_ligne]):
			if i > indice_liste:
				CheckLong(i,v,nombre_déplacements,direction_déplacements,numero_ligne,indice_liste)

	elif direction_déplacements == 'q':
		i = 0
		v = 0
		for i,v in enumerate(liste_inversé):
			new_indice_liste = len(parties[numero_ligne]) - indice_liste - 1
			if i > new_indice_liste:
				CheckLong(i,v,nombre_déplacements,direction_déplacements,numero_ligne,indice_liste,1)

	elif direction_déplacements == 's':
		i = 0
		v = 0
		for clé,valeur in parties.items():
			if clé >= numero_ligne:
				CheckUp(clé,valeur,nombre_déplacements,direction_déplacements,numero_ligne,indice_liste)

	elif direction_déplacements == 'z':
		i = 0
		v = 0
		#new_numero_ligne = len(parties) - numero_ligne
#		print("numero :", numero_ligne, new_numero_ligne)
		for clé,valeur in parties_inversé.items():
			if clé <= numero_ligne:
				CheckUp(clé,valeur,nombre_déplacements,direction_déplacements,numero_ligne,indice_liste,1)

	else:
		print("\n<ValueError> Vous devez saisir les bonnes lettres. Voici un rappel :\n\
- 'z': aller vers le haut\
- 's': aller vers le bas\n\
- 'q': aller vers la gauche\
- 'd': aller vers la droite\n")
		input("\nContinuer..")
		return déplacements(1)