from .g_Imovel import Imovel
class Novo(Imovel):
    def __init__(self, endereco: str, preco: float, adicional: float) -> None:
        super().__init__(endereco, preco)
        self.adicional = adicional
    
    def get_adicional(self) -> float:
        return self.adicional
    
    def display_info(self) -> None:
        super().display_info()
        print("Valor adicional:", self.adicional)
