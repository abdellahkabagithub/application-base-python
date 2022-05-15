#Affiche le min dans une liste
liste = [8,6,2,5]

for i in liste :
    if liste[0] > liste[i] :
        liste[0] = liste[i]
print("le plus petit est {}".format(liste[0]))