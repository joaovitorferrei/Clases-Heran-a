# Crie uma classe chamada Cachorro que tenha os atributos nome 
# e raca. Crie um método latir que
# imprime uma mensagem dizendo "Au au!".
class Cachoro:
    def __init__(self,nome,raca):
        self.nome = nome
        self.raca = raca
    def latir(self):
        print("Au au!")
c1 = Cachoro("pé de pano","cão")
c1.latir()