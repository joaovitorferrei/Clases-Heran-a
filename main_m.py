from Classes.m_Aluguel import Aluguel
from Classes.m_Cliente import Cliente
from Classes.m_Tema import Tema

if __name__ == "__main__":
    cliente1 = Cliente("Joao", "123456789", "Rua A, 123")
    tema1 = Tema("Princesa", ["castelo", "boneca da Cinderela"], 200, "rosa")
    aluguel1 = Aluguel(cliente1, "Rua A, 123", tema1, "2023-08-15", "15:00", "18:00")
    
    print("Detalhes do aluguel:")
    print("Cliente:", aluguel1.cliente.nome)
    print("Telefone:", cliente1.telefone)
    print("Tema:", aluguel1.tema.nome)
    print("Itens:", tema1.itens)
    print("Desconto: 10%")
    print("Data:", aluguel1.data)
    print("Hora de início:", aluguel1.hora_inicio)
    print("Hora de término:", aluguel1.hora_termino)
    print("Valor total:", aluguel1.calcular_valor_total())