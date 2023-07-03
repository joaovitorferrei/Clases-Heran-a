from .f_Vip import Vip
class CamaroteSuperior(Vip):
    def __init__(self, preco: float) -> None:
        super().__init__(preco)
        self.preco = preco + 150
    def display_vip_upper(self):
        print(f"Camarote superior valor: {self.preco}")