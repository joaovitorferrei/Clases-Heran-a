
from Classes.Animal_2 import Animal,Gato,Cachorro
gato1 = Gato("Mimi", "Persa","")
gato1.get_informacoes()
miado = gato1.miau()
print(miado)

cachorro1 = Cachorro("Rex", "Labrador","")
cachorro1.get_informacoes()
latido = cachorro1.latir()
print(latido)
