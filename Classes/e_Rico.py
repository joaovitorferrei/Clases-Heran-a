from .e_Pessoa import Pessoa,Decimal

class Rico(Pessoa):
    def __init__(self, nome:str,idade:int,dinheiro:Decimal) -> None:
        super().__init__(nome, idade)
        self.dinheiro = dinheiro
    def fazCompras(self):
        return f"Faz Compras:{self.dinheiro} nome {self.nome}"

