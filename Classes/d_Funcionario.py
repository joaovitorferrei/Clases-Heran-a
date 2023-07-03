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