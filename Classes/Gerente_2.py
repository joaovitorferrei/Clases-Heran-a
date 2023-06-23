from .Funcionario_2 import Funcionario
class Gerente(Funcionario):
    def __init__(self, cpf: str = "", nome: str = "",nivel_acesso:int=0) -> None:
        super().__init__(cpf, nome)
        self.__nivel_acesso = nivel_acesso
    
    def get_informcoes(self) -> str:
        return super().get_informcoes()+f"\nNivel: {self.__nivel_acesso}"