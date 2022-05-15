#soit la liste 
liste = ["vache","souris","levure","bacterie"] 
for elm in liste:
    print(elm)
print("----------------------")
for i in range(len(liste)):
    print(liste[i])
print("----------------------")
for i , animal in enumerate(liste):
    print("l'animal {} est {} " . format(i,animal))
print("-------------------")
for i in range(len(liste)) :
    print("L'animal {} est un (e) {}". format(i,liste[i]))
print("-------------------")
i = 0
while i <= len(liste):
    print(i)
    i+=i
