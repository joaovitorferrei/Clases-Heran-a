# Crie uma classe chamada Triangulo com os atributos privados __largura e __altura.
# Adicione métodos para definir e obter a largura e altura do Triangulo. 
class Triangulo:
    def __init__(self,altura,largura):
        if isinstance(altura,float) and isinstance(largura,float):
            self.__altura = altura
            self.__largura = largura

    def calculo_altura_largura(self):
        resultado = (self.__altura * self.__largura)/2
        return resultado

    def exibir_informacoes(self):
        print(f"Altura  = {self.__altura}")
        print(f"largura = {self.__largura}")
        print(f"resultado = {self.calculo_altura_largura()}")

a1 = float(input("digite a  altura do seu triangulo: "))
l1 = float(input("digite a largura do seu triangulo: "))

t1 = Triangulo(a1,l1)
t1.calculo_altura_largura()
t1.exibir_informacoes()
        
        


