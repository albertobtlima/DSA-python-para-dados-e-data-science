# Capítulo 6 - Pacotes e Módulos

# Importando um pacote Python
import numpy
import random
import statistics
import os
# Importando o módulo request do pacote urllib, usado para trazer url's
# para dentro do nosso ambiente Python
import urllib.request

# Importando apenas um dos métodos do pacote Numpy
from numpy import sqrt

# Verificando todos os métodos e atributos disponíveis no pacote
# print(dir(numpy))

# Usando um dos métodos do pacote Numpy
print(numpy.sqrt(25))

# Usando o método
print(sqrt(9))

# Help do método sqrt do pacote Numpy
print(help(sqrt))

print(random.choice(['Abacate', 'Banana', 'Laranja']))

print(random.sample(range(100), 10))

dados = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(dados))
print(statistics.median(dados))

print(os.getcwd())
print(dir(os))

print("-" * 50)

# Podemos trabalhar com módulos dos pacotes (quando disponíveis).

# Variável resposta armament o objeto de conexão à url passada como
# parâmetro
resposta = urllib.request.urlopen('http://python.org')
# Objeto resposta
print(resposta)
# Chamando o método read() do objeto resposta e armazenando o código
# html na variável html
html = resposta.read()
# Imprimindo html
print(html)
