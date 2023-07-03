from .d_Funcionario import Funcionario
class Assistente(Funcionario):
    def __init__(self, nome: str, salario: float, numero_matricula: str):
        super().__init__(nome, salario)
        self.__numero_matricula = numero_matricula

    def get_numero_matricula(self) -> str:
        return self.__numero_matricula

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Número de Matrícula: {self.__numero_matricula}")