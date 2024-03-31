# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 1

import random                    # Import
from os import system, name


# Função para limpar a tela a cada execução
def limpa_tela():
    if name == 'nt':         # windows
        _ = system('cls')
    else:                    # Mac ou Linux
        _ = system('clear')


def game():
    limpa_tela()

    print("\nBem vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo\n")

    # Lista de palavras para o jogo
    palavras = ['BANANA', 'ABACATE', 'UVA', 'MORANGO', 'LARANJA']

    # Escolhe randomicamente uma palavra
    palavra = random.choice(palavras)

    # List comprehension
    letras_descobertas = ['_' for letra in palavra]

    # Número de chances
    chances = 6

    # Lista para as letras erradas
    letras_erradas = []

    # Loop enquanto número de chances for maior do que zero
    while chances > 0:
        print(" ".join(letras_descobertas))
        print("\nChances restantes: ", chances)
        print("Letras erradas: ", " ".join(letras_erradas))

        # Tentativas
        tentativa = input("\nDigite uma letra: ").upper()

        # Condicional
        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        # Condicional
        if "-" not in letras_descobertas:
            print("\nVocê venceu! A palavra era: ", palavra)
            break

    # Condicional
    if "-" in letras_descobertas:
        print("\nVocê perdeu... A palavra era: ", palavra)

'''
# Bloco main
if __name__ = "__main__":
    game()
    print("\nParabéns")
'''
game()
