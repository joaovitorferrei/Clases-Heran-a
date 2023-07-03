from .d_Assistente import Assistente
class Administrativo(Assistente):
    def __init__(self, nome: str, salario: float, numero_matricula: str, turno: str):
        super().__init__(nome, salario, numero_matricula)
        self.__turno = turno
        self.__adicional_noturno = 0.0
        self.__bonus = 0.0

    def set_adicional_noturno(self, adicional: float):
        self.__adicional_noturno = adicional

    def set_bonus(self, bonus: float):
        self.__bonus = bonus

    def ganho_anual(self) -> float:
        salario_anual = super().ganho_anual()
        if self.__turno == "Noturno":
            return salario_anual + self.__adicional_noturno + self.__bonus
        else:
            return salario_anual + self.__bonus

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Turno: {self.__turno}")
        if self.__turno == "Noturno":
            print(f"Adicional Noturno: R${self.__adicional_noturno:.2f}")
