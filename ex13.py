import random
#importei de novo
palavra = "PYTHON"
lista_letras = list(palavra) 
random.shuffle(lista_letras) 

embaralhada = "".join(lista_letras) # Junta tudo de novo
print(f"A palavra é: {embaralhada}")

chute = input("Qual é a palavra? ").upper()
if chute == palavra:
    print("Acertou!")
else:
    print(f"Errou! Era {palavra}")
