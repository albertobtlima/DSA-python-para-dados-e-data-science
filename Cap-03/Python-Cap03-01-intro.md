Data Science Academy
Fundamentos de Linguagem Python Para Análise de Dados e Data Science
Capítulo 3 - Introdução à Lógica de Programação
[1]
# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())
Versão da Linguagem Python Usada Neste Jupyter Notebook: 3.9.13

Pressione as teclas shift e enter para executar o código em uma célula ou pressione o botão Run no menu superior.
Pseudocódigo 1 - Calcular a Área de Um Paralelograma
Nota: Um paralelogramo é um quadrilátero com lados opostos paralelos (e portanto ângulos opostos iguais). 
Um quadrilátero com lados iguais é chamado de losango e um paralelogramo cujos ângulos são todos ângulos retos é chamado de retângulo.

**Inicie**

    Exiba "Bem-vindo ao Calculador de Área de Paralelogramo"
    Peça para o usuário inserir o comprimento da base
    Armazene o comprimento da base em uma variável
    Peça para o usuário inserir a altura
    Armazene a altura em uma variável
    Calcule a área do paralelogramo:  base * altura
    Armazene o resultado em uma variável
    Exiba o resultado
**Fim**

## Convertendo o Pseudocódigo 1 em Programa Python

````
print("Bem-vindo ao Calculador de Área de Paralelogramo")
Bem-vindo ao Calculador de Área de Paralelogramo

base = float(input("Insira o comprimento da base: "))
Insira o comprimento da base: 4

altura = float(input("Insira a altura: "))
Insira a altura: 7

area = base * altura
print("A área do paralelogramo é: ", area)
A área do paralelogramo é:  28.0
````

## Pseudocódigo 2 - Calculadora Simples

**Inicie**

    Exiba "Bem-vindo à Calculadora"
    Peça para o usuário inserir o primeiro número
    Armazene o primeiro número em uma variável
    Peça para o usuário inserir o segundo número
    Armazene o segundo número em uma variável
    Peça para o usuário selecionar uma operação (+, -, *, /)
    Armazene a operação em uma variável
    Utilize a operação selecionada e os números armazenados para realizar o cálculo
    Exiba o resultado
**Fim**

## Convertendo o Pseudocódigo 2 em Programa Python

````
print("Bem-vindo à Calculadora")
Bem-vindo à Calculadora

num1 = float(input("Insira o primeiro número: "))
Insira o primeiro número: 3

num2 = float(input("Insira o segundo número: "))
Insira o segundo número: 4

operacao = input("Selecione uma operação (+, -, *, /): ")
Selecione uma operação (+, -, *, /): *

if operacao == "+":

    resultado = num1 + num2
    print("O resultado é: ", resultado)

elif operacao == "-":
    resultado = num1 - num2
    print("O resultado é: ", resultado)
    
elif operacao == "*":
    resultado = num1 * num2
    print("O resultado é: ", resultado)
        
elif operacao == "/":
    resultado = num1 / num2
    print("O resultado é: ", resultado)
    
else:
    print("Operação inválida.")
````
O resultado é:  12.0

## Pseudocódigo 3 - Algoritmo Bubble Sort
Bubble Sort é um algoritmo de ordenação simples que funciona comparando cada elemento com o próximo, e trocando-os de lugar 
se eles estiverem em ordem incorreta. O algoritmo repete esse processo várias vezes, até que todos os elementos estejam ordenados. 
A cada passagem, o maior elemento "flutua" para o final do array, como uma bolha, dando origem ao nome do algoritmo.

**Inicie**

    Para cada elemento i no array de tamanho n
        Para cada elemento j no array de tamanho n - 1
            Se elemento i for maior que elemento j
                Troque os elementos i e j
    Exiba o array ordenado
**Fim**

````
# Considere esta lista como exemplo para ordenação com o Bubble sort
lista = [6, 3, 12, 7]

# Primeira passada do algoritmo (troca os elementos 6 e 3 de lugar)
lista = [3, 6, 12, 7]

# Segunda passada do algoritmo (não tem troca entre 6 e 12)
lista = [3, 6, 12, 7]

# Terceira passada do algoritmo (troca os elementos 12 e7 de lugar)
lista = [3, 6, 7, 12]
Convertendo o Pseudocódigo 3 em Programa Python

lista = [6,7,8,3,10,19,4,1,0,61,30,16,17,82,29,34,43,21,11,39,56,67,12]

def bubble_sort(arr):
    
    n = len(arr)
    
    # Para cada elemento i do array
    for i in range(n):
    
        # Para cada elemento j do array
        for j in range(0, n-i-1):
        
            # Se elemento i for maior que elemento j
            if arr[j] > arr[j+1]:
            
                # Troque os elementos i e j
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

print(bubble_sort(lista))
[0, 1, 3, 4, 6, 7, 8, 10, 11, 12, 16, 17, 19, 21, 29, 30, 34, 39, 43, 56, 61, 67, 82]

Parece mágica! Mas não é. É a beleza da programação de computadores!

lista2 = [60,17,28,3,10,19,4,1,0,61,30,16,17,82,29,34,43,21,11,39,56,67,12]

print(bubble_sort(lista2))
[0, 1, 3, 4, 10, 11, 12, 16, 17, 17, 19, 21, 28, 29, 30, 34, 39, 43, 56, 60, 61, 67, 82]
````
Fim
