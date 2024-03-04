# Manipulando Arquivos TXT

# Importando os módulos
import os
import csv

texto = "Cientista de Dados pode ser uma excelente alternativa de carreira.\n"
texto = texto + "Esses profissionais precisam saber como programar em Python.\n"
texto += "E, claro, devem ser proficientes em Data Science."

print(texto)

# Criando um arquivo
arquivo = open(os.path.join('arquivos/cientista.txt'), 'w')

# Gravando os dados no arquivo
for palavra in texto.split():
    arquivo.write(palavra + ' ')

# Fechando o arquivo
arquivo.close()

print("")

# Lendo o arquivo
arquivo = open('arquivos/cientista.txt', 'r')
conteudo = arquivo.read()
arquivo.close()
print(conteudo)

print('-' * 50)  # -----------------------------------------
# Usando a Expressão with
# O método close() é executado automaticamente.

with open('arquivos/cientista.txt', 'r') as arquivo:
    conteudo = arquivo.read()
print(len(conteudo))
print(conteudo)

print("")

with open('arquivos/cientista.txt', 'w') as arquivo:
    arquivo.write(texto[:19])
    arquivo.write('\n')
    arquivo.write(texto[28:66])

arquivo = open('arquivos/cientista.txt', 'r')
conteudo = arquivo.read()
arquivo.close()
print(conteudo)

print('-' * 50)  # -----------------------------------------
# Manipulando Arquivos CSV

with open('arquivos/numeros.csv', 'w') as arquivo:
    # Cria o objeto de gravação
    writer = csv.writer(arquivo)

    # Grava no arquivo linha a linha
    writer.writerow(('nota1', 'nota2', 'nota3'))
    writer.writerow((63, 87, 92))
    writer.writerow((61, 79, 76))
    writer.writerow((72, 64, 91))

# Leitura de arquivos csv
with open('arquivos/numeros.csv', 'r', encoding='utf8', newline='\r\n') as arquivo:
    # Cria o objeto de leitura
    leitor = csv.reader(arquivo)
    # Loop
    for x in leitor:
        print(x)

print("")
# Gerando uma lista com dados do arquivo csv
with open('arquivos/numeros.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)
print(dados)

print("")
# Imprimindo a partir da segunda linha
for linha in dados[1:]:
    print(linha)
