from .i_Empregado import Empregado

class Gerente(Empregado):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento


    def get_departamento(self):
        return self.departamento

    def set_departamento(self, departamento):
        self.departamento = departamento

    # Método toString (incluindo informações do departamento)
    def __str__(self):
        return f"{super().__str__()}, Departamento: {self.departamento}"

