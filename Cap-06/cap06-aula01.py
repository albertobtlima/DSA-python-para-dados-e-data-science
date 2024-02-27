# Capítulo 6 - Manipulação de Arquivos - Parte 1

# Lendo Arquivos

# Abrindo o arquivo para leitura
arq1 = open("arquivos/arquivo1.txt", "r")            # r = read
print(type(arq1))

# Lendo o arquivo
print(arq1.read())

# Contar o número de caracteres
print(arq1.tell())

# Lendo o arquivo
print(arq1.read())

# Retornar para o iníco do arquivo
print(arq1.seek(0, 0))

# Lendo os primeiros 23 caracteres
print(arq1.read(23))

# Lendo o arquivo
print(arq1.read())

print('-' * 40)  # -----------------------------------------------------
# Gravando Arquivos

# Abrindo arquivo para gravação
arq2 = open("arquivos/arquivo2.txt", "w")              # w = write

# Gravando arquivo
arq2.write('Aprendendo a programar em Python.')
arq2.close()

# Lendo arquivo gravado
arq2 = open("arquivos/arquivo2.txt", "r")
print(arq2.read())

# Acrescentando conteúdo
arq2 = open("arquivos/arquivo2.txt", "a")              # a = append
arq2.write(" E a metodologia de ensino da Data Science Academy facilita o aprendizado.")
arq2.close()
arq2 = open("arquivos/arquivo2.txt", "r")
print(arq2.read())

# Retornando ao início do arquivo para leitura
arq2.seek(0, 0)
print(arq2.read())
