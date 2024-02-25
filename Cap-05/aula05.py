# Capítulo 5 - Métodos

"""
Métodos
Tudo em Python é objeto. E cada objeto tem métodos e atributos.

Atributos são propriedades, características do objeto.
Métodos são funções com ações que podem ser executadas nos objetos.
"""

lista = [100, -2, 12, 65, 0]      # Criando uma lista
print(type(lista))
print(lista)                      # Verificando métodos e atributos

lista.append(100)                 # Usando um método do objeto lista
print(lista)

print(lista.count(100))           # Usando um método do objeto lista

help(lista.count)                 # A função help() explica como utilizar cada método de um objeto

print(dir(lista))                 # A função dir() mostra todos os métodos e atributos de um objeto

print('-' * 30)  # -------------------------------------------------------------------------------------------------

frase = 'Isso é uma string'
print(type(frase))
print(frase)                      # Verificando métodos e atributos

print(frase.split())             # O método de um objeto pode ser chamado dentro de uma função, como print()
