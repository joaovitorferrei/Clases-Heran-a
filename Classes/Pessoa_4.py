#Exercicio número 2 da lista letra b
class Pessoa:
    def __init__(self,Nome:str,idade:int) -> None:
        if isinstance(idade,int):
            self.Nome = Nome
            self.idade = idade
class Rico(Pessoa):
    def __init__(self, Nome: str, idade: int,dinheiro) -> None:
        super().__init__(Nome, idade)
        self.dinheiro = dinheiro
        raise NotImplementedError("Método não implementado.")
    def fazCompras(self):
        return f"Faz Compras:{self.dinheiro}"

class Pobre(Pessoa):
    def __init__(self, Nome: str, idade: int) -> None:
        super().__init__(Nome, idade)
        raise NotImplementedError("Método não implementado.")
    
    def Trabalha(self):
        return True

class Miseravel(Pessoa):
    def __init__(self, Nome: str, idade: int) -> None:
        super().__init__(Nome, idade)
        raise NotImplementedError("Método não implementado.")

    