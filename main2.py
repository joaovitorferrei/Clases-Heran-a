from Classes.Funcionario_2 import Funcionario
from Classes.Gerente_2 import Gerente

if __name__=="__main__":
    func = Funcionario(cpf="048783655665",nome="joao")
    gerente = Gerente("931.868.330-86","joao",10)
    print(func.get_informcoes())
    print(gerente.get_informcoes())
    print(gerente.get_total_funcionario())
    print(func.get_total_funcionario())

