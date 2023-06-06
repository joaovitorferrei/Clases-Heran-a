# Crie uma classe chamada Carro que tenha os atributos marca, modelo e ano. 
# Crie um método acelerar que aumenta a velocidade do carro em 10 km/h e um método 
# frear que diminui a
# velocidade do carro em 10 km/h.
class Carro:
    def __init__(self,marca,modelo,ano):
        self.__marca = marca 
        self.__modelo = modelo
        self.__ano = ano
        self.velocidade = 50

    def acelerar(self):
        print("-"*30)
        self.velocidade = 50
        print(f"velocidade: {self.velocidade}km")
        self.resultado = self.velocidade + 10
        print(f"aumentar a velocidade {self.velocidade + 10}km")
        print("-"*30)

    def frear(self):
        print(f"velocidade: {self.resultado}")
        print(f"diminuir velocidade {self.resultado-10}km")
        print("-"*30)

    def exibir_veiculo(self):
        print(f"marca: {self.__marca}")
        print(f"modelo: {self.__modelo}")
        print(f"ano: {self.__ano}")

mar1 = input("digite a marca do seu carro: ")
mod1 = input("digite o modelo do seu carro: ")
ano1 = input("digite o ano do carro: ")

v1 = Carro(mar1,mod1,ano1)
v1.acelerar()
v1.frear()
v1.exibir_veiculo()
