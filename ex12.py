telefone = input("Telefone: ").replace("-", "")

if len(telefone) == 7:
    print("Telefone possui 7 dígitos. Vou adicionar o 3 na frente.")
    telefone = "3" + telefone
print(f"Telefone corrigido: {telefone[:4]}-{telefone[4:]}")
