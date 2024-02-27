def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print('***** Calculadora em Python *****\n')
print('Selecione o número da operação desejada:\n')

print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão\n')

operacao = input('Digite sua opção (1/2/3/4): ')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
print('')

if operacao == '1':
    print(num1, '+', num2, '=', add(num1, num2))
elif operacao == '2':
    print(num1, '-', num2, '=', subtract(num1, num2))
elif operacao == '3':
    print(num1, '*', num2, '=', multiply(num1, num2))
elif operacao == '4':
    print(num1, '/', num2, '=', divide(num1, num2))
else:
    print('Operação invalida')
