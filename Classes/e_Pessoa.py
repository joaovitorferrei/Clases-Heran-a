#Exercicio número 2 da lista letra b
from decimal import Decimal
class Pessoa:
    def __init__(self,nome:str,idade:int) -> None:
        if isinstance(idade,int):
            self.nome = nome
            self.idade = idade
    def display(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}")


