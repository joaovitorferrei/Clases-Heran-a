# Exercício 1: Implemente a classe Funcionario com nome, salario e os métodos
# addAumento(double valor), ganhoAnual() e exibeDados() - imprime os valores do funcionário.
# a. crie a classe Assistente, que também é um funcionário, e que possui um número de
# matrícula (faça os métodos GET e SET). Sobrescreva o método exibeDados().
# b. sabendo que os Assistentes Técnicos possuem um bônus salarial e que os Assistentes
# Administrativos possuem um turno (dia ou noite) e um adicional noturno, crie as classes
# Tecnico e Administrativo e sobrescreva o método ganhoAnual() de ambas as classes
# (Administrativo e Tecnico)
class Animal:
    def __init__(self,nome:str,raca:str) -> None:
        self.__nome = nome
        self.__raca = raca

    def get_informacoes(self):
        print(f"Nome: {self.__nome}\nraca: {self.__raca}")




