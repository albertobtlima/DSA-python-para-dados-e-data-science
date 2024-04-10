# Criando a classe
class Algoritmo:

    def __init__(self, tipo_algo):
        self.tipo = tipo_algo
        print("Construtor chamado para criar um objeto desta classe.")


# Criando um objeto a partir da classe
algo1 = Algoritmo(tipo_algo='Random Forest')

# Criando um objeto a partir da classe
algo2 = Algoritmo(tipo_algo='Deep Learning')

# Atributo da classe
print(algo1.tipo)

# Atributo da classe
print(algo2.tipo)
