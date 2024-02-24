# Capítulo 4 - Variáveis e Operadores

var_teste = 1              # Atribuindo o valor 1 a variável var_teste
print(var_teste)           # Imprimindo o valor da variável

var_teste = 2              # Alterar o valor da variável var_teste de 1 para 2
print(var_teste)           # Imprimindo o valor da variável

print(type(var_teste))     # Verificar o tipo da variável

var_teste = 9.5            # Alterar o valor da variável var_teste de 2 para 9.5
print(type(var_teste))     # Verificar o tipo da variável

x = 4                      # Atribuindo o valor 4 a variável x
print(x)                   # Imprimindo o valor da variável

print("-=" * 15)   # ------------------------------------------------------------

# Declaração Múltipla

pessoa1, pessoa2, pessoa3 = "Bob", "Maria", "Ana"
print(pessoa1)
print(pessoa2)
print(pessoa3)

fruta1 = fruta2 = fruta3 = "Melancia"
print(fruta1)
print(fruta2)
print(fruta3)

print("-=" * 15)   # ------------------------------------------------------------

# Pode-se usar letras, números e underline em nome de variável (mas não se pode começar com números).

x1 = 50
print(x1)

#  Ira dar erro  ->  x1 = 50

"""
    Não se pode usar palavras reservadas como nome de variável
    Ex: break = 1
"""

print("-=" * 15)   # ------------------------------------------------------------

# Variáveis Atribuídas a Outras Variáveis e Ordem dos Operadores

largura = 2
altura = 4
area = largura * altura
print(area)

perimetro = 2 * largura + 2 * altura
print(perimetro)

perimetro = 2 * (largura + 2) * altura      # A ordem dos operadores é a mesma seguida na Matemática
print(perimetro)

print("-=" * 15)   # ------------------------------------------------------------

# Operações com Variáveis

idade1 = 25
idade2 = 35

print(idade1 + idade2)
print(idade2 - idade1)
print(idade2 * idade1)
print(idade2 / idade1)
print(idade2 % idade1)

print("-=" * 15)   # ------------------------------------------------------------

# Concatenação de Variáveis

nome = "Bob"
sobrenome = "Marley"
fullName = nome + " " + sobrenome
print(fullName)
