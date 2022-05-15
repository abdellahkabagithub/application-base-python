#Calcul des notes et mention d'un étudiant

note = [14,9,13,15,12]
print("Le Maximum des notes est : {} ". format(max(note)))
print("Le Minimum des notes est : {} ".format(min(note)))
som = 0
moy = 1
for i in note : 
    som+=i
    moy = som/len(note)
print(f"La Moyenne des notes est {moy} ")

print("Appréciation de la Moyenne ! ")
if moy >=10 and moy <12 :
    print(f"{moy} est 'Passable'")
elif moy >=12 and moy <14 :
    print(f"{moy} est  'assez bien' !")
else :
    print(f"{moy} est  'Bien' !")