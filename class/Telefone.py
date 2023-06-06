# Crie uma classe chamada Telefone que tenha os atributos modelo e numero. 
# Crie um método
# ligar que imprime uma mensagem dizendo "Ligando para o número [numero]".
class Telefone:
    def __init__(self,modelo,numero_cel):
        self.modelo = modelo
        self.__numero_cel = numero_cel

    def ligar(self):
        print(f"Ligando para o número {self.__numero_cel}")
    
numero = input("digite o número de telefone: ")
t1 = Telefone("samsung",numero)
t1.ligar()