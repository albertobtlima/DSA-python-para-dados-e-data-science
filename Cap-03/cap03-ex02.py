"""
Pseudocódigo 2 - Calculadora Simples

    Inicie
    Exiba "Bem-vindo à Calculadora"
    Peça para o usuário inserir o primeiro número
    Armazene o primeiro número em uma variável
    Peça para o usuário inserir o segundo número
    Armazene o segundo número em uma variável
    Peça para o usuário selecionar uma operação (+, -, *, /)
    Armazene a operação em uma variável
    Utilize a operação selecionada e os números armazenados para realizar o cálculo
    Exiba o resultado
    Fim
"""

print("Bem-vindo à Calculadora")
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = str(input("Selecione uma operação: (+, -, *, /): "))

print("")

if operacao == "+":
    resultado = numero1 + numero2
    print(f"A soma entre {numero1} e {numero2} é: {resultado}")
elif operacao == "-":
    resultado = numero1 - numero2
    print(f"A subtração entre {numero1} e {numero2} é: {resultado}")
elif operacao == "*":
    resultado = numero1 * numero2
    print(f"A multiplicação entre {numero1} e {numero2} é: {resultado}")
else:
    resultado = numero1 / numero2
    print(f"A divisão entre {numero1} e {numero2} é: {resultado}")
