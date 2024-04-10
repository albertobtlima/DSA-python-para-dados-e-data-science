# Criando uma classe chamada Livro
class Livro:

    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        print("Construtor chamado para criar um objeto desta classe.")

    def imprime(self, titulo, isbn):
        print("Foi criado o livro %s com ISBN %d" % (self.titulo, self.isbn))


# Criando o objeto Livro2 que é uma instância da classe Livro
Livro2 = Livro("O Poder do Hábito", 77886611)

print(Livro2.titulo)

# Método do objeto Livro2
print(Livro2.imprime())
