# -*-coding:Utf-8-*
#!/usr/bin/python3.7

""" Interface graphique pour Roboc. """

# importation des modules;
import os
from tkinter import *
from classe_carte import *

# création de notre objet contenant notre labyrinte;
for carte in os.listdir('cartes/'):
	path = os.path.join('cartes/', carte)
	with open(path, 'r') as fichier:
		laby = CarteClass(fichier.read())

# création de notre carte graphique;
oslow = ''.join(laby.see())

# création de l'interface graphique;
f = Tk()
ecrit = Label(f, text=oslow)
ecrit.pack()
f.mainloop()
from tkinter import *

f = Tk()    # création de notre objet Tk;
print('\x1b[3;34m' + "\n[ ✔ ] création de l'objet Tk().. fait !")

# création d'un label (ce qui s'affiche dans la fenetre);
label = Label(f, text='test avec idle')
label.pack()
print("[ ✔ ] création d'un label.. fait !")


