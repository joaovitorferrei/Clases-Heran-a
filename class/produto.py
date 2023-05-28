# Crie uma classe chamada Produto com os atributos privados _nome e _preco. 
# Adicione métodos para definir e obter o nome e o preço do produto.
class Produto:
    def __init__(self,nome,preco = 0):
        if isinstance(nome, str) and isinstance(preco, float):
            self.__nome = nome
            self.__preco = preco
    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

n1 = input("Digite seu nome: ")
p1 = float(input("Digite o preco do produto: "))
pr1 = Produto(n1,p1) 
print(pr1.get_nome()) # pr1 significa Produto 1
print(f"Produto: {pr1.get_preco():.2f}")