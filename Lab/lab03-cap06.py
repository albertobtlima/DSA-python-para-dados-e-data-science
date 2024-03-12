# Lab 3 - Trabalhando com Expressões Regulares em Python com ChatGPT
# Expressões Regulares
# Expressões regulares são padrões usados para combinar ou encontrar ocorrências de sequências de caracteres em uma
# string. Em Python, expressões regulares são geralmente usadas para manipular strings e realizar tarefas como
# validação de entrada de dados, extração de informações de strings e substituição de texto.

import re

texto = "Meu e-mail é exemplo@gmail.com e você pode me contatar em outro_email@yahoo.com."
# Expressão regular para contar quantas vezes o caracter arroba aparece no texto
resultado = len(re.findall("@", texto))
print("O caractere '@' apareceu", resultado, "vezes no texto.")

# Expressão regular para extrair a palavra que aparece após a palavra "você" em um texto
# Nota: O r antes da string que representa a expressão regular em Python é usado para indicar que a string é uma
# string literal raw. Isso significa que as barras invertidas () não são interpretadas como caracteres de escape,
# mas são incluídas na expressão regular como parte do padrão.
resultado = re.findall(r'você (\w+)', texto)
print("A palavra após 'você' é:", resultado[0])

# Expressão regular para extrair endereços de e-mail de uma string
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', texto)
print(emails)

text = "O aluno estava incrivelmente perdido, mas encontrou a DSA e rapidamente começou a aprender."
# Extraindo os advérbios da frase
for m in re.finditer(r"\w+mente\b", text):
    print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))

print("-" * 50)

# REGEX com ChatGPT
# Música: Tempo Perdido
# Legião Urbana
# Variável do tipo string

musica = '''
Todos os dias quando acordo
Não tenho mais
O tempo que passou
Mas tenho muito tempo
Temos todo o tempo do mundo
Todos os dias
Antes de dormir
Lembro e esqueço
Como foi o dia
Sempre em frente
Não temos tempo a perder
Nosso suor sagrado
É bem mais belo
Que esse sangue amargo
E tão sério
E selvagem! Selvagem!
Selvagem!
Veja o sol
Dessa manhã tão cinza
A tempestade que chega
É da cor dos teus olhos
Castanhos
Então me abraça forte
E diz mais uma vez
Que já estamos
Distantes de tudo
Temos nosso próprio tempo
Temos nosso próprio tempo
Temos nosso próprio tempo
Não tenho medo do escuro
Mas deixe as luzes
Acesas agora
O que foi escondido
É o que se escondeu
E o que foi prometido
Ninguém prometeu
Nem foi tempo perdido
Somos tão jovens
Tão jovens! Tão jovens!
'''
print(musica)

# 1- Crie um REGEX para contar quantas vezes o caracter "a" aparece em todo o texto da música.
# 2- Crie um REGEX em Python para contar quantas vezes a palavra tempo aparece na música.
# 3- Crie um REGEX em Python para extrair as palavras seguidas por exclamação.
# 4- Crie um REGEX que extrai qualquer palavra cujo antecessor seja a palavra "esse" e o sucessor seja a palavra
#    "amargo" em um texto.
# 5- Crie um REGEX que retorne as palavras com acento, mas somente os caracteres na palavra que são anteriores ao
#    caracter com acento.


# 1 -> Usando a função findall() do módulo re para encontrar todas as ocorrências do caractere 'a'
ocorrencias = re.findall('a', musica)
# Contando o número de ocorrências
numero_ocorrencias = len(ocorrencias)
print("Número de vezes que 'a' aparece no texto:", numero_ocorrencias)
'''
Este código primeiro usa a função findall() do módulo re para encontrar todas as ocorrências do caractere "a" no texto. 
Em seguida, conta o número de ocorrências encontradas usando a função len().
'''
resultado1 = len(re.findall("a", musica))
print("O caractere 'a' apareceu", resultado1, "vezes na música.")

print("")
# -----------------------------------------------------------------------------------------------------------

