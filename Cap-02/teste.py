print('Olá Mundo!')
print(2 + 2)

print("-=" * 10)

# Gere código Python que crie uma lista com os números entre 1 e 100 e então imprima os números pares,
# mas somente se o número for divisível por 4.

# Cria uma lista com os números entre 1 e 100
numeros = list(range(1, 101))

print(type(numeros))

# Percorre a lista e verifica se o número é par e divisível por 4
for numero in numeros:
    if numero % 2 == 0 and numero % 4 == 0:
        print(numero)

print("-=" * 10)

# Gere código Python que crie uma lista com os números entre 1 e 100 e então imprima os números pares,
# mas somente se o número for divisível por 4, usando list comprehension.

# Cria uma lista com os números entre 1 e 100
numeros = list(range(1, 101))

# Usa a list comprehension para gerar uma lista somente com os números pares e divisíveis por 4
pares_div4 = [numero for numero in numeros if numero % 2 == 0 and numero % 4 == 0]

print(pares_div4)
print(type(pares_div4))
