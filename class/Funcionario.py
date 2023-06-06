#  Crie uma classe chamada Funcionario que tenha os atributos nome e salario. 
# Crie um método aumento que recebe um valor como parâmetro e aumenta o salário 
# do funcionário em um percentual correspondente a esse valor.
class Funcionario:
    def __init__(self,nome,salario):
        if isinstance(salario,float):  
            self.__nome = nome
            self.__salario = salario
    
    def aumento_salario(self):
        print(f"Funcionario: {self.__nome}")
        resultado = (self.__salario)
        print(f"salario: {self.__salario + resultado}")
        
f1 = Funcionario("marcos",float(1500))
f1.aumento_salario()
