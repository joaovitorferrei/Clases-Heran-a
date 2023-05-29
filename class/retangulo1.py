# Crie uma nova classe chamada "Retângulo" com os atributos "largura" e "altura". Adicione
# um método chamado "calcular_area" que retorna a área do retângulo (largura multiplicada 
# pela altura).
class Retangulo:
    def __init__(self,largura,altura):
        if isinstance(altura,float) and isinstance(largura,float):
            self.largura = largura
            self.altura = altura
    def calcular_area(self):
        area = self.largura * self.altura
        return area
    def calcular_perimetro(self):
        cauculo_perimetro = (b + h)**2
        return cauculo_perimetro

b = float(input("digite sua base: ")) # quando colocar um input voce tem que especificar qual
h = float(input("digite sua altura: "))# tipo de variavel deve retornar 
t1 = Retangulo(h,b)
area_retangulo = t1.calcular_area() # |aqui são estou passando o parametros para a variavel
perimetro = t1.calcular_perimetro() # |

print(f"A área do retângulo é: {area_retangulo:.2f}")# esse trexo exibe os calculos
print(f"seu perimetro é {perimetro:.2f}")

