# Exercício 1: Implemente a classe Funcionario com nome, salario e os métodos
# addAumento(double valor), ganhoAnual() e exibeDados() - imprime os valores do funcionário.
# a. crie a classe Assistente, que também é um funcionário, e que possui um número de
# matrícula (faça os métodos GET e SET). Sobrescreva o método exibeDados().
# b. sabendo que os Assistentes Técnicos possuem um bônus salarial e que os Assistentes
# Administrativos possuem um turno (dia ou noite) e um adicional noturno, crie as classes
# Tecnico e Administrativo e sobrescreva o método ganhoAnual() de ambas as classes
# (Administrativo e Tecnico)
class Funcionario:
    def __init__(self,nome:str,salario:float):
        self.__nome = nome
        self.__salario = salario
    def __addAumento(self):
        aumento_salario = self.__salario * 0.10
        resultado_aumento = aumento_salario + self.__salario
        return resultado_aumento
    def __ganho_anual(self):
        MESES = 12 # Constante Para o messes 
        salario_anual = MESES * self.__salario
        return salario_anual
    def exibir_dados(self):
        print(f"Salario Mensal: {self.__salario}")
        print(f"aumento de salario foi: {self.__addAumento}")
        print(f"salario anual: {self.__ganho_anual()}")
class Assistente(Funcionario):
    def __init__(self, nome: str, salario: float,numero_matricula:str):
        super().__init__(nome, salario)
        self.numero_matricula:str = numero_matricula
    def get_maricula(self):
        return self.numero_matricula 
        
    def __Assistente_tecnico(self):
        bonus_assistente_tecnico = self.__salario * 0.05
        resultado_bonus = self.__salario + bonus_assistente_tecnico
        return resultado_bonus
# Em Desenvolvimento

















