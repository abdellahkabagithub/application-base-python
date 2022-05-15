#Parcourt des nombres paires
print('\n')
print("---Les nombres paires entre 0 et 20")
for i in range(0,20) :
    if i%2 == 0 :
        print(i , end= ',')

print('\n') 
print("---Les Nombres impairs qui sont supérieurs à 10")     
for i in range(0,20) :
    if i%2 != 0 and i > 9:
        print(i , end= ',')