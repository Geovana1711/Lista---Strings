import random
# Tive que importar uma função de sortear
palavras = ["PYTHON", "PROGRAMA", "LOGICA", "COMPUTADOR", "ALGORITMO"]
palavra_secreta = random.choice(palavras).upper()
letras_descobertas = []
tentativas_restantes = 6
letras_chutadas = []
while tentativas_restantes > 0:
    display = ""
    for letra in palavra_secreta:
        if letra in letras_chutadas:
            display += letra + " "
        else:
            display += "_ "
    
    print(f"\nPalavra: {display}")
    print(f"Letras já tentadas: {letras_chutadas}")
    print(f"Tentativas restantes: {tentativas_restantes}")
    if "_" not in display:
        print("PARABÉNS! Você venceu! ")
        break

    chute = input("Digite uma letra: ").upper()
    if len(chute) != 1 or not chute.isalpha():
        print("Digite apenas UMA letra válida.")
        continue
    
    if chute in letras_chutadas:
        print("Você já tentou essa letra!")
        continue

    letras_chutadas.append(chute)
    if chute in palavra_secreta:
        print(f"Boa! A letra {chute} existe na palavra.")
    else:
        tentativas_restantes -= 1
        print(f"Putz, a letra {chute} NÃO existe.")
if tentativas_restantes == 0:
    print(f"\nGAME OVER! A palavra era: {palavra_secreta} ")
