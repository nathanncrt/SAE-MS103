# Tapez votre code ici
from random import *
a=0
b=9
nombre_alea=randint(a,b)
essai=int(input("Vous pariez sur quel nombre entre 0 et 9 ? :")) 
if essai >9:
    print("ATTENTION VOUS DEVEZ CHOISIR UN NOMBRE ENTRE 0 ET 9")
elif essai<0:
    print("ATTENTION VOUS DEVEZ CHOISIR UN NOMBRE ENTRE 0 ET 9")
elif essai == nombre_alea:
    print(f"Bravo ! C'était bien le {nombre_alea} qu'il fallait choisir !")
else:
    print(f"Perdu... il fallait jouer {nombre_alea} et pas {essai}")

