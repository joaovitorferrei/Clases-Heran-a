from .c_Animal import Animal
class Cachorro(Animal):
    def __init__(self, nome: str, raca: str,latir:str) -> None:
        super().__init__(nome, raca)
        self.__latir = latir
    def latir(self):
        self.__latir = "au au"
        return self.__latir