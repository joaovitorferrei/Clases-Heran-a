class Circulo:
    def __init__(self,raio):
        if isinstance(raio,float):
            self.raio = raio

    def caucular_area(self):
        area = 3.14 * (self.raio)**2
        return area

    def caucular_perimetro(self):
        perimetro = (3.14 * self.raio)*2
        return perimetro

get_raio = float(input("digite o valor do seu raio: "))
c1 = Circulo(get_raio)
area1 = c1.caucular_area()
perimetro1 = c1.caucular_perimetro()

print(f"Calculo do raio é : {get_raio}")
print(f"Calculo da sua area é : {area1:.2f} cm")
print(f"Calculo do seu perimetro é : {perimetro1:.2f}")
        