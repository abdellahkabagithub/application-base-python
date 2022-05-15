
#Affiche le nombre de 1 à 10
for i in range(1,11) : 
    print(i , end=',')
print("\n")
#Nombres paires et impaires
impairs = [1 , 3 , 5 , 7 , 9 , 11 , 13 , 15 , 17 , 19 , 21]
print("Nombre pairs à partir des impairs")
for i in impairs : 
    x = i+1
    print(x , end=' , ')
print("\n")
#Calcul de la moyenne
notes = [14 , 9 , 6 , 8 , 12]
som = 0
moy = 1
for i in notes :
    som+=i
    moy = som / len(notes)
print("-----La moyenne des notes d'étudiant-----")
print(f"la moyenne des notes est : {moy} ")
print("--Le produit des nombres consécutifs--")
#Produit des nombres consécutifs
liste = [2]  
liste.extend([4,6,8,10,12,14,16,18,20,22])
som = 0
p = 1
for i in liste :
    x = i*(i+2)
    print(x)
print("\n")
print("--------------------------")
for i in range(1,21) :
    if(i%2 == 0) : 
        x = i*(i+2)
        print(x)
