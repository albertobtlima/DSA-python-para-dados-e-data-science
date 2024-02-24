# Capítulo 4 - Estruturas de Dados (Listas)

# Trabalhando com Listas

lista_1 = ["arroz, frango, tomate, leite"]          # Criando uma lista
print(type(lista_1))
print(lista_1)

lista_2 = ["arroz", "frango", "tomate", "leite"]    # Criando outra lista
print(type(lista_2))
print(lista_2)


lista_3 = [23, 100, "Cientista de Dados"]           # Criando lista
print(type(lista_3))
print(lista_3)

# Atribuindo cada valor da lista a uma variável.
item1 = lista_3[0]
item2 = lista_3[1]
item3 = lista_3[2]
print(item1, item2, item3)                         # Imprimindo as variáveis

print("-=" * 15)   # ------------------------------------------------------------

# Atualizando Um Item da Lista

print(lista_2[2])
lista_2[2] = "chocolate"                           # Atualizando um item da lista
print(lista_2)

print("-=" * 15)   # ------------------------------------------------------------

# Deletando Um Item da Lista

# Não é possível deletar um item que não existe na lista. Vai gerar erro index out of range
# del lista_2[4]

del lista_2[3]                                    # Deletando um item específico da lista
print(lista_2)

print("-=" * 15)   # ------------------------------------------------------------

# Listas de Listas (Listas Aninhadas)
# Listas de listas são matrizes em Python.

listas = [[1, 2, 3], [10, 15, 14], [10.1, 8.7, 2.3]]       # Criando uma lista de listas
print(listas)                                              # Imprimindo a lista

a = listas[0]
print(a)

b = a[0]
print(b)

list1 = listas[1]
print(list1)

valor_1_0 = list1[0]
print(valor_1_0)

valor_1_2 = list1[2]
print(valor_1_2)

list2 = listas[2]
print(list2)

valor_2_0 = list2[0]
print(valor_2_0)

print("-=" * 15)   # ------------------------------------------------------------

# Operações com Listas

listas = [[1, 2, 3], [10, 15, 14], [10.1, 8.7, 2.3]]     # Criando uma lista aninhada (lista de listas)
print(listas)
print(listas[0][2])

a = listas[0][0]                                         # Atribuindo à variável a o primeiro valor da primeira lista
print(a)

b = listas[1][2]
print(b)

c = listas[0][2] + 10
print(c)

d = 10
e = d * listas[2][0]
print(e)

print("-=" * 15)   # ------------------------------------------------------------

# Concatenando Listas

lista_s1 = [34, 32, 56]
lista_s2 = [21, 90, 51]
print(lista_s1, lista_s2)

lista_total = lista_s1 + lista_s2
print(lista_total)

print("-=" * 15)   # ------------------------------------------------------------

# Operador in

lista_teste_op = [100, 2, -5, 3.4]        # Criando uma lista
print(10 in lista_teste_op)               # Verificando se o valor 10 pertence a lista
print(100 in lista_teste_op)              # Verificando se o valor 100 pertence a lista

print("-=" * 15)   # ------------------------------------------------------------

# Funções Built-in

lista_numeros = [10, 20, 50, -3.4]       # Criando uma lista
print(len(lista_numeros))                # Função len() retorna o comprimento da lista
print(max(lista_numeros))                # Função max() retorna o valor máximo da lista
print(min(lista_numeros))                # Função min() retorna o valor mínimo da lista

lista_formacoes_dsa = ["Analista de Dados", "Cientista de Dados", "Engenheiro de Dados"]       # Criando uma lista
print(lista_formacoes_dsa)
lista_formacoes_dsa.append("Engenheiro de IA")       # Adicionando um item à lista
print(lista_formacoes_dsa)
lista_formacoes_dsa.append("Engenheiro de IA")
print(lista_formacoes_dsa.count("Engenheiro de IA"))

print('\n')

a = []        # Criando uma lista vazia
print(a)
print(type(a))
a.append(10)
print(a)
a.append(50)
print(a)

old_list = [1, 2, 5, 10]
new_list = []
for item in old_list:              # Copiando os itens de uma lista para outra
    new_list.append(item)
print(new_list)

print('\n')

cidades = ['Recife', 'Manaus', 'Salvador']
cidades.extend(['Fortaleza', 'Palmas'])
print(cidades)
print(cidades.index('Salvador'))

cidades.insert(2, 110)
print(cidades)
cidades.remove(110)       # Remove um item da lista
print(cidades)
cidades.reverse()         # Reverte a lista
print(cidades)

print('\n')

x = [3, 4, 2, 1]
print(x)
x.sort()                 # Ordena a lista
print(x)
