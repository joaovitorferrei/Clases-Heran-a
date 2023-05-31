from datetime import datetime
from .Cliente import Cliente

class Pedido:
    def __init__(self,prepago=False,numero:str=None,preco=0.0,cliente:Cliente=None) -> None:
        self.dataRecebimento = datetime.today()
        self.ePrepago = prepago
        self.numero = numero
        self.preco = preco
        self.encerrado = False
        self.cliente = cliente
    def expedir(self):
        print("----------- Pedido enviado -----------")
        print(f"Numero : {self.numero}")
        print(f"Cliente: {self.cliente.nome}")
        print(f"Data: {self.dataRecebimento}")
        print(f"Pre-pago: {self.ePrepago}")
        print(f"Preco: {self.preco}")

    def encerrar(self)-> None:
        print("----------- Pedido encerrado -----------")
        self.encerrado=True