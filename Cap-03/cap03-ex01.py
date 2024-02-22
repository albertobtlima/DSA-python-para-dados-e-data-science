"""
Pseudocódigo 1 - Calcular a Área de Um Paralelograma
Nota: Um paralelogramo é um quadrilátero com lados opostos paralelos (e portanto ângulos opostos iguais).
Um quadrilátero com lados iguais é chamado de losango e um paralelogramo cujos ângulos são todos ângulos retos
é chamado de retângulo.

    Inicie
    Exiba "Bem-vindo ao Calculador de Área de Paralelogramo"
    Peça para o usuário inserir o comprimento da base
    Armazene o comprimento da base em uma variável
    Peça para o usuário inserir a altura
    Armazene a altura em uma variável
    Calcule a área do paralelogramo:  base * altura
    Armazene o resultado em uma variável
    Exiba o resultado
    Fim
"""

print("Bem-vindo ao Calculador de Área de Paralelogramo")
base = float(input("Insira o comprimento da base: "))
altura = float(input("Insira a altura: "))
area = base * altura
print("A área do paralelogramo é: ", area)
