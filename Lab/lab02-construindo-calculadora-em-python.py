print('***** Calculadora em Python *****\n')

print('Selecione o número da operação desejada:\n')

print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão\n')

operacao = input('Digite sua opção (1/2/3/4): ')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
resultado = 0
sinal = ''

if operacao == '1':
    sinal = '+'
    resultado = num1 + num2
elif operacao == '2':
    sinal = '-'
    resultado = num1 - num2
elif operacao == '3':
    sinal = '*'
    resultado = num1 * num2
elif operacao == '4':
    sinal = '/'
    resultado = num1 / num2
else:
    print('Operação invalida')

print('')
print(f'{num1} {sinal} {num2} = {resultado}')
