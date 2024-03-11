# Capítulo 6 - Função Map

# Função Map
# A função map() em Python é uma função que aplica uma determinada função a cada elemento de uma estrutura de dados
# iterável (como uma lista, tupla ou outro objeto iterável). A função map() retorna um objeto que pode ser convertido
# em outra estrutura de dados, como uma lista, se necessário.

# Função Python que retorna um número ao quadrado
def potencia(x):
    return x ** 2


# Função 1 - Recebe uma temperatura como parâmetro e retorna a temperatura em Fahrenheit
def fahrenheit(t):
    return (float(9) / 5) * t + 32


# Função 2 - Recebe uma temperatura como parâmetro e retorna a temperatura em Celsius
def celsius(t):
    return (float(5)/9) * (t - 32)


numeros = [1, 2, 3, 4, 5]
numeros_ao_quadrado = list(map(potencia, numeros))
print(numeros_ao_quadrado)

# Criando uma lista
temperaturas = [0, 22.5, 40, 100]

# Aplicando a função a cada elemento da lista de temperaturas.
# Em Python 3, a funçãp map() retornar um iterator
map(fahrenheit, temperaturas)
# Função map() retornando a lista de temperaturas convertidas em Fahrenheit
print(list(map(fahrenheit, temperaturas)))
# Usando um loop for para imprimir o resultado da função map()
for temp in map(fahrenheit, temperaturas):
    print(temp)

# Convertendo para Celsius
map(celsius, temperaturas)
print(list(map(celsius, temperaturas)))

# Usando expressão lambda
map(lambda x: (5.0/9) * (x - 32), temperaturas)
print(list(map(lambda x: (5.0/9) * (x - 32), temperaturas)))

# Somando os elementos de 2 listas
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
print(list(map(lambda x, y: x + y, a, b)))

# Somando os elementos de 3 listas
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = [9, 10, 11, 12]
print(list(map(lambda x, y, z: x + y + z, a, b, c)))
