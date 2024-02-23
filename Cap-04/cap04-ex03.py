# Capítulo 4 - Strings e Indexação

# Criando uma String
# Para criar uma string em Python você pode usar aspas simples ou duplas. Por exemplo:

print('Oi')                                                             # Uma única palavra
print('Criando uma string em Python')                                   # Uma frase
print("Podemos usar aspas duplas ou simples para strings em Python")    # Podemos usar aspas duplas
print("Testando strings em 'Python'")                                   # Você pode combinar aspas duplas e simples

print("-=" * 15)   # ------------------------------------------------------------

# Imprimindo uma String
print('Testando Strings em Python')
print('Testando \n Strings \n em \n Python')
print('\n')                                                             # Imprime uma linha vazia

print("-=" * 15)   # ------------------------------------------------------------

# Indexando Strings
# Indexação em Python começar por zero.

s = 'Data Science Academy'   # Atribuindo uma string
print(s)
print(s[0])                  # Primeiro elemento da string
print(s[1])                  # Segundo elemento da string
print(s[2])                  # Terceiro elemento da string
print(s[3])                  # Quarto elemento da string

# Podemos usar um : para executar um slicing que faz a leitura de tudo até um ponto designado. Por exemplo:
print(s[1:])
# Retorna todos os elementos da string, começando pela posição
# (lembre-se que Python começa a indexação pela posição 0), até o fim da string.

print(s[:3])    # Retorna tudo até a posição de índice 3
print(s[:4])    # Retorna tudo até a posição de índice 4
print(s[-1])    # Nós também podemos usar a indexação negativa e ler de trás para frente
print(s[:-1])   # Retornar tudo, exceto a última letra

# Nós também podemos usar a notação de índice e fatiar a string em pedaços específicos (o padrão é 1).
# Por exemplo, podemos usar dois pontos duas vezes em uma linha e, em seguida, um número que especifica a frequência
# para retornar elementos.

print(s[::1])
print(s[::2])
print(s[::-1])

print("-=" * 15)   # ------------------------------------------------------------

# Propriedades de Strings

# Alterando um caracter (não é possível alterar um elemento da string)
# s[0] = 'x' -> Ira ocasionar um erro

print(s + ' é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dados!')

s = s + ' é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dados!'
print(s)

letra = "w"
print(letra * 3)     # Podemos usar o símbolo de multiplicação para criar repetição!

print("-=" * 15)   # ------------------------------------------------------------

# Funções Built-in de Strings

print(s.upper())      # Upper Case
print(s.lower())      # Lower case
print(s.split())      # Dividir uma string por espaços em branco (padrão)
print(s.split('y'))   # Dividir uma string por um elemento específico

print("-=" * 15)   # ------------------------------------------------------------

# Funções String

s = 'seja bem vindo ao universo da Linguagem Python!'
print(s.capitalize())
print(s.count('a'))
print(s.isalnum())
print(s.islower())
print(s.isspace())
print(s.endswith('o'))

s = '1000'
print(s)
print(type(s))

print("-=" * 15)   # ------------------------------------------------------------

# Comparando Strings

print("Python" == "R")
print("Python" == "Python")
