# Crie uma classe chamada Retângulo com os atributos privados __largura e __altura.
# Adicione métodos para definir e obter a largura e altura do retângulo. 
class Retangulo:
    def __init__(self,largura,altura):
        if isinstance(altura,float) and isinstance(largura,float):
            self.__largura = largura
            self.__altura = altura
    def calcular_area(self):
        area = self.__largura * self.__altura
        return area
    def calcular_perimetro(self):
        cauculo_perimetro = (b + h)**2
        return cauculo_perimetro
    def exibir(self):
        print(f"A área do retângulo é: {area_retangulo:.2f}")
        print(f"seu perimetro é {perimetro:.2f}")

b = float(input("digite sua base: ")) 
h = float(input("digite sua altura: "))
t1 = Retangulo(h,b)
area_retangulo = t1.calcular_area() 
perimetro = t1.calcular_perimetro()
t1.exibir()