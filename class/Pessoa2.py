# Crie uma classe chamada Pessoa que tenha os atributos nome, idade e altura. Crie um 
# método falar que imprime uma mensagem dizendo "Olá, meu nome é [nome], eu tenho
# [idade] anos e minha altura é [altura] metros".
class Pessoa:
    def __init__(self,nome,idade,altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
    def falar(self):
        print(
            f"Olá, meu nome é {self.nome}, eu tenho {self.idade} anos e minha altura é {self.altura} metros"
            )
p1 = Pessoa("joao",18,1.83)
p1.falar()