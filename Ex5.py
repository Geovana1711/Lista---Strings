nome = input("Diga uma palavra ")
quantidade__espaco = len(nome)
for letra in nome:
    print(" " * quantidade__espaco+letra)
    quantidade__espaco -=1
