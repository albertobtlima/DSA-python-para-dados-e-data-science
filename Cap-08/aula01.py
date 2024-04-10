'''
Classes
Em Programação Orientada a Objetos (POO), uma classe é uma estrutura que descreve um objeto, especificando os atributos
e comportamentos que o objeto deve ter. Uma classe é uma espécie de modelo que define as características e ações que um
objeto deve possuir.

As classes são usadas para criar objetos, que são instâncias da classe. Cada objeto criado a partir da mesma classe
terá os mesmos atributos e comportamentos.

Para criar uma classe em Python, utiliza-se a palavra reservada class.

O nome da classe segue a mesma convenção de nomes para criação de funções e variáveis em Python, mas normalmente se usa
a primeira letra maiúscula em cada palavra no nome da classe.
'''


# Criando uma classe chamada Livro
class Livro:
    # Este método vai inicializar cada objeto criado a partir desta classe
    # O nome deste método é __init__
    # (self) é uma referência a cada atributo da própria classe (e não de uma classe mãe, por exemplo)
    def __init__(self):
        # Atributos são propriedades
        self.titulo = 'Sapiens - Uma Breve História da Humanidade'
        self.isbn = 9988888
        print("Construtor chamado para criar um objeto desta classe.")

    # Métodos são funções que executam ações nos objetos da classe
    def imprime(self):
        print("Foi criado o livro %s com ISBN %d" % (self.titulo, self.isbn))


# Em Python, a palavra reservada self é uma referência ao objeto atual da classe. Quando um objeto é criado a partir de
# uma classe, self é utilizado para se referir a esse objeto específico.

# Criando uma instância da classe Livro
Livro1 = Livro()

# O objeto Livro1 é do tipo Livro
print(type(Livro1))

# Atributo do objeto Livro1
print(Livro1.titulo)

# Método do objeto Livro1
print(Livro1.imprime())
