# Tapez votre code ici
m=0
n=int(input("Saisissez le nombre de rangée(s)")) #L'utilisateur tape le nombre de rangée(s) ici
for i in range(1,n+1,1): #Démarrage de la boucle
    m=m+i
print(f"Numéro de la rangée {i}. Nombre de maccarons total {m}") #print le résultat