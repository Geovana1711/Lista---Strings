nome = input("Diga uma palavra ")
quantidade__espaco = 0
for letra in nome:
    print(" " * quantidade__espaco+letra)
    quantidade__espaco +=1
