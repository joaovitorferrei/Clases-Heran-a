valor_ingresso_normal = 50 
class Ingresso:
    def __init__(self,preco:float) -> None:
        self.preco = valor_ingresso_normal
    
    def display(self):
        print(self.preco)
class Vip(Ingresso):
    def __init__(self, preco: float) -> None:
        super().__init__(preco)
        self.preco = 50
        pass