# 2 -> Usando a função findall() do módulo re para encontrar todas as ocorrências da palavra 'tempo'
ocorrencias = re.findall(r'\btempo\b', musica)
# Contando o número de ocorrências
numero_ocorrencias = len(ocorrencias)
print("Número de vezes que 'tempo' aparece no texto:", numero_ocorrencias)
'''
Neste código, a expressão regular \btempo\b é usada para encontrar todas as ocorrências da palavra "tempo" como uma 
palavra inteira. O \b representa uma fronteira de palavra, garantindo que "tempo" seja considerado apenas quando 
é uma palavra completa, não parte de uma palavra maior. Em seguida, o código conta o número de ocorrências 
usando a função len().
'''
resultado2 = len(re.findall("tempo", musica))
print("A palavra 'tempo' apareceu", resultado2, "vezes na música.")

print("")
# -----------------------------------------------------------------------------------------------------------

# 3 -> Usando a função findall() do módulo re para encontrar todas as palavras seguidas por uma exclamação
palavras_exclamacao = re.findall(r'\b\w+!\b', musica)
print("Palavras seguidas por exclamação:", palavras_exclamacao)

# Neste código, a expressão regular \b\w+!\b é usada para encontrar palavras seguidas por um ponto de exclamação.
# Explicação da expressão regular:
# \b: Representa uma fronteira de palavra para garantir que a palavra comece após um limite de palavra.
# \w+: Corresponde a uma ou mais letras, números ou underscores (caracteres de palavra).
# !: Corresponde a um ponto de exclamação.
# \b: Outra fronteira de palavra para garantir que a palavra termine antes de um limite de palavra.
# Essa expressão regular vai encontrar palavras completas seguidas por um ponto de exclamação no texto.

resultado3 = re.findall(r'\b\w+!', musica)
print("Estas são as palavras seguidas por exclamação:", resultado3)

print("")
# -----------------------------------------------------------------------------------------------------------

# 4 -> Usando a função findall() do módulo re para encontrar todas as palavras que têm "esse" como antecessor e
#      "amargo" como sucessor
palavras = re.findall(r'\besse\s+(\w+)\s+amargo\b', musica)
print("Palavras que têm 'esse' como antecessor e 'amargo' como sucessor:", palavras)

# Neste código, a expressão regular \besse\s+(\w+)\s+amargo\b é usada para encontrar as palavras que têm "esse"
# como antecessor e "amargo" como sucessor. Explicação da expressão regular:

# \b: Representa uma fronteira de palavra para garantir que a palavra comece após um limite de palavra.
# esse: Corresponde exatamente à palavra "esse".
# \s+: Corresponde a um ou mais caracteres de espaço em branco.
# (\w+): Corresponde a uma palavra (uma sequência de caracteres alfanuméricos) e a captura usando parênteses.
# \s+: Corresponde a um ou mais caracteres de espaço em branco.
# amargo: Corresponde exatamente à palavra "amargo".
# \b: Outra fronteira de palavra para garantir que a palavra termine antes de um limite de palavra.
# Essa expressão regular vai extrair as palavras que têm "esse" como antecessor e "amargo" como sucessor no texto.

resultado4 = re.findall(r'\besse\s(\w+)\samargo\b', musica)
print("Palavra(s) encontrada(s):", resultado4)

print("")
# -----------------------------------------------------------------------------------------------------------

# 5 -> Usando a função findall() do módulo re para encontrar as palavras com acento e retornar apenas os caracteres
#      anteriores ao acento
palavras_acentuadas = re.findall(r'\b\w+(?=[áéíóúâêîôûàèìòùäëïöü])', musica)
print("Palavras com acento e caracteres anteriores:", palavras_acentuadas)

# Explicação da expressão regular:

# \b: Representa uma fronteira de palavra para garantir que a palavra comece após um limite de palavra.
# \w+: Corresponde a uma ou mais letras, números ou underscores (caracteres de palavra).
# (?=...): É um lookahead positivo que faz com que a correspondência seja bem-sucedida apenas se seguida pelo padrão dentro dos parênteses, mas não inclui esse padrão na correspondência.
# [áéíóúâêîôûàèìòùäëïöü]: Corresponde a qualquer caractere acentuado. Esta parte do padrão é apenas para identificar a presença de acento.
# O resultado dessa expressão regular serão as palavras com acento, retornando somente os caracteres que estão antes do acento em cada palavra acentuada.

resultado5 = re.findall(r'\b[\wÀ-ÿ]+[áéíóúãõç]', musica)
print("As palavras acentuadas são:", resultado5)
