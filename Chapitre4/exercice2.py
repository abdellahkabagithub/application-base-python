#création des 4 listes ("hiver,printemps,ete,autonome")
hiver = ["Decembre","Janvier","Fevrier"]
printemps = ["Mars","Avril","Mai"]
ete = ["Juin","Jeuillet","Août"]
autonome = ["Septembre","Octobre","Novembre"]
#creation de la liste saisons
saisons = [hiver , printemps, ete , autonome]
print(saisons)

# 1) saisons[2] // renvoie ["Juin","Jeuillet","Août"]
# 2) saisons[1][0] // renvoie ["Mars"]
# 3) saisons[1:2] // revoie ["Mars","Avril","Mais"]
# 4) saisons[:][1] // renvoie ["Mars","Avril","Mais"]
# Explication du dernier resultat 
#saisons[:] // renvoie tous le contenu de la liste puis on n'accroche [1] qui indique le choix de l'indice 1 contenant la liste printemps
