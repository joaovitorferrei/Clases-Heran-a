#Exercicio número 2 da lista letra b
from decimal import Decimal
class Pessoa:
    def __init__(self,nome:str,idade:int) -> None:
        if isinstance(idade,int):
            self.nome = nome
            self.idade = idade
    def display(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}")

class Rico(Pessoa):
    def __init__(self, nome:str,idade:int,dinheiro:Decimal) -> None:
        super().__init__(nome, idade)
        self.dinheiro = dinheiro
    def fazCompras(self):
        return f"Faz Compras:{self.dinheiro} nome {self.nome}"

class Pobre(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
    
    def trabalha(self):
        return f"Nome: {self.nome} não aguento mais trabalhar"
    
class Mendiga(Pessoa):
    def __init__(self,nome: str, idade: int) -> None:
        super().__init__(nome, idade)

    def mendiga(self):
        print(f"nome: {self.nome} min da dois reais")
