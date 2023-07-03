from .g_Imovel import Imovel
class Velho(Imovel):
    def __init__(self, endereco: str, preco: float, desconto: float) -> None:
        super().__init__(endereco, preco)
        self.desconto = desconto
    
    def get_desconto(self) -> float:
        return self.desconto
    
    def display_info(self) -> None:
        super().display_info()
        print("Desconto:", self.desconto)