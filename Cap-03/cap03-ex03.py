"""
    Pseudocódigo 3 - Algoritmo Bubble Sort
    Bubble Sort é um algoritmo de ordenação simples que funciona comparando cada elemento com o próximo,
    e trocando-os de lugar se eles estiverem em ordem incorreta. O algoritmo repete esse processo várias vezes,
    até que todos os elementos estejam ordenados. A cada passagem, o maior elemento "flutua" para o final do array,
    como uma bolha, dando origem ao nome do algoritmo.

    Inicie

    Para cada elemento i no array de tamanho n
        Para cada elemento j no array de tamanho n - 1
            Se elemento i for maior que elemento j
                Troque os elementos i e j
    Exiba o array ordenado
    Fim
"""

lista = [6, 7, 8, 3, 10, 19, 4, 1, 0, 61, 30, 16, 17, 82, 29, 34, 43, 21, 11, 39, 56, 67, 12]


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):                                   # Para cada elemento i do array
        for j in range(0, n - i - 1):                    # Para cada elemento j do array
            if arr[j] > arr[j+1]:                        # Se elemento i for maior que elemento J
                arr[j], arr[j+1] = arr[j+1], arr[j]      # Troque os elementos i e j
    return arr


print(bubble_sort(lista))

lista2 = [45, 8, 90, 1, 7, 21, 12, 4, 6, 9, 11, 16, 30]

print(bubble_sort(lista2))
