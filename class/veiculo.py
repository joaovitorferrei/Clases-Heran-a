class Veiculo:
    def __init__(self,marca,modelo):
        self.__marca = marca 
        self.__modelo = modelo
    def exibir_veiculo(self):
        print(f"marca: {self.__marca}")
        print(f"modelo: {self.__modelo}")
mar1 = input("digite a marca do seu carro: ")
mod1 = input("digite o modelo do seu carro: ")
v1 = Veiculo(mar1,mod1)
v1.exibir_veiculo()

   