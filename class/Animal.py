# Crie uma classe chamada Animal que tenha os atributos nome e especie. Crie um 
# método dormir que imprime uma mensagem dizendo "Zzzz".
class Animal:
    def __init__(self,nome,especie):
        self.__nome = nome
        self.__especie = especie
    def dormir(self):
        print('Zzzz')
n1 = Animal("cavalo","mamifero")
n1.dormir()