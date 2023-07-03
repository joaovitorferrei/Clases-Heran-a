from .c_Animal import Animal
class Gato(Animal):
    def __init__(self, nome: str, raca: str,miar:str) -> None:
        super().__init__(nome, raca)
        self.__miar:str = miar

    def miau(self):
        self.__miar = "miau  miau"
        return self.__miar