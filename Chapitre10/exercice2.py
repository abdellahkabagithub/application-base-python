#Palindrome d'un mot
def palin(x):
    if x[::-1] == x :
        print("Bien il s'agit d'un mot palindromme")
    else :
        print("Desolé il ne s'agit pas d'un mot palindromme ! ")
#Exemple
palin("radar")