class Empregado:
    def __init__(self, nome: str, salario: float):
        self.__nome = nome
        self.__salario = salario

    def getNome(self):
        return self.__nome

    def getSalario(self):
        return self.__salario


