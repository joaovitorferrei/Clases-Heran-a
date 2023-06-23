class Funcionario:
    n_funcionario = 0
    def __init__(self,cpf:str="",nome:str="") -> None:
        self.__cpf = cpf
        self.__nome = nome
        self.add_funcionario()
    def get_informcoes(self)->str:
        return f"Nome: {self.__nome} \nCPF: {self.__cpf}"

    @staticmethod
    def add_funcionario():
        Funcionario.n_funcionario+=1
    
    @staticmethod
    def get_total_funcionario():
        return Funcionario.n_funcionario
        
