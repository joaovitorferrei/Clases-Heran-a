class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano 

    def acelerrar(self,velocidade):
        print(f"O carro {self.modelo} está acelerando a {velocidade} km/h.")

    def exibirinformacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano} ")

c1_marca = input("digite marca: ")            # |
c1_modelo = input("digite o modelo: ")        # |  esse trexo de codigo pega oque o usuario digitar
c1_ano = input("digite o ano: ")              # |
c1_velocidade = input("Digite a velocidade: ")# |
c1 = Carro(c1_marca,c1_modelo,c1_ano) # | esse linha pega oque o usuario digita é passa para a class caro

c1.exibirinformacoes()      # | exibe oque esta dentro da função exibirinformacoes
c1.acelerrar(c1_velocidade) # | esse exibe oque eata dentro da funcão acelerrar