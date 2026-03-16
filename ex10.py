unidades = ["Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", 
            "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove"]
dezenas = ["", "", "Vinte", "Trinta", "Quarenta", "Cinquenta", "Sessenta", "Setenta", "Oitenta", "Noventa"]
num = int(input("Digite um número até 99: "))

if num < 20:
    print(unidades[num])
else:
    d = num // 10
    u = num % 10
    if u == 0:
        print(dezenas[d])
    else:
        print(f"{dezenas[d]} e {unidades[u]}")
