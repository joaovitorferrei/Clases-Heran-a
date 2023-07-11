from .h_Empregado import Empregado
class Gerente(Empregado):
    def __init__(self, nome: str, salario: float):
        super().__init__(nome, salario)

    @property
    def nome(self):
        return self.getNome()

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def salario(self):
        return self.getSalario()

    @salario.setter
    def salario(self, novo_salario):
        self.__salario = novo_salario

    def __str__(self):
        return f"Nome: {self.getNome()}, Salário: {self.getSalario()}"
