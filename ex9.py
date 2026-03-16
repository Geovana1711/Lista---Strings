cpf_raw = input("Digite o CPF (xxx.xxx.xxx-xx): ")
cpf = cpf_raw.replace(".", "").replace("-", "")
if len(cpf) != 11 or cpf == cpf[0] * 11:
    print("CPF Inválido!")
else:
    soma = 0
    peso = 10
    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1
    
    digito1 = (soma * 10) % 11
    if digito1 == 10: digito1 = 0 
    soma = 0
    peso = 11
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1
        
    digito2 = (soma * 10) % 11
    if digito2 == 10: digito2 = 0
    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
        print(f"O CPF {cpf_raw} é VÁLIDO!")
    else:
        print(f"O CPF {cpf_raw} é INVÁLIDO!")
