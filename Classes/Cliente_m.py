from datetime import datetime

class Cliente:
    def __init__(self, nome: str, telefone: str, endereco: str, cliente_antigo: bool = False):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.cliente_antigo = cliente_antigo
        self.data_cadastro = datetime.now()