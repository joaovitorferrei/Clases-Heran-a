from .f_Ingresso import Ingresso
class Cliente_Normal(Ingresso):
    def __init__(self, preco: float) -> None:
        super().__init__(preco)

    def display(self):
        print(f"Cliente Normal Preco: {self.preco}")

