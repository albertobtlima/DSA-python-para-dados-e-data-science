# Capítulo 4 - Estruturas de Dados (Tuplas)
# Trabalhando com Tuplas

tupla1 = ("Geografia", 23, "Elefantes", 9.8, 'Python')    # Criando uma tupla
print(tupla1)                                             # Imprimindo a tupla

# tupla1.append("Chocolate") -> Ira dar erro. Tuplas não suportam append()
# del tupla1["Elefantes"]    -> Ira dar erro. Tuplas não suportam delete de um item específico

tupla1 = ("Chocolate")  # Tuplas podem ter um único item
print(tupla1)
tupla1 = ("Geografia", 23, "Elefantes", 9.8, 'Python')
print(tupla1[0])
print(len(tupla1))       # Verificando o comprimento da tupla
print(tupla1[1:])        # Slicing, da mesma forma que se faz com listas
print(tupla1.index('Elefantes'))

# tupla1[1] = 21  -> Ira dar erro. Tuplas não suportam atribuição de item
del tupla1   # Deletando a tupla

print('\n')

t2 = ('A', 'B', 'C')
print(t2)

# t2[0] = 'D' -> Ira dar erro. Tuplas não suportam atribuição de item

print('\n')

lista_t2 = list(t2)      # Usando a função list() para converter uma tupla para lista
print(type(t2))
print(type(lista_t2))
print(lista_t2)
lista_t2.append('D')
t2 = tuple(lista_t2)     # Usando a função tuple() para converter uma lista para tupla
print(t2)
