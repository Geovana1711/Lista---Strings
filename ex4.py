frase = input("Diga uma frase ").lower()
contador_espacos = 0
contador_vogais = 0
vogais = ["a","e","i","o","u"]
for letra in frase:
    if letra == " ":
     contador_espacos += 1
    elif letra in vogais:
     contador_vogais += 1

print(f"O número de espaços é de {contador_espacos} e o número de vogais é {contador_vogais}")

