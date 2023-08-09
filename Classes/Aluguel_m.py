from classes.Cliente_m import Cliente
from classes.Tema_m import Tema
from datetime import datetime

class Aluguel:
    def __init__(self, cliente: Cliente, endereco: str, tema: Tema, data: str, hora_inicio: str, hora_termino: str):
        self.cliente = cliente
        self.endereco = endereco
        self.tema = tema
        self.data = data
        self.hora_inicio = hora_inicio
        self.hora_termino = hora_termino

    def calcular_valor_total(self):
        valor_total = self.tema.valor_aluguel
        if self.cliente.cliente_antigo and (datetime.now() - self.cliente.data_cadastro).days >= 365 * 5:
            valor_total *= 0.9  # 10% de desconto para clientes antigos com mais de 5 anos de cadastro
        return valor_total
