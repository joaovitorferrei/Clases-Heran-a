# Crie uma classe chamada Cafeteira que tenha os atributos marca e capacidade. 
# Crie um método fazer_cafe que imprime uma mensagem dizendo "Fazendo café!".
class Cafeteria:
    def __init__(self,marca,capacidade):
        self.marca = marca
        self.capacidade = capacidade
    def fazer_cafe(self):
        print("fazendo café")
c1 = Cafeteria("starbucks","500 ml")
c1.fazer_cafe()