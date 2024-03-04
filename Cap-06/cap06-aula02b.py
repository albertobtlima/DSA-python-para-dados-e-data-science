# Manipulando Arquivos JSON (Java Script Object Notation)

# Importando os módulos
import json
from urllib.request import urlopen

# Criando um dicionário

dict_guido = {
    'nome': 'Guido van Rossum',
    'linguagem': 'Python',
    'similar': ['c', 'Modula-3', 'lisp'],
    'users': 1000000
}

for k, v in dict_guido.items():
    print(k, v)

print("")
# Convertendo o dicionário para um objeto json
json.dumps(dict_guido)
print(dict_guido)

print("")
# Criando um arquivo Json
with open('arquivos/dados.json', 'w') as arquivo:
    arquivo.write(json.dumps(dict_guido))

# Leitura de arquivos Json
with open('arquivos/dados.json', 'r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)
print(dados)
print(dados['nome'])

print('-' * 50)
# Extração de Arquivo da Web

# Imprimindo um arquivo JSON copiado da internet
response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
dados = json.loads(response)[0]
print(dados, '\n')

print('Título: ', dados['title'])
print('URL: ', dados['url'])
print('Duração: ', dados['duration'])
print('Número de Visualizações: ', dados['stats_number_of_plays'])

print('-' * 50)
# Copiando o conteúdo de um arquivo para outro.
arquivo_fonte = 'arquivos/dados.json'
arquivo_destino = 'arquivos/dados.txt'

# Método 1
'''
with open(arquivo_fonte, 'r') as infile:
    text = infile.read()
    with open(arquivo_destino, 'w') as outfile:
        outfile.write(text)
'''

# Método 2
open(arquivo_destino, 'w').write(open(arquivo_fonte, 'r').read())

# Leitura do arquivo txt
with open('arquivos/dados.txt', 'r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)
print(dados)
