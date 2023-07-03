from .e_Pessoa import Pessoa
class Mendiga(Pessoa):
    def __init__(self,nome: str, idade: int) -> None:
        super().__init__(nome, idade)

    def mendiga(self):
        print(f"nome: {self.nome} min da dois reais")