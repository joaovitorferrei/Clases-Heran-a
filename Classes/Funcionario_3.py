# Exercício 1: Implemente a classe Funcionario com nome, salario e os métodos
# addAumento(double valor), ganhoAnual() e exibeDados() - imprime os valores do funcionário.
# a. crie a classe Assistente, que também é um funcionário, e que possui um número de
# matrícula (faça os métodos GET e SET). Sobrescreva o método exibeDados().
# b. sabendo que os Assistentes Técnicos possuem um bônus salarial e que os Assistentes Administrativos possuem um turno (dia ou noite) e um adicional noturno, crie as classes Tecnico e Administrativo e sobrescreva o método ganhoAnual() de 
# ambas as classe (Administrativo e Tecnico)
class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.__nome = nome
        self.__salario = salario

    def get_nome(self) -> str:
        return self.__nome

    def get_salario(self) -> float:
        return self.__salario

    def ganho_anual(self) -> float:
        return 12 * self.__salario

    def exibir_dados(self):
        print("Dado do Funcionario:")
        print(f"Nome: {self.__nome}")
        print(f"Salario Mensal: R${self.__salario:.2f}")
        print(f"Salario Anual: R${self.ganho_anual():.2f}")


class Assistente(Funcionario):
    def __init__(self, nome: str, salario: float, numero_matricula: str):
        super().__init__(nome, salario)
        self.__numero_matricula = numero_matricula

    def get_numero_matricula(self) -> str:
        return self.__numero_matricula

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Número de Matrícula: {self.__numero_matricula}")


class Tecnico(Assistente):
    def __init__(self, nome: str, salario: float, numero_matricula: str, turno: str):
        super().__init__(nome, salario, numero_matricula)
        self.__turno = turno
        self.__adicional_noturno = 0.0

    def set_adicional_noturno(self, adicional: float):
        self.__adicional_noturno = adicional

    def ganho_anual(self) -> float:
        salario_anual = super().ganho_anual()
        if self.__turno == "Noturno":
            return salario_anual + self.__adicional_noturno
        else:
            return salario_anual

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Turno: {self.__turno}")
        if self.__turno == "Noturno":
            print(f"Adicional Noturno: R${self.__adicional_noturno:.2f}")


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




