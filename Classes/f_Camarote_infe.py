from .f_Vip import Vip
class CamaroteInferior(Vip):
    def __init__(self, preco: float,location:int) -> None:
        super().__init__(preco)
        self.location = location

    def display_preco(self):
        print(f"valor do Camarote Inferirior: {self.preco}")

    def display_location(self):
        if self.location <= 100:
            return f"localização do camarote inferior: {self.location}"
        else:
            return "Só temos 100 acentos"
