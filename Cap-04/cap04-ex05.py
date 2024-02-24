# Capítulo 4 - Estruturas de Dados (Dicionários)

# Trabalhando com Dicionários

estudantes_lst = ["Pedro", 24, "Ana", 22, "Ronaldo", 26, "Janaina", 25]         # Isso é uma lista
print(estudantes_lst)
print(type(estudantes_lst))

print('\n')

estudantes_dict = {"Pedro": 24, "Ana": 22, "Ronaldo": 26, "Janaina": 25}        # Isso é um dicionário
print(estudantes_dict)
print(type(estudantes_dict))
print(estudantes_dict["Pedro"])
estudantes_dict["Marcelo"] = 23
print(estudantes_dict["Marcelo"])
print(estudantes_dict)
estudantes_dict.clear()
print(estudantes_dict)
del estudantes_dict
# print(estudantes_dict)  ->  Ira dar erro, o dicionário não existe mais

print('\n')

estudantes = {"Pedro": 24, "Ana": 22, "Ronaldo": 26, "Janaina": 25}
print(estudantes)
print(len(estudantes))
print(estudantes.keys())
print(estudantes.values())
print(estudantes.items())

print('\n')

estudantes2 = {"Camila": 27, "Adriana": 28, "Roberta": 26}
print(estudantes2)
estudantes.update(estudantes2)
print(estudantes)

print('\n')

dic1 = {}
print(dic1)
dic1["chave_um"] = 2
print(dic1)
dic1[10] = 5
print(dic1)
dic1[9.13] = "Python"
print(dic1)
dic1["teste"] = 5
print(dic1)

print('\n')

dict1 = {}
dict1["teste"] = 10
dict1["key"] = "teste"
print(dict1)                 # Atenção, pois chave e valor podem ser iguais, mas representam coisas diferentes.

print('\n')

dict2 = {}
dict2["key1"] = "Data Science"
dict2["key2"] = 10
dict2["key3"] = 100
print(dict2)

a = dict2["key1"]
b = dict2["key2"]
c = dict2["key3"]
print(a, b, c)

print('\n')

# Dicionário de listas
dict3 = {'chave1': 1230, 'chave2': [22, 453, 73.4], 'chave3': ['picanha', 'fraldinha', 'alcatra']}
print(dict3)
print(dict3['chave2'])
print(dict3['chave3'][0].upper())  # Acessando um item da lista, dentro do dicionário e colocando em maiúsculo
var1 = dict3['chave2'][0] - 2
print(var1)
dict3['chave2'][0] -= 2   # Duas operações no mesmo comando, para atualizar um item dentro da lista
print(dict3)

print("-=" * 15)   # ------------------------------------------------------------

# Criando Dicionários Aninhados

dict_aninhado = {'key1': {'key2_aninhada': {'key3_aninhada': 'Dict aninhado em Python'}}}
print(dict_aninhado)
print(dict_aninhado['key1'])
print(dict_aninhado['key1']['key2_aninhada'])
print(dict_aninhado['key1']['key2_aninhada']['key3_aninhada'])
