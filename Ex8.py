#palindromo
palindromo = input("Diga uma palavra e direi se é um Palíndromo ")
reverso = palindromo[::-1]
if palindromo == reverso:
    print("É uma palíndromo")
else:
    print("Não é um palíndromo")
