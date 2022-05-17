import os
#La fonction qui permet d'afficher le chemin du repertoire courant
repertoirCourant = os.getcwd()
print(f"Le Chemin du repertoire courant est : ''{repertoirCourant}'' ")
print("----------------------------------------------------------------------")
#La liste de tous les fichers contenant dans le repertoire courant
repertoirCourantFichiers = os.listdir()
print(f"Les Fichiers contenant dans le repertoire Courant est : {repertoirCourantFichiers}")

