# Tapez votre code ici
sold_dep=int(input("Indiquez le solde de départ :"))
duree=int(input("Combien d'années d'intérêts voulez vous ?"))
taux=int(input("Quelle est le taux d'intérêts impliqués sur cette période ?"))

for i in range(0,12,1):
    interet=sold_dep*taux/100
    sold_dep=sold_dep+interet
    print(round(sold_dep,2))
print()