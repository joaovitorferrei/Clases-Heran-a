class Imovel:
    def __init__(self, endereco: str, preco: float) -> None:
        self.endereco = endereco
        self.preco = preco
    
    def get_endereco(self) -> str:
        return self.endereco
    
    def get_preco(self) -> float:
        return self.preco
    
    def display_info(self) -> None:
        print("Endereço:", self.endereco)
        print("Preço:", self.preco)










