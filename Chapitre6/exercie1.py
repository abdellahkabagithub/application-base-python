# Soit la liste des jours de la semaine
semaine = ["Lundi","Mardi","Mercredi","jeudi","Vendredi","Samedi","Dimanche"]

for i in semaine :
    if i == "Lundi" or i == "Mardi" or i == "Mercredi" :
        print(f"{i} Au Travail")
    elif i == "Vendredi" :
        print(f"Chouette c'est le {i}")
    elif i == "Samedi" or i == "Dimanche":
        print(f"{i} Repos ce week-end")


