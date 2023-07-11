from .h_Empregado import Empregado
class Vendedor(Empregado):
    def __init__(self, nome, salario, percentual_comissao):
        super().__init__(nome, salario)
        self._percentual_comissao = percentual_comissao

    @property
    def percentual_comissao(self):
        return self._percentual_comissao

    @percentual_comissao.setter
    def percentual_comissao(self, novo_percentual):
        self._percentual_comissao = novo_percentual

    def calcularSalario(self):
        comissao = self.getSalario() * (self._percentual_comissao / 100)
        return self.getSalario() + comissao

    def __str__(self):
        salario_com_comissao = self.calcularSalario()
        return f"Nome: {self.getNome()}, Salário sem comissão: {self.getSalario()}, Salário com comissão: {salario_com_comissao}, Percentual de comissão: {self._percentual_comissao}%"

    

