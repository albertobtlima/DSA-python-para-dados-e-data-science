# Capítulo 5 - Funções

print('Hello World')


def primeiraFunc():                 # Definindo uma função
    nome = 'Bob'
    print('Hello %s' % nome)


primeiraFunc()

print('-' * 30)  # ----------------------------------------------------------
# Definindo uma função com parâmetro


def segundaFunc(nome):
    print('Hello %s' % nome)


segundaFunc('Aluno')

print('-' * 30)  # ----------------------------------------------------------
# Função para imprimir números


def imprimeNumeros():
    # Loop
    for i in range(0, 5):
        print("Número " + str(i))


imprimeNumeros()

print('-' * 30)  # ----------------------------------------------------------
# Função para somar números


def addNum(firstnum, secondnum):
    print("Primeiro número: " + str(firstnum))
    print("Segundo número: " + str(secondnum))
    print("Soma: ", firstnum + secondnum)


addNum(4, 7)               # Chamando a função e passando parâmetros
addNum(45, 3)              # Chamando a função e passando parâmetros

print('-' * 30)  # ----------------------------------------------------------
# Funções com número variável de argumentos


def printVarInfo(arg1, *vartuple):
    print("O parâmetro passado foi: ", arg1)         # Imprimindo o valor do primeiro argumento

    for item in vartuple:                            # Imprimindo o valor do segundo argumento
        print("O parâmetro passado foi: ", item)
    return


printVarInfo(10)                                     # Fazendo chamada à função usando apenas 1 argumento
printVarInfo('Chocolate', 'Morango')
printVarInfo('Data', 'Science', 'Academy')

print('-' * 30)  # ----------------------------------------------------------
# Escopo de Variável - Local e Global

var_global = 10      # Esta é uma variável global


def multiplica_numeros(num1, num2):            # Função
    var_global = num1 * num2                   # Esta é uma variável local
    print(var_global)


multiplica_numeros(5, 25)
print(var_global)

print('-' * 30)  # ----------------------------------------------------------
# Funções Built-in

print(abs(-56))
print(abs(23))
print(bool(0))
print(bool(1))
print(int(4.3))
print(str(13))
print(float(5))

# Usando a função int para converter o valor digitado
idade = int(input("Digite sua idade: "))
if idade > 13:
    print("Você pode acessar Redes Sociais sem supervisão!")
else:
    print("Seus pais não deveriam você acessar Redes Sociais sem supervisão!")

print(int("26"))
print(float("123.345"))
print(str(14))
print(len([23, 34, 45, 46]))

array = [1, 2, 3]
print(max(array))
print(min(array))

list1 = [16, 23, 44, 75]
print(sum(list1))
