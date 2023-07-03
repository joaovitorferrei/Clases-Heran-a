from .e_Pessoa import Pessoa
class Pobre(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
    
    def trabalha(self):
        return f"Nome: {self.nome} não aguento mais trabalhar"
    
