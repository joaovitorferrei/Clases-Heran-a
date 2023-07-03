from Classes.__init__b import Funcionario,Gerente

if __name__=="__main__":
    func = Funcionario(cpf="048783655665",nome="joao")
    gerente = Gerente("931.868.330-86","Matheus",10)
    print(func.get_informcoes())
    print(gerente.get_informcoes())
    print(gerente.get_total_funcionario())
    print(func.get_total_funcionario())

