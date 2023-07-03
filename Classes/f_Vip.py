from .f_Ingresso import Ingresso
class Vip(Ingresso):
    def __init__(self, preco: float) -> None:
        super().__init__(preco)
        self.preco = preco + 50
    
    def display_vip(self):
        print(f"Preço do Camarote Vip {self.preco}")

