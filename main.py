from Classes import Pedido,Cliente
pedidos = []

if __name__=="__main__":
    cliente = Cliente("joão votor ferreira","Rua bastista ,bairro nove de março,n:261")
    pedidos.append(Pedido(prepago=True,numero="001",preco=250.00,cliente=cliente))
    pedidos.append(Pedido(prepago=True,numero="002",preco=350.00,cliente=cliente))
    pedidos.append(Pedido(prepago=True,numero="003",preco=50.00,cliente=cliente))
    pedidos.append(Pedido(prepago=True,numero="004",preco=500.00,cliente=cliente))
    pedidos.append(Pedido(prepago=True,numero="005",preco=150.00,cliente=cliente))


    for pedido in pedidos:
        pedido.expedir()